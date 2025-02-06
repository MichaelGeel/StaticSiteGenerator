from conversions import markdown_to_html_node
from text_testing import full_markdown_text
from file_copy import fresh_port
from extraction import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        md_contents = file.read()
    with open(template_path) as template:
        template_contents = template.read()
    md_html_node = markdown_to_html_node(md_contents)
    html_code = md_html_node.to_html()
    try:
        page_title = extract_title(md_contents)
    except:
        page_title = "No title given"
    template_contents = template_contents.replace("{{ Title }}", page_title)
    template_contents = template_contents.replace("{{ Content }}", html_code)
    # if not os.path.isfile(dest_path):
    #     os.mkdir(dest_path)
    #     with open(os.path.join(dest_path, "index.html"), "w") as new_file:
    #         new_file.write(template_contents)
    # else:
    with open(os.path.join(dest_path), "w") as new_file:
        new_file.write(template_contents)


def main():
    #print(markdown_to_html_node(full_markdown_text).to_html())
    fresh_port()
    generate_page("./content/index.md", "./template.html", "./public/index.html")


if __name__ == "__main__":
    main()