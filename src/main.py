from textnode import TextNode, TextType
from htmlnode import LeafNode
import node_split

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

def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    node_list = node_split.split_nodes_delimited([node], "**", TextType.BOLD)
    node_list = node_list[:-1] + node_split.split_nodes_delimited([node_list[-1]], "*", TextType.ITALIC)
    node_list = node_list[:-1] + node_split.split_nodes_delimited([node_list[-1]], "`", TextType.CODE)
    node_list = node_list[:-1] + node_split.split_nodes_image([node_list[-1]])
    node_list = node_list[:-1] + node_split.split_nodes_link([node_list[-1]])

    return node_list


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))


if __name__ == "__main__":
    main()