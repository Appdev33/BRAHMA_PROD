package Graph;

import java.util.*;

class Trie {
    static TrieNode root;

    static class TrieNode {
        static final int ALPHABET_SIZE = 26;
        boolean isWordEnd;
        TrieNode[] children;

        TrieNode() {
            isWordEnd = false;
            children = new TrieNode[ALPHABET_SIZE];
        }
    }

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            current = current.children[index];
        }

        current.isWordEnd = true;
    }

    public boolean search(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (current.children[index] == null) {
                return false;
            }
            current = current.children[index];
        }

        return current.isWordEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode current = root;

        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            if (current.children[index] == null) {
                return false;
            }
            current = current.children[index];
        }

        return true;
    }

    public void delete(String word) {
        delete(root, word, 0);
    }

    private boolean delete(TrieNode current, String word, int index) {
        if (index == word.length()) {
            if (!current.isWordEnd) {
                return false; // Word not present in trie
            }
            current.isWordEnd = false;
            return hasNoChildren(current);
        }

        char ch = word.charAt(index);
        int chIndex = ch - 'a';
        TrieNode nextNode = current.children[chIndex];
        if (nextNode == null) {
            return false; // Word not present in trie
        }

        boolean shouldDeleteCurrentNode = delete(nextNode, word, index + 1);

        if (shouldDeleteCurrentNode) {
            current.children[chIndex] = null;
            return hasNoChildren(current) && !current.isWordEnd;
        }

        return false;
    }

    private boolean hasNoChildren(TrieNode node) {
        for (TrieNode child : node.children) {
            if (child != null) {
                return false;
            }
        }
        return true;
    }

    public void display() {
        List<String> words = new ArrayList<>();
        display(root, "", words);
        System.out.println("Trie Contents:");
        for (String word : words) {
            System.out.println(word);
        }
    }

    private void display(TrieNode current, String prefix, List<String> words) {
        if (current.isWordEnd) {
            words.add(prefix);
        }

        for (int i = 0; i < current.children.length; i++) {
            if (current.children[i] != null) {
                char ch = (char) ('a' + i);
                display(current.children[i], prefix + ch, words);
            }
        }
    }

    public static void main(String[] args) {
        Trie trie = new Trie();

        trie.insert("apple");
        trie.insert("app");
        trie.insert("bat");
        trie.insert("batman");

        System.out.println(trie.search("apple"));   // Output: true
        System.out.println(trie.search("app"));     // Output: true
        System.out.println(trie.search("bat"));     // Output: true
        System.out.println(trie.startsWith("batm")); // Output: true

        trie.display();

        trie.delete("app");
        System.out.println(trie.search("app"));     // Output: false

        trie.display();
    }
}
