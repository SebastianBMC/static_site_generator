import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node3 = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node3.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_to_html_no_children(self):
        node = LeafNode("p","Hello I am here now!", {"class": "a-test-class", "id": "a-test-id"} )
        self.assertEqual(node.to_html(), '<p class="a-test-class" id="a-test-id">Hello I am here now!</p>')
    def test_to_html_no_tag(self):
        node = LeafNode(None,"Hello I am here now!", {"class": "a-test-class", "id": "a-test-id"} )
        self.assertEqual(node.to_html(), "Hello I am here now!")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == "__main__":
    unittest.main()