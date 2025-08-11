import itertools
from collections import Counter

class AnagramGenerator:
    def __init__(self):
        # Basic English word list for validation
        # In a real application, this could be loaded from a file or API
        self.word_list = {
            'cat', 'act', 'tac', 'dog', 'god', 'listen', 'silent', 'enlist',
            'rat', 'tar', 'art', 'eat', 'tea', 'ate', 'eta', 'bat', 'tab',
            'evil', 'vile', 'live', 'veil', 'stop', 'tops', 'pots', 'spot',
            'post', 'opts', 'dear', 'read', 'dare', 'race', 'care', 'acre',
            'arc', 'car', 'stressed', 'desserts', 'heart', 'earth', 'hater',
            'thread', 'hatred', 'dearth', 'red', 'der', 'angel', 'glean',
            'angle', 'lange', 'nag', 'gan', 'bag', 'gab', 'tab', 'bat'
        }
    
    def are_anagrams(self, word1, word2):
        """
        Check if two words are anagrams of each other.
        
        Args:
            word1 (str): First word
            word2 (str): Second word
            
        Returns:
            bool: True if words are anagrams, False otherwise
        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Both inputs must be strings")
        
        # Normalize: convert to lowercase and remove spaces
        word1_clean = word1.lower().replace(' ', '')
        word2_clean = word2.lower().replace(' ', '')
        
        # Check if they have the same character counts
        return Counter(word1_clean) == Counter(word2_clean)
    
    def generate_anagrams(self, letters, min_length=1, max_length=None):
        """
        Generate all possible anagrams from given letters.
        
        Args:
            letters (str): Letters to generate anagrams from
            min_length (int): Minimum length of anagrams (default: 1)
            max_length (int): Maximum length of anagrams (default: length of input)
            
        Returns:
            set: Set of all possible anagram strings
        """
        if not isinstance(letters, str):
            raise TypeError("Letters must be a string")
        
        letters_clean = letters.lower().replace(' ', '')
        if not letters_clean:
            return set()
        
        if max_length is None:
            max_length = len(letters_clean)
        
        anagrams = set()
        
        # Generate permutations of different lengths
        for length in range(min_length, min(max_length + 1, len(letters_clean) + 1)):
            for perm in itertools.permutations(letters_clean, length):
                anagrams.add(''.join(perm))
        
        return anagrams
    
    def find_valid_anagrams(self, letters, min_length=3):
        """
        Find valid English words that are anagrams of the given letters.
        
        Args:
            letters (str): Letters to find anagrams for
            min_length (int): Minimum word length (default: 3)
            
        Returns:
            list: List of valid anagram words, sorted by length
        """
        if not isinstance(letters, str):
            raise TypeError("Letters must be a string")
        
        letters_clean = letters.lower().replace(' ', '')
        if not letters_clean:
            return []
        
        valid_anagrams = []
        letter_counter = Counter(letters_clean)
        
        # Check each word in our word list
        for word in self.word_list:
            if len(word) >= min_length:
                word_counter = Counter(word.lower())
                # Check if the word can be formed from available letters
                if all(word_counter[char] <= letter_counter[char] for char in word_counter):
                    valid_anagrams.append(word)
        
        # Sort by length (shorter words first), then alphabetically
        return sorted(valid_anagrams, key=lambda x: (len(x), x))
    
    def add_word_to_dictionary(self, word):
        """
        Add a word to the internal dictionary.
        
        Args:
            word (str): Word to add to dictionary
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        
        self.word_list.add(word.lower().strip())
    
    def get_anagram_groups(self, word_list=None):
        """
        Group words by their anagram signature.
        
        Args:
            word_list (list): List of words to group (default: use internal dictionary)
            
        Returns:
            dict: Dictionary where keys are sorted letter signatures and values are lists of anagrams
        """
        if word_list is None:
            word_list = list(self.word_list)
        
        anagram_groups = {}
        
        for word in word_list:
            if isinstance(word, str):
                # Create signature by sorting letters
                signature = ''.join(sorted(word.lower().replace(' ', '')))
                if signature not in anagram_groups:
                    anagram_groups[signature] = []
                anagram_groups[signature].append(word)
        
        # Only return groups with more than one word
        return {k: v for k, v in anagram_groups.items() if len(v) > 1}


def main():
    """Command-line interface for the Anagram Generator."""
    generator = AnagramGenerator()
    print("Welcome to the Anagram Generator!")
    print("Available operations:")
    print("1. check - Check if two words are anagrams")
    print("2. generate - Generate all possible anagrams from letters")
    print("3. find - Find valid English words that are anagrams")
    print("4. groups - Show anagram groups from dictionary")
    print("5. add - Add a word to the dictionary")
    
    while True:
        print("\n" + "="*50)
        operation = input("Enter operation (1-5 or 'quit' to exit): ").lower().strip()
        
        if operation in ['quit', 'q', 'exit']:
            break
        
        try:
            if operation in ['1', 'check']:
                word1 = input("Enter first word: ").strip()
                word2 = input("Enter second word: ").strip()
                
                if generator.are_anagrams(word1, word2):
                    print(f"✓ '{word1}' and '{word2}' are anagrams!")
                else:
                    print(f"✗ '{word1}' and '{word2}' are NOT anagrams.")
            
            elif operation in ['2', 'generate']:
                letters = input("Enter letters to generate anagrams from: ").strip()
                min_len = input("Enter minimum length (default 1): ").strip()
                max_len = input("Enter maximum length (default all): ").strip()
                
                min_length = int(min_len) if min_len else 1
                max_length = int(max_len) if max_len else None
                
                anagrams = generator.generate_anagrams(letters, min_length, max_length)
                
                if anagrams:
                    print(f"\nGenerated {len(anagrams)} anagrams:")
                    # Show first 50 anagrams to avoid overwhelming output
                    sorted_anagrams = sorted(anagrams, key=lambda x: (len(x), x))
                    for i, anagram in enumerate(sorted_anagrams[:50]):
                        print(f"  {anagram}")
                    if len(anagrams) > 50:
                        print(f"  ... and {len(anagrams) - 50} more")
                else:
                    print("No anagrams found.")
            
            elif operation in ['3', 'find']:
                letters = input("Enter letters to find anagrams for: ").strip()
                min_len = input("Enter minimum word length (default 3): ").strip()
                
                min_length = int(min_len) if min_len else 3
                
                valid_anagrams = generator.find_valid_anagrams(letters, min_length)
                
                if valid_anagrams:
                    print(f"\nFound {len(valid_anagrams)} valid anagrams:")
                    for word in valid_anagrams:
                        print(f"  {word}")
                else:
                    print("No valid anagrams found in dictionary.")
            
            elif operation in ['4', 'groups']:
                groups = generator.get_anagram_groups()
                
                if groups:
                    print(f"\nFound {len(groups)} anagram groups:")
                    for signature, words in sorted(groups.items()):
                        print(f"  {' / '.join(words)}")
                else:
                    print("No anagram groups found.")
            
            elif operation in ['5', 'add']:
                word = input("Enter word to add to dictionary: ").strip()
                generator.add_word_to_dictionary(word)
                print(f"Added '{word}' to dictionary.")
            
            else:
                print("Invalid operation. Please choose 1-5 or 'quit'.")
        
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    print("\nThank you for using the Anagram Generator!")


if __name__ == "__main__":
    main()