from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.isEndOfWord = True

    def contains_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.isEndOfWord

    def update(self, old_word, new_word):
        if self.delete(self.root, old_word, 0):
            self.insert(new_word)

    def delete(self, node, word, depth):
        # Base case: If we've reached the end of the word
        if depth == len(word):
            # If the word is not marked as the end of a valid word
            if not node.isEndOfWord:
                return False  # Word not found, nothing to delete

            # Unmark the end of the word
            node.isEndOfWord = False

            # If the node has no children, it can be deleted
            return len(node.children) == 0

        # Recursive case: Process the current character
        char = word[depth]
        # Ensure the character exists in the current node's children
        if char not in node.children:
            return False  # Word not found, nothing to delete

        # Recurse to the next level
        should_delete_next = self.delete(node.children[char], word, depth + 1)

        # If the child node should be deleted
        if should_delete_next:
            del node.children[char]

            # Check if the current node is now empty and not the end of another word
            return len(node.children) == 0 and not node.isEndOfWord

        return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("hell")
    trie.insert("world")
    trie.delete(trie.root, "world", 0)
    trie.update("hell", "hello")
    print("Hello, world!")
    print(trie.contains_word("work"))
    print(trie.search("work"))
    print(
        trie.root.children["h"]
        .children["e"]
        .children["l"]
        .children["l"]
        .children["o"]
        .isEndOfWord
    )


# class TrieNode:
#     children = {}
#     is_end_of_word = False

#     @classmethod
#     def create_node(cls):
#         node = cls()
#         node.children = {}
#         node.is_end_of_word = False
#         return node

# class Trie:
#     root = TrieNode.create_node()

#     @classmethod
#     def insert(cls, word):
#         current_node = cls.root
#         for char in word:
#             if char not in current_node.children:
#                 current_node.children[char] = TrieNode.create_node()
#             current_node = current_node.children[char]
#         current_node.is_end_of_word = True

#     @classmethod
#     def contains_word(cls, word):
#         current_node = cls.root
#         for char in word:
#             if char not in current_node.children:
#                 return False
#             current_node = current_node.children[char]
#         return True

#     @classmethod
#     def search(cls, word):
#         current_node = cls.root
#         for char in word:
#             if char not in current_node.children:
#                 return False
#             current_node = current_node.children[char]
#         return current_node.is_end_of_word

#     @classmethod
#     def update(cls, old_word, new_word):
#         if cls.delete(cls.root, old_word, 0):
#             cls.insert(new_word)

#     @classmethod
#     def delete(cls, node, word, depth):
#         if depth == len(word):
#             if not node.is_end_of_word:
#                 return False
#             node.is_end_of_word = False
#             return len(node.children) == 0

#         char = word[depth]
#         if char not in node.children:
#             return False

#         should_delete_next = cls.delete(node.children[char], word, depth + 1)

#         if should_delete_next:
#             del node.children[char]
#             return len(node.children) == 0 and not node.is_end_of_word

#         return False


# if __name__ == "__main__":
#     Trie.insert("hell")
#     Trie.insert("world")
#     Trie.delete(Trie.root, "world", 0)
#     Trie.update("hell", "hello")
#     print("Hello, world!")
#     print(Trie.contains_word("work"))
#     print(Trie.search("work"))
#     print(Trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].is_end_of_word)
