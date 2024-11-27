import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            value="Google",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="p", value="Hello, World!")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="div", value="Sample Text", props={"class": "container"})
        self.assertEqual(
            repr(node),
            "HTMLNode(tag='div', value='Sample Text', children=[], props={'class': 'container'})",
        )


if __name__ == "__main__":
    unittest.main()