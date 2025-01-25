from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            converted_node = LeafNode(value=text_node.text)
        case TextType.BOLD:
            converted_node = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            converted_node = LeafNode(text_node.text, "i")
        case TextType.CODE:
            converted_node = LeafNode(text_node.text, "code")
        case TextType.LINK:
            converted_node = LeafNode(text_node.text, "a", {"href": text_node.url})
        case TextType.IMAGE:
            converted_node = LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
    
    return converted_node


def main():
    new_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(new_node)


if __name__ == "__main__":
    main()