import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leaf_node_with_tag_value_and_props(self):
        node = LeafNode(
            "a", "Click me!", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Click me!</a>',
        )

    def test_leaf_node_with_no_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leaf_node_with_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)


if __name__ == "__main__":
    unittest.main()
