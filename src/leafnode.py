from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.tag is None:
            return self.value  # Return raw text if no tag
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
