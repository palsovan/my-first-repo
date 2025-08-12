import unittest
from string_case_converter import StringCaseConverter

class TestStringCaseConverter(unittest.TestCase):
    def setUp(self):
        self.converter = StringCaseConverter()

    def test_to_lowercase(self):
        self.assertEqual(self.converter.to_lowercase("HELLO WORLD"), "hello world")
        self.assertEqual(self.converter.to_lowercase("Hello World"), "hello world")
        self.assertEqual(self.converter.to_lowercase("hello world"), "hello world")
        self.assertEqual(self.converter.to_lowercase(""), "")
        self.assertEqual(self.converter.to_lowercase("123ABC"), "123abc")

    def test_to_uppercase(self):
        self.assertEqual(self.converter.to_uppercase("hello world"), "HELLO WORLD")
        self.assertEqual(self.converter.to_uppercase("Hello World"), "HELLO WORLD")
        self.assertEqual(self.converter.to_uppercase("HELLO WORLD"), "HELLO WORLD")
        self.assertEqual(self.converter.to_uppercase(""), "")
        self.assertEqual(self.converter.to_uppercase("123abc"), "123ABC")

    def test_to_title_case(self):
        self.assertEqual(self.converter.to_title_case("hello world"), "Hello World")
        self.assertEqual(self.converter.to_title_case("HELLO WORLD"), "Hello World")
        self.assertEqual(self.converter.to_title_case("hello-world"), "Hello-World")
        self.assertEqual(self.converter.to_title_case(""), "")
        self.assertEqual(self.converter.to_title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_to_camel_case(self):
        self.assertEqual(self.converter.to_camel_case("hello world"), "helloWorld")
        self.assertEqual(self.converter.to_camel_case("Hello World"), "helloWorld")
        self.assertEqual(self.converter.to_camel_case("hello-world"), "helloWorld")
        self.assertEqual(self.converter.to_camel_case("hello_world"), "helloWorld")
        self.assertEqual(self.converter.to_camel_case("the quick brown fox"), "theQuickBrownFox")
        self.assertEqual(self.converter.to_camel_case(""), "")
        self.assertEqual(self.converter.to_camel_case("hello"), "hello")
        self.assertEqual(self.converter.to_camel_case("HTML parser"), "htmlParser")

    def test_to_pascal_case(self):
        self.assertEqual(self.converter.to_pascal_case("hello world"), "HelloWorld")
        self.assertEqual(self.converter.to_pascal_case("Hello World"), "HelloWorld")
        self.assertEqual(self.converter.to_pascal_case("hello-world"), "HelloWorld")
        self.assertEqual(self.converter.to_pascal_case("hello_world"), "HelloWorld")
        self.assertEqual(self.converter.to_pascal_case("the quick brown fox"), "TheQuickBrownFox")
        self.assertEqual(self.converter.to_pascal_case(""), "")
        self.assertEqual(self.converter.to_pascal_case("hello"), "Hello")
        self.assertEqual(self.converter.to_pascal_case("HTML parser"), "HtmlParser")

    def test_to_snake_case(self):
        self.assertEqual(self.converter.to_snake_case("hello world"), "hello_world")
        self.assertEqual(self.converter.to_snake_case("Hello World"), "hello_world")
        self.assertEqual(self.converter.to_snake_case("helloWorld"), "hello_world")
        self.assertEqual(self.converter.to_snake_case("HelloWorld"), "hello_world")
        self.assertEqual(self.converter.to_snake_case("hello-world"), "hello_world")
        self.assertEqual(self.converter.to_snake_case("the quick brown fox"), "the_quick_brown_fox")
        self.assertEqual(self.converter.to_snake_case(""), "")
        self.assertEqual(self.converter.to_snake_case("hello"), "hello")
        self.assertEqual(self.converter.to_snake_case("XMLHttpRequest"), "xml_http_request")

    def test_to_kebab_case(self):
        self.assertEqual(self.converter.to_kebab_case("hello world"), "hello-world")
        self.assertEqual(self.converter.to_kebab_case("Hello World"), "hello-world")
        self.assertEqual(self.converter.to_kebab_case("helloWorld"), "hello-world")
        self.assertEqual(self.converter.to_kebab_case("HelloWorld"), "hello-world")
        self.assertEqual(self.converter.to_kebab_case("hello_world"), "hello-world")
        self.assertEqual(self.converter.to_kebab_case("the quick brown fox"), "the-quick-brown-fox")
        self.assertEqual(self.converter.to_kebab_case(""), "")
        self.assertEqual(self.converter.to_kebab_case("hello"), "hello")
        self.assertEqual(self.converter.to_kebab_case("XMLHttpRequest"), "xml-http-request")

    def test_to_alternating_case(self):
        self.assertEqual(self.converter.to_alternating_case("hello"), "hElLo")
        self.assertEqual(self.converter.to_alternating_case("hello world"), "hElLo WoRlD")
        self.assertEqual(self.converter.to_alternating_case("HELLO"), "hElLo")
        self.assertEqual(self.converter.to_alternating_case(""), "")
        self.assertEqual(self.converter.to_alternating_case("a"), "a")
        self.assertEqual(self.converter.to_alternating_case("ab"), "aB")
        self.assertEqual(self.converter.to_alternating_case("123abc"), "123aBc")
        self.assertEqual(self.converter.to_alternating_case("hello-world"), "hElLo-WoRlD")

    def test_to_sentence_case(self):
        self.assertEqual(self.converter.to_sentence_case("hello world"), "Hello world")
        self.assertEqual(self.converter.to_sentence_case("HELLO WORLD"), "Hello world")
        self.assertEqual(self.converter.to_sentence_case("hELLO wORLD"), "Hello world")
        self.assertEqual(self.converter.to_sentence_case(""), "")
        self.assertEqual(self.converter.to_sentence_case("a"), "A")
        self.assertEqual(self.converter.to_sentence_case("the quick brown fox jumps"), "The quick brown fox jumps")

    def test_edge_cases(self):
        # Test with special characters
        self.assertEqual(self.converter.to_snake_case("hello@world#test"), "hello_world_test")
        self.assertEqual(self.converter.to_kebab_case("hello@world#test"), "hello-world-test")
        
        # Test with numbers
        self.assertEqual(self.converter.to_camel_case("hello2world"), "hello2World")
        self.assertEqual(self.converter.to_pascal_case("hello2world"), "Hello2World")
        
        # Test with single character
        self.assertEqual(self.converter.to_camel_case("a"), "a")
        self.assertEqual(self.converter.to_pascal_case("a"), "A")
        
        # Test with multiple spaces/separators
        self.assertEqual(self.converter.to_snake_case("hello   world"), "hello_world")
        self.assertEqual(self.converter.to_kebab_case("hello---world"), "hello-world")

if __name__ == '__main__':
    unittest.main()