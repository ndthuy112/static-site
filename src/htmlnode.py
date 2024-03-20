class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if self.props is None:
            return None
        for prop in self.props:
            output = f'{output} {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props_to_html()}"