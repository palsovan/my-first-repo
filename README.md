# Python Utility Apps

This repository contains two Python applications: a Calculator App and an Anagram Generator App.

## Calculator App

A simple calculator application that provides basic arithmetic operations.

### Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

### Usage

```bash
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

## Anagram Generator App

A comprehensive anagram generator that can check anagrams, generate permutations, and find valid English words.

### Features

- **Check Anagrams**: Verify if two words are anagrams of each other
- **Generate Anagrams**: Create all possible permutations from given letters
- **Find Valid Words**: Discover valid English words that are anagrams of input letters
- **Anagram Groups**: Display groups of words that are anagrams of each other
- **Dictionary Management**: Add custom words to the internal dictionary
- **Case Insensitive**: Handles uppercase, lowercase, and mixed case inputs
- **Space Handling**: Ignores spaces in anagram comparisons

### Usage

```bash
python anagram_generator.py
```

The application provides an interactive menu with the following options:

1. **Check** - Check if two words are anagrams
2. **Generate** - Generate all possible anagrams from letters
3. **Find** - Find valid English words that are anagrams
4. **Groups** - Show anagram groups from dictionary
5. **Add** - Add a word to the dictionary

### Examples

```python
from anagram_generator import AnagramGenerator

generator = AnagramGenerator()

# Check if two words are anagrams
print(generator.are_anagrams('listen', 'silent'))  # True
print(generator.are_anagrams('hello', 'world'))    # False

# Generate all anagrams from letters
anagrams = generator.generate_anagrams('cat')
print(anagrams)  # {'a', 'c', 't', 'ac', 'at', 'ca', 'ct', 'ta', 'tc', 'cat', 'cta', 'act', 'atc', 'tac', 'tca'}

# Find valid English words
valid_words = generator.find_valid_anagrams('listen')
print(valid_words)  # ['enlist', 'listen', 'silent']
```

## Running Tests

To run the unit tests for both applications:

```bash
# Test calculator
python -m unittest test_calculator.py

# Test anagram generator
python -m unittest test_anagram_generator.py

# Run all tests
python -m unittest discover
```

## File Structure

- `calculator.py`: Calculator class and command-line interface
- `test_calculator.py`: Unit tests for the Calculator class
- `anagram_generator.py`: AnagramGenerator class and command-line interface
- `test_anagram_generator.py`: Unit tests for the AnagramGenerator class
- `README.md`: This file, containing project documentation

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## License

This project is licensed under the terms of the LICENSE file in the root directory.