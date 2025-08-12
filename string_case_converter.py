import re

class StringCaseConverter:
    def to_lowercase(self, text):
        """Convert text to lowercase."""
        return text.lower()
    
    def to_uppercase(self, text):
        """Convert text to uppercase."""
        return text.upper()
    
    def to_title_case(self, text):
        """Convert text to title case (first letter of each word capitalized)."""
        return text.title()
    
    def to_camel_case(self, text):
        """Convert text to camelCase (first word lowercase, subsequent words capitalized, no spaces)."""
        # Split by spaces, underscores, hyphens, and other non-alphanumeric characters
        words = re.findall(r'[a-zA-Z0-9]+', text.lower())
        if not words:
            return ""
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    
    def to_pascal_case(self, text):
        """Convert text to PascalCase (all words capitalized, no spaces)."""
        words = re.findall(r'[a-zA-Z0-9]+', text.lower())
        return ''.join(word.capitalize() for word in words)
    
    def to_snake_case(self, text):
        """Convert text to snake_case (lowercase with underscores)."""
        # Replace spaces and hyphens with underscores, then handle camelCase
        text = re.sub(r'[-\s]+', '_', text)
        # Insert underscores before uppercase letters (for camelCase conversion)
        text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
        return text.lower()
    
    def to_kebab_case(self, text):
        """Convert text to kebab-case (lowercase with hyphens)."""
        # Replace spaces and underscores with hyphens, then handle camelCase
        text = re.sub(r'[_\s]+', '-', text)
        # Insert hyphens before uppercase letters (for camelCase conversion)
        text = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
        return text.lower()
    
    def to_alternating_case(self, text):
        """Convert text to aLtErNaTiNg CaSe."""
        result = []
        uppercase = False
        for char in text:
            if char.isalpha():
                result.append(char.upper() if uppercase else char.lower())
                uppercase = not uppercase
            else:
                result.append(char)
        return ''.join(result)
    
    def to_sentence_case(self, text):
        """Convert text to sentence case (first letter capitalized, rest lowercase)."""
        if not text:
            return text
        return text[0].upper() + text[1:].lower()

if __name__ == "__main__":
    converter = StringCaseConverter()
    print("Welcome to the String Case Converter App!")
    print("Available conversions: lowercase, uppercase, title, camel, pascal, snake, kebab, alternating, sentence")
    
    while True:
        conversion = input("Enter conversion type (or 'quit' to exit): ").lower()
        if conversion == 'quit':
            break
        
        valid_conversions = ['lowercase', 'uppercase', 'title', 'camel', 'pascal', 'snake', 'kebab', 'alternating', 'sentence']
        if conversion not in valid_conversions:
            print("Invalid conversion type. Please try again.")
            continue
        
        text = input("Enter text to convert: ")
        
        if conversion == 'lowercase':
            result = converter.to_lowercase(text)
        elif conversion == 'uppercase':
            result = converter.to_uppercase(text)
        elif conversion == 'title':
            result = converter.to_title_case(text)
        elif conversion == 'camel':
            result = converter.to_camel_case(text)
        elif conversion == 'pascal':
            result = converter.to_pascal_case(text)
        elif conversion == 'snake':
            result = converter.to_snake_case(text)
        elif conversion == 'kebab':
            result = converter.to_kebab_case(text)
        elif conversion == 'alternating':
            result = converter.to_alternating_case(text)
        else:  # sentence
            result = converter.to_sentence_case(text)
        
        print(f"Result: {result}")
    
    print("Thank you for using the String Case Converter App!")