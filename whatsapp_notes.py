"""Turn a WhatsApp exported chat (.txt) into markdown revision notes.

Usage: python whatsapp_notes.py chat.txt -o notes.md [--me "Your Name"]
"""

import argparse
import re
from collections import OrderedDict

# 07/09/26, 10:15 - Name: message   |   [07/09/26, 10:15:03] Name: message
LINE = re.compile(
    r"^\[?(\d{1,2}[/.]\d{1,2}[/.]\d{2,4}),?\s+"
    r"(\d{1,2}:\d{2}(?::\d{2})?\s*(?:[AaPp][Mm])?)\]?\s*[-–]?\s*"
    r"([^:]{1,60}?):\s(.*)$"
)

NOISE = (
    "<media omitted>", "image omitted", "video omitted", "sticker omitted",
    "audio omitted", "this message was deleted", "you deleted this message",
    "missed voice call", "missed video call", "null",
)
FILLER = {
    "ok", "okay", "k", "hmm", "hm", "yes", "no", "yeah", "yep", "nope", "lol",
    "haha", "hahaha", "thanks", "thank you", "ty", "welcome", "hi", "hello",
    "hey", "good morning", "good night", "gm", "gn", "bye", "sure", "done",
    "cool", "nice", "great", "👍", "ok ok",
}
URL = re.compile(r"https?://\S+")


def parse(path):
    msgs = []
    with open(path, encoding="utf-8", errors="ignore") as fh:
        for raw in fh:
            raw = raw.rstrip("\n").replace("\u200e", "")
            m = LINE.match(raw)
            if m:
                date, _, sender, text = m.groups()
                msgs.append({"date": date, "sender": sender.strip(), "text": text.strip()})
            elif msgs:
                msgs[-1]["text"] += "\n" + raw.strip()
    return msgs


def is_noise(text):
    low = text.lower().strip()
    if not low or low in FILLER:
        return True
    if any(n in low for n in NOISE):
        return True
    return len(low) < 12 and not URL.search(low)


def score(text):
    """Higher = more note-worthy."""
    s = min(len(text) / 120, 3)
    low = text.lower()
    if URL.search(text):
        s += 2
    if "```" in text or re.search(r"\b(def |class |function |SELECT |import )", text):
        s += 2
    if any(w in low for w in ("because", "note", "remember", "important", "key",
                             "difference", "vs ", "means", "steps", "how to", "why")):
        s += 1.5
    if "?" in text:
        s += 0.5
    if text.count("\n") >= 2:
        s += 1
    return s


def build(msgs, min_score, me):
    days = OrderedDict()
    for msg in msgs:
        if is_noise(msg["text"]):
            continue
        if me and msg["sender"].lower() != me.lower():
            pass  # keep everyone; --me only affects labelling
        sc = score(msg["text"])
        if sc < min_score:
            continue
        days.setdefault(msg["date"], []).append((sc, msg))
    return days


def render(days, title):
    out = [f"# {title}", ""]
    links = []
    for date, items in days.items():
        out.append(f"## {date}")
        out.append("")
        for _, msg in items:
            text = msg["text"]
            links.extend(URL.findall(text))
            body = "\n".join("  " + ln if i else ln
                             for i, ln in enumerate(text.split("\n")))
            out.append(f"- **{msg['sender']}** — {body}")
        out.append("")
    if links:
        out += ["## Links", ""] + [f"- {u}" for u in dict.fromkeys(links)] + [""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chat", help="WhatsApp exported .txt file")
    ap.add_argument("-o", "--out", default="notes.md")
    ap.add_argument("--me", default=None, help="your name as it appears in the export")
    ap.add_argument("--min-score", type=float, default=2.0,
                    help="lower = more messages kept")
    args = ap.parse_args()

    msgs = parse(args.chat)
    days = build(msgs, args.min_score, args.me)
    kept = sum(len(v) for v in days.values())
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(render(days, "Revision Notes"))
    print(f"{len(msgs)} messages -> {kept} notes across {len(days)} days -> {args.out}")


if __name__ == "__main__":
    main()
