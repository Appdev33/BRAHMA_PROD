 import java.util.Map;



import java.util.HashMap;

public class TriesPractice {
	
	
	class Trie{
		
		static int ALPHABET_SIZE = 26;
		static TrieNode root;
		static TrieNode temp;
		
		class TrieNode{
			Map<Character, TrieNode> children;
			boolean isEndWord;
			
			public TrieNode() {
				this.children = new HashMap<>();
				this.isEndWord = false;
			}
			
		}
		
		Trie(){
			root = new TrieNode();
			temp = root;
		}

	    // Insert a word into the Trie
	    public void insert(String word) {
	        TrieNode currentNode = root;
	        for (char c : word.toCharArray()) {
	            currentNode = currentNode.children.computeIfAbsent(c, k -> new TrieNode());
	        }
	        currentNode.isEndWord = true;
	    }

	    // Search for a word in the Trie
	    public boolean searchInTrie(String word) {
	        TrieNode currentNode = root;
	        for (char c : word.toCharArray()) {
	            currentNode = currentNode.children.get(c);
	            if (currentNode == null) {
	                return false;
	            }
	        }
	        return currentNode.isEndWord;
	    }

	    // Check if there is any word in the Trie that starts with the given prefix
	    public boolean startsWith(String prefix) {
	        TrieNode currentNode = root;
	        for (char c : prefix.toCharArray()) {
	            currentNode = currentNode.children.get(c);
	            if (currentNode == null) {
	                return false;
	            }
	        }
	        return true;
	    }
	    
	    
	    public boolean update(String old_word, String new_word) {
	        if (!searchInTrie(old_word)) {
	            return false; // Old word doesn't exist, update not possible
	        }

	       deleteWord(this.temp, old_word, 0); 
	            insert(new_word); // Insert the new word
	            return true;
	        
//	        return false; // Deletion failed
	    }

	  ///	    https://www.youtube.com/watch?v=FAj5SQD9XI8
	    public boolean deleteWord(TrieNode current, String word, int index) {
	        // Base case: if the end of the word is reached
	        if (index == word.length()) {
	            // If the word is not marked as end of a word, it doesn't exist
	            if (!current.isEndWord) {
	                return false;
	            }
	            // Unmark the end of the word
	            current.isEndWord = false;
	            // If the current node has no children, it can be deleted
	            return current.children.isEmpty();
	        }

	        char ch = word.charAt(index);
	        TrieNode node = current.children.get(ch);

	        // If the character does not exist in children, the word doesn't exist
	        if (node == null) {
	            return false;
	        }

	        // Recursively delete the word from the child node
	        boolean shouldDeleteCurrentNode = deleteWord(node, word, index + 1);

	        // If true, delete the mapping of character and TrieNode reference from map
	        if (shouldDeleteCurrentNode) {
	            current.children.remove(ch);
	            // Return true if no children and not end of another word
	            return current.children.isEmpty() && !current.isEndWord;
	        }

	        // No need for the final return true; just return false by default
	        return false;
	    }

   }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TriesPractice obj = new TriesPractice();
		TriesPractice.Trie trie = obj.new Trie(); 
		
		String[] strings = {"app","apple", "banana",  "bat", "batman", "cat", "dog", "doggie", "car"};

        for (String word : strings) {
            trie.insert(word);
        }
        
        System.out.println("**********************");
        
        String[] search = {"ap", "banana","apple", "apricot"};
        for (String word : search) {
            System.out.println(trie.searchInTrie(word) );
        }
        
        System.out.println("**********************");
        String[] startsWith = {"ap", "banana","apple"};
        for (String word : startsWith) {
            System.out.println(trie.startsWith(word) );
        }
        
        System.out.println(trie.searchInTrie("apple")+"  Searching...");
        
        System.out.println(trie.update( "apple", "apricot") +"---Update");
        
        System.out.println(trie.searchInTrie("apricot") + " and " + trie.searchInTrie("apple"));
        
        System.out.println("DELETING PROCESS **********************");
        System.out.println(trie.deleteWord(trie.root, "apricot", 0));
        
        

        for (String word : search) {
            System.out.println(trie.searchInTrie(word) );
        }
        
	}

}
