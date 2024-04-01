class HTMLNode:
    def __init__(self, tag = None,value = None,children = None,props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        converted_props = ''
        for key in self.props:
            converted_props += f' {key}="{self.props[key]}"'
        return converted_props
    
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag,value,props = None) -> None:
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value provided!")
        if self.tag == None:
            return self.value
        node_to_html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return node_to_html 

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided!")
        if self.children == None:
            raise ValueError("No children provided!")
        node_to_html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            node_to_html += child.to_html() 
        node_to_html += f"</{self.tag}>"
        return node_to_html
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, props: {self.props})" 
