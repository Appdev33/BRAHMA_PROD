from collections import defaultdict
# http://youtube.com/watch?v=fzGVMOmBQWo

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
    Trie.insert("hell")
    Trie.insert("world")
    Trie.delete(Trie.root, "world", 0)
    Trie.update("hell", "hello")
    print("Hello, world!")
    print(Trie.contains_word("work"))
    print(Trie.search("work"))
    print(Trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].is_end_of_word)


variable = "hello"
var1, var2 = ""
int_var,float_var =""
#1️⃣ f-Strings (Python 3.6+) ✅ (Recommended)
#Syntax:
print(f"text {variable}")
Example:
key_to_check = "apple"
treeMap = {"apple": 1, "banana": 2}

print(f"Contains key '{key_to_check}'? {key_to_check in treeMap}")

#2️⃣ .format() Method (Python 2.7 & 3.x)
#Syntax:
print("text {}".format(variable))
print("text {0} {1}".format(var1, var2))
print("text {name}".format(name=variable))
#Example:
print("Contains key '{}' ? {}".format(key_to_check, key_to_check in treeMap))
print("Contains key '{0}'? {1}".format(key_to_check, key_to_check in treeMap))
print("Contains key '{key}'? {value}".format(key=key_to_check, value=key_to_check in treeMap))

#3️⃣ % Formatting (Old Style, Python 2 & 3)
#Syntax:
print("text %s" % variable)
print("text %d %f" % (int_var, float_var))

print("Contains key '%s'? %s" % (key_to_check, key_to_check in treeMap))

#4️⃣ String Concatenation (+)
#Syntax:
print("text " + str(variable))

print("Contains key '" + key_to_check + "'? " + str(key_to_check in treeMap))

#5️⃣ Comma-Separated Printing
#Syntax:
print("text", variable)

print("Contains key '", key_to_check, "'?", key_to_check in treeMap)

#6️⃣ Using join() (For Lists or Multiple Variables)
#Syntax:
print("separator".join([str(var1), str(var2)]))
Example:
print(" ".join(["Contains key '", key_to_check, "'?", str(key_to_check in treeMap)]))

#7️⃣ Using repr() for Debugging
#Syntax:
print(f"text {repr(variable)}")

print(f"Contains key {repr(key_to_check)}? {repr(key_to_check in treeMap)}")
