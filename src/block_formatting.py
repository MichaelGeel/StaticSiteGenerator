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
text = """#   This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item"""

print(markdown_to_blocks(text))