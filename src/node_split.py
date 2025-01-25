from textnode import TextNode, TextType

def split_nodes_delimited(old_nodes, delimiter, text_type):
    text_nodes = []
    for node in old_nodes:
        text_string = node.text
        while len(text_string) > 0:
            first_delim = text_string.find(delimiter)
            if first_delim == -1:
                text_nodes.append(TextNode(text_string, TextType.NORMAL))
                text_string = ""
                continue
            if first_delim > 0:
                text_nodes.append(TextNode(text_string[:first_delim], TextType.NORMAL))
            text_string = text_string[(first_delim+len(delimiter)):]
            second_delim = text_string.find(delimiter)
            text_nodes.append(TextNode(text_string[:second_delim], text_type))
            text_string = text_string[(second_delim+len(delimiter)):]
   
    return text_nodes
