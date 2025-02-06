from textnode import TextNode, TextType
import re
from extraction import extract_markdown_links, extract_markdown_images

def split_nodes_delimited(old_nodes, delimiter, text_type):

    text_nodes = []
    for node in old_nodes:
        text_string = node.text
        node_type = node.text_type
        while len(text_string) > 0:
            first_delim = text_string.find(delimiter)
            if first_delim == -1:
                text_nodes.append(TextNode(text_string, node_type))
                text_string = ""
                continue
            if first_delim > 0:
                text_nodes.append(TextNode(text_string[:first_delim], TextType.NORMAL))
            text_string = text_string[(first_delim+len(delimiter)):]
            second_delim = text_string.find(delimiter)
            text_nodes.append(TextNode(text_string[:second_delim], text_type))
            text_string = text_string[(second_delim+len(delimiter)):]
   
    return text_nodes


def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            node_text = node.text
            raw_images = re.findall(r"\!\[.*?\]\(.*?\)", node_text)
            for raw_image in raw_images:
                img_pos = node_text.find(raw_image)
                if img_pos != 0:
                    nodes.append(TextNode(node_text[:img_pos], TextType.NORMAL))
                processed_img = (re.findall(r"\[(.*?)\]", raw_image)[0], re.findall(r"\((.*?)\)", raw_image)[0])
                nodes.append(TextNode(processed_img[0], TextType.IMAGE, processed_img[1]))
                node_text = node_text[img_pos+len(raw_image):]
            if len(node_text) > 0:
                nodes.append(TextNode(node_text, TextType.NORMAL))
        else:
            nodes.append(node)
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            node_text = node.text
            raw_links = re.findall(r"\[.*?\]\(.*?\)", node_text)
            for raw_link in raw_links:
                link_pos = node_text.find(raw_link)
                if link_pos != 0:
                    nodes.append(TextNode(node_text[:link_pos], TextType.NORMAL))
                processed_link = (re.findall(r"\[(.*?)\]", raw_link)[0], re.findall(r"\((.*?)\)", raw_link)[0])
                nodes.append(TextNode(processed_link[0], TextType.LINK, processed_link[1]))
                node_text = node_text[link_pos+len(raw_link):]
            if len(node_text) > 0:
                nodes.append(TextNode(node_text, TextType.NORMAL))
        else:
            nodes.append(node)
    return nodes