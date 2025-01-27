from enum import Enum
from functools import reduce

class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            return reduce(lambda x, y: f'{x} {y}="{self.props[y]}"', self.props, "")
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        elif self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag was provided")
        if self.children == None or self.children == []:
            raise ValueError("No children were provided")
        html_strings = []
        for child in self.children:
            html_strings.append(child.to_html())
        html_string = f"<{self.tag}{self.props_to_html()}>{''.join(html_strings)}</{self.tag}>"
        return html_string
        
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
