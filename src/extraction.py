import re

def extract_markdown_images(text):
    raw_images = re.findall(r"\!\[.*?\]\(.*?\)", text)
    images = [
        (re.findall(r"\[(.*?)\]", image)[0], re.findall(r"\((.*?)\)", image)[0]) for image in raw_images
    ]
    return images

def extract_markdown_links(text):
    raw_links = re.findall(r"[^!]\[.*?\]\(.*?\)", text)
    links = [
        (re.findall(r"\[(.*?)\]", link)[0], re.findall(r"\((.*?)\)", link)[0]) for link in raw_links
    ]
    return links

def extract_title(markdown):
    md_lines = markdown.split("\n")
    for line in md_lines:
        if line[:2] == "# ":
            return line[2:]
    raise BaseException("no title in file")