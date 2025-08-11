import unittest
from anagram_generator import AnagramGenerator

class TestAnagramGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AnagramGenerator()

    def test_are_anagrams_basic(self):
        """Test basic anagram checking functionality."""
        # Positive cases
        self.assertTrue(self.generator.are_anagrams('listen', 'silent'))
        self.assertTrue(self.generator.are_anagrams('evil', 'vile'))
        self.assertTrue(self.generator.are_anagrams('a', 'a'))
        self.assertTrue(self.generator.are_anagrams('', ''))
        
        # Negative cases
        self.assertFalse(self.generator.are_anagrams('hello', 'world'))
        self.assertFalse(self.generator.are_anagrams('cat', 'dog'))
        self.assertFalse(self.generator.are_anagrams('listen', 'listing'))

    def test_are_anagrams_case_insensitive(self):
        """Test that anagram checking is case insensitive."""
        self.assertTrue(self.generator.are_anagrams('Listen', 'Silent'))
        self.assertTrue(self.generator.are_anagrams('EVIL', 'vile'))
        self.assertTrue(self.generator.are_anagrams('CaT', 'TaC'))

    def test_are_anagrams_with_spaces(self):
        """Test anagram checking with spaces."""
        self.assertTrue(self.generator.are_anagrams('a gentleman', 'elegant man'))
        self.assertTrue(self.generator.are_anagrams('conversation', 'voices rant on'))
        self.assertTrue(self.generator.are_anagrams('the eyes', 'they see'))

    def test_are_anagrams_type_error(self):
        """Test that non-string inputs raise TypeError."""
        with self.assertRaises(TypeError):
            self.generator.are_anagrams(123, 'hello')
        with self.assertRaises(TypeError):
            self.generator.are_anagrams('hello', None)
        with self.assertRaises(TypeError):
            self.generator.are_anagrams([], 'hello')

    def test_generate_anagrams_basic(self):
        """Test basic anagram generation."""
        anagrams = self.generator.generate_anagrams('ab')
        expected = {'a', 'b', 'ab', 'ba'}
        self.assertEqual(anagrams, expected)

    def test_generate_anagrams_single_char(self):
        """Test anagram generation with single character."""
        anagrams = self.generator.generate_anagrams('a')
        expected = {'a'}
        self.assertEqual(anagrams, expected)

    def test_generate_anagrams_empty_string(self):
        """Test anagram generation with empty string."""
        anagrams = self.generator.generate_anagrams('')
        self.assertEqual(anagrams, set())

    def test_generate_anagrams_with_length_limits(self):
        """Test anagram generation with length constraints."""
        anagrams = self.generator.generate_anagrams('abc', min_length=2, max_length=2)
        expected = {'ab', 'ac', 'ba', 'bc', 'ca', 'cb'}
        self.assertEqual(anagrams, expected)

    def test_generate_anagrams_min_length_only(self):
        """Test anagram generation with minimum length constraint."""
        anagrams = self.generator.generate_anagrams('ab', min_length=2)
        expected = {'ab', 'ba'}
        self.assertEqual(anagrams, expected)

    def test_generate_anagrams_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            self.generator.generate_anagrams(123)
        with self.assertRaises(TypeError):
            self.generator.generate_anagrams(None)

    def test_find_valid_anagrams_basic(self):
        """Test finding valid anagrams from dictionary."""
        # Test with letters that form known words
        anagrams = self.generator.find_valid_anagrams('cat')
        self.assertIn('cat', anagrams)
        self.assertIn('act', anagrams)

    def test_find_valid_anagrams_with_min_length(self):
        """Test finding valid anagrams with minimum length constraint."""
        anagrams = self.generator.find_valid_anagrams('listen', min_length=6)
        # Should find words of length 6 or more
        for word in anagrams:
            self.assertGreaterEqual(len(word), 6)

    def test_find_valid_anagrams_no_matches(self):
        """Test finding valid anagrams when no matches exist."""
        anagrams = self.generator.find_valid_anagrams('xyz')
        self.assertEqual(anagrams, [])

    def test_find_valid_anagrams_empty_input(self):
        """Test finding valid anagrams with empty input."""
        anagrams = self.generator.find_valid_anagrams('')
        self.assertEqual(anagrams, [])

    def test_find_valid_anagrams_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            self.generator.find_valid_anagrams(123)

    def test_add_word_to_dictionary(self):
        """Test adding words to the dictionary."""
        original_size = len(self.generator.word_list)
        self.generator.add_word_to_dictionary('newword')
        self.assertEqual(len(self.generator.word_list), original_size + 1)
        self.assertIn('newword', self.generator.word_list)

    def test_add_word_to_dictionary_case_normalization(self):
        """Test that added words are normalized to lowercase."""
        self.generator.add_word_to_dictionary('UPPERCASE')
        self.assertIn('uppercase', self.generator.word_list)
        self.assertNotIn('UPPERCASE', self.generator.word_list)

    def test_add_word_to_dictionary_whitespace_handling(self):
        """Test that whitespace is stripped from added words."""
        self.generator.add_word_to_dictionary('  spaced  ')
        self.assertIn('spaced', self.generator.word_list)

    def test_add_word_to_dictionary_type_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            self.generator.add_word_to_dictionary(123)

    def test_get_anagram_groups_basic(self):
        """Test getting anagram groups from dictionary."""
        groups = self.generator.get_anagram_groups()
        
        # Should be a dictionary
        self.assertIsInstance(groups, dict)
        
        # Each group should have more than one word
        for signature, words in groups.items():
            self.assertGreater(len(words), 1)
            
        # Check that known anagrams are grouped together
        # Find the group containing 'cat'
        cat_group = None
        for signature, words in groups.items():
            if 'cat' in words:
                cat_group = words
                break
        
        if cat_group:  # Only test if 'cat' is in our word list
            self.assertIn('act', cat_group)

    def test_get_anagram_groups_custom_word_list(self):
        """Test getting anagram groups from custom word list."""
        custom_words = ['cat', 'act', 'dog', 'god', 'hello']
        groups = self.generator.get_anagram_groups(custom_words)
        
        # Should find groups for cat/act and dog/god
        self.assertEqual(len(groups), 2)
        
        # Check that the groups are correct
        signatures = list(groups.keys())
        cat_signature = ''.join(sorted('cat'))
        dog_signature = ''.join(sorted('dog'))
        
        self.assertIn(cat_signature, signatures)
        self.assertIn(dog_signature, signatures)

    def test_get_anagram_groups_no_anagrams(self):
        """Test getting anagram groups when no anagrams exist."""
        custom_words = ['hello', 'world', 'python']
        groups = self.generator.get_anagram_groups(custom_words)
        self.assertEqual(groups, {})

    def test_get_anagram_groups_with_non_strings(self):
        """Test that non-string items in word list are handled gracefully."""
        custom_words = ['cat', 'act', 123, None, 'dog']
        groups = self.generator.get_anagram_groups(custom_words)
        
        # Should still work and find the cat/act group
        self.assertGreater(len(groups), 0)

    def test_anagram_generation_performance(self):
        """Test that anagram generation doesn't hang on reasonable inputs."""
        # This should complete quickly
        anagrams = self.generator.generate_anagrams('abcd', max_length=3)
        self.assertIsInstance(anagrams, set)
        self.assertGreater(len(anagrams), 0)

    def test_duplicate_letters_handling(self):
        """Test handling of duplicate letters in anagram generation."""
        anagrams = self.generator.generate_anagrams('aab')
        # Should handle duplicates correctly
        self.assertIn('aab', anagrams)
        self.assertIn('aba', anagrams)
        self.assertIn('baa', anagrams)

    def test_case_sensitivity_in_find_valid_anagrams(self):
        """Test that find_valid_anagrams handles case correctly."""
        anagrams1 = self.generator.find_valid_anagrams('CAT')
        anagrams2 = self.generator.find_valid_anagrams('cat')
        self.assertEqual(anagrams1, anagrams2)


if __name__ == '__main__':
    unittest.main()