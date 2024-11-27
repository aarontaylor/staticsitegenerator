from textnode import TextNode, TextType

def main():
    # Create a TextNode object
    text_node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")

    # Print the TextNode object
    print(text_node)

if __name__ == "__main__":
    main()
