class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        # To be implemented by child classes
        raise NotImplementedError("This method should be implemented by subclasses")

    def props_to_html(self):
        if not self.props:
            return ""
        # Generate HTML attributes as a string
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )