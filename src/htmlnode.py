class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self):

        if self.props == None:
            return None

        prop_string = ""

        for value in self.props:
            prop_string += " " + value + "="
            prop_string += f'"{self.props[value]}"'

        return prop_string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)
    
    def to_html(self):
       
        if self.value is None:
            raise ValueError("There is no value dummy")
        if self.tag is None:
            return self.value
        if self.props:
            html_string=f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            return html_string

        html_string = f'<{self.tag}>{self.value}</{self.tag}>'
        return html_string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("No tag fool")
        if self.children is None:
            raise ValueError("No children, what is wrong with you")
        
        html_string = ""

        for child in self.children:
            
            html_string += child.to_html()

        full_string = f'<{self.tag}>{html_string}</{self.tag}>'
      
        return full_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"