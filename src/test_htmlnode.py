import unittest

from htmlnode import (HTMLNode,LeafNode,ParentNode)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}) 
        self.assertEqual(' href="https://www.google.com" target="_blank"',node.props_to_html())
    def test_props_to_html2(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "alt": "this is a alt text"}) 
        self.assertEqual(' href="https://www.google.com" target="_blank" alt="this is a alt text"',node.props_to_html())
    def test_repl(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}) 
        self.assertEqual("HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))
    def test_parent_leaf(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())
    def test_nested_parent_props(self):
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Inner text bold"),
                LeafNode(None, "Inner Normal text"),
            ],
        ) 

        node = ParentNode(
            "input",
            [
                node2,
                LeafNode("b", "Bold text"),
            ],
            {
                "type": "text"
            }
        )
        self.assertEqual('<input type="text"><p><b>Inner text bold</b>Inner Normal text</p><b>Bold text</b></input>',node.to_html())

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("<p>This is a paragraph of text.</p>", node1.to_html())
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node2.to_html())
    



if __name__ == '__main__':
    unittest.main()
