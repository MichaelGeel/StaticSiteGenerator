from conversions import markdown_to_html_node
from text_testing import full_markdown_text


def main():
    print(markdown_to_html_node(full_markdown_text).to_html())


if __name__ == "__main__":
    main()