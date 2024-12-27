import re
from collections import Counter

# List of common words to exclude (articles, common words, and names)
# stop_words = {
#     "a", "an", "the", "i", "you", "he", "she", "it", "we", "they", "them", "us", "his", "her", "theirs", "mine", "ours",
#     "in", "on", "at", "by", "for", "to", "with", "about", "as", "from", "of", "through", "between", "under", "over",
#     "and", "but", "or", "nor", "so", "yet", "either", "neither", "this", "that", "these", "those", "each", "every", 
#     "some", "no", "all", "any", "much", "more", "less", "such", "is", "are", "was", "were", "be", "been", "being", 
#     "has", "have", "had", "do", "does", "did", "will", "would", "can", "could", "shall", "should", "may", "might", 
#     "must", "not", "only", "very", "too", "also", "even", "just", "always", "never", "here", "there", "when", "where", 
#     "why", "how", "which", "all", "any", "one", "two", "three", "several", "both", "few", "many", "much", "more", "most", 
#     "least"
# }
stop_words = {""}

# Example song lyrics (replace with actual lyrics)
lyrics = """
Hurt by Johnny Cash: I hurt myself today, to see if I still feel
Wish You Were Here by Pink Floyd: How I wish, how I wish you were here
Everybody Hurts by R.E.M.: When your day is long, and the night, the night is yours alone
Hallelujah by Leonard Cohen: Now I’ve heard there was a secret chord
9 Crimes by Damien Rice: Leave me out with the waste
Lovely by Billie Eilish & Khalid: Isn't it lovely, all alone
How to Disappear Completely by Radiohead: That’s why I’m lying here
Snuff by Slipknot: Deliver me into my fate
Liability by Lorde: I do my best to meet her demands
"""

# Function to preprocess the lyrics, remove stop words, and count word frequencies
def get_most_common_words(text, top_n=10):
    # Remove non-alphabetic characters, convert to lowercase, and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out the stop words
    filtered_words = [word for word in words if word not in stop_words]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Get the most common words
    most_common = word_counts.most_common(top_n)
    
    return most_common

# Get the 10 most frequent words from the lyrics, excluding stop words
top_words = get_most_common_words(lyrics)
print("Top 10 most common words (excluding stop words):", top_words)
