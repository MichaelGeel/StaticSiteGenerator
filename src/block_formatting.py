from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from node_split import split_nodes_delimited, split_nodes_image, split_nodes_link

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    formatted_blocks = []
    for block in markdown_blocks:
        formatted_block = block
        if formatted_block == "":
            continue
        if formatted_block[0] == "\n":
            formatted_block = formatted_block[1:]
        formatted_block = f"{formatted_block[0:2]}{formatted_block[2:].strip()}"
        formatted_blocks.append(formatted_block)

    return formatted_blocks

def block_to_block_type(markdown_block):
    # Heading check:
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    if markdown_block[:markdown_block.find(" ")+1] in headings:
        return "heading"
    elif markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return "code"
    if markdown_block[0] == ">":
        block_test = markdown_block.split("\n")
        is_quote = True
        for block in block_test:
            if block[0] != ">":
                is_quote = False
                break
        if is_quote:
            return "quote"
    ul_starts = ["* ", "- "]
    if markdown_block[:2] in ul_starts:
        block_test = markdown_block.split("\n")
        is_ul = True
        for line in block_test:
            if line[:2] not in ul_starts:
                is_ul = False
                break
        if is_ul:
            return "unordered list"
        
    if markdown_block[:3] == "1. ":
        block_test = markdown_block.split("\n")
        is_ol = True
        ol_increment = 1
        for line in block_test:
            if line[:3] == f"{ol_increment}. ":
                ol_increment += 1
            else:
                is_ol = False
                break
        if is_ol:
            return "ordered list"
    return "normal"