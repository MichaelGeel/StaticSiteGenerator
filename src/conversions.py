from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
import node_split
from text_testing import full_markdown_text
from block_formatting import block_to_block_type, markdown_to_blocks

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

def list_items(text, list_type):
    item_list = text.split("\n")
    list_items = []
    for item in item_list:
        if list_type == "ul":
            trimmed_item = item[2:]
        else:
            trimmed_item = item[3:]
        nodes = text_to_textnodes(trimmed_item)
        if len(nodes) > 1:
            child_nodes = []
            for sub_node in nodes:
                child_nodes.append(text_node_to_html_node(sub_node))
            list_items.append(ParentNode("li", child_nodes))
        else:
            list_items.append(ParentNode("li", [text_node_to_html_node(nodes[0])]))
    return ParentNode(list_type, list_items)

def block_to_node(block_tuple):
    # (block_type, block_text)
    match block_tuple[0]:
        case "normal":
            node_list = text_to_textnodes(block_tuple[1])
            html_nodes = []
            for node in node_list:
                html_nodes.append(text_node_to_html_node(node))
            return ParentNode("p", html_nodes)
        case "heading":
            length_to_trim = len(block_tuple[1][:block_tuple[1].find(" ")])
            text = block_tuple[1][length_to_trim+1:]
            return LeafNode(text, f"h{length_to_trim}")
        case "code": # Code node on the block level.
            code_text = block_tuple[1][2:-2]
            node = text_to_textnodes(code_text)[0]
            return text_node_to_html_node(node)
        case "quote":
            text = block_tuple[1].split("\n")
            child_parent_nodes = []
            for line in text:
                nodes = text_to_textnodes(line[1:])
                if len(nodes) > 1:
                    child_nodes = []
                    for sub_node in node:
                        child_nodes.append(text_node_to_html_node(sub_node))
                    child_parent_nodes.append(ParentNode("p", child_nodes))
                else:
                    child_parent_nodes.append(text_node_to_html_node(nodes[0]))
            return ParentNode("blockquote", [child_parent_nodes])
        case "unordered list": # Create a separate function for handling the items of un/ordered lists to save on code repitition.
            return list_items(block_tuple[1], "ul")
        case "ordered list":
            return list_items(block_tuple[1], "ol")


def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    block_and_type = list(map(lambda x: (block_to_block_type(x), x), blocks_list))
    block_nodes = []
    for block in block_and_type:
        block_nodes.append(block_to_node(block))
    if block_nodes != []:
        body_node = ParentNode("body", block_nodes)
    else:
        body_node = LeafNode("", "body")
    html_node = ParentNode("html", [body_node])

    return html_node