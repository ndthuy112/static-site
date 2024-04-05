class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for prop in self.props:
            output = f'{output} {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        return f"# Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props_to_html()} #"

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("HTML tag required")
        if self.children is None:
            raise ValueError("No children in parent node")
        output = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        return output
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required in Leaf Node")
        if self.tag is None:
            return self.value
        starting_tag = f"<{self.tag}{self.props_to_html()}>"
        ending_tag = f"</{self.tag}>"
        return f"{starting_tag}{self.value}{ending_tag}"
        