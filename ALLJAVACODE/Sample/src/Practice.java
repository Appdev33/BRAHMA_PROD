
//https://www.youtube.com/watch?v=syWGhtvzk80
public class Practice {
	
	class Trie{
		static int ALPHABET_SIZE = 26;
		static TrieNode root; 
		
		class TrieNode{
			TrieNode children[];
			boolean endOfWord;
			
			TrieNode() {
				this.children = new TrieNode[ALPHABET_SIZE];
				this.endOfWord = false;
			}
		}
		
		Trie(){
			root = new TrieNode();
		}
		
		public void addToTrie(String str) {
			TrieNode crawl = root;
			for(char c: str.toCharArray()) {
				if(crawl.children[c-'a']==null) {
					crawl.children[c-'a'] = new TrieNode();
				}
				crawl = crawl.children[c-'a'];
			}
			crawl.endOfWord = true;
		}

		public boolean searchInTrie(String word) {
			TrieNode crawl = root;
			
			for(char c: word.toCharArray()) {
				if(crawl.children[c-'a']==null)
					return false;
				else{
					crawl = crawl.children[c-'a'];
				}
			}
			return crawl.endOfWord;
		}
		

		
		public boolean startsWith(String word) {
			TrieNode crawl = root;
			
			for(char c: word.toCharArray()) {
				if(crawl.children[c-'a']==null)
					return false;
				else{
					crawl = crawl.children[c-'a'];
				}
			}
			return true;
		}
		
		
		public void deleteWord(String word) {
	        delete(root, word, 0);
	    }

	    public boolean delete(TrieNode current, String word, int index) {
	    	
	        if (index == word.length()) {
	            if (!current.endOfWord) {
	                return false; // Word not present in trie
	            }
	            current.endOfWord = false;
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
	            return hasNoChildren(current) && !current.endOfWord;
	        }

	        return false;
	    }

	    public boolean hasNoChildren(TrieNode node) {
	        for (TrieNode child : node.children) {
	            if (child != null) {
	                return false;
	            }
	        }
	        return true;
	    }
		
		public void getChildren() {}
		
		public void countChildren() {}
		
		public void deleteChild() {}
		

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Practice obj = new Practice();
		Practice.Trie trie = obj.new Trie(); 
		String[] strings = {"app","apple", "banana", "apricot",  "bat", "batman", "cat", "dog", "doggie", "car"};

        for (String word : strings) {
            trie.addToTrie(word);
        }
        System.out.println("**********************");
        String[] search = {"app", "banana","apple"};
        for (String word : search) {
            System.out.println(trie.searchInTrie(word) );
        }
        System.out.println("**********************");
        String[] startsWith = {"ap", "anana","apple"};
        for (String word : startsWith) {
            System.out.println(trie.startsWith(word) );
        }
        
        trie.deleteWord("hello");

	}

	

}
