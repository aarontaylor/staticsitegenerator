import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_default_url(self):
        # Test equality with default URL (None)
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_different_text(self):
        # Test inequality when text property is different
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_with_different_text_type(self):
        # Test inequality when text_type property is different
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        # Test equality when URLs are provided and equal
        node1 = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_with_different_url(self):
        # Test inequality when URLs are different
        node1 = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINKS, "https://different.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()