from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import ParentNode, LeafNode

def main():


    node3 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    node3.to_html()


    #print(node.__eq__(node2))
    


main()

