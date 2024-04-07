from genericpath import isfile
import os, shutil
from blocks import markdown_to_blocks, markdown_to_html_node, block_to_block_type

def main():
    copy_static("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


def copy_static(current, target):
    directory_list = os.listdir(current)
    for item in directory_list:
        file_path = os.path.join(current, item)
        target_path = os.path.join(target, item)
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_path)
        else:
            if os.path.exists(target_path):
                shutil.rmtree(target_path)
            os.mkdir(target_path)
            copy_static(file_path, target_path)


def extract_title(markdown:str):
    first_block = markdown_to_blocks(markdown)[0]
    if not first_block.startswith("# "):
        raise ValueError("Heading 1 needed")
    return first_block[2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    markdown_file = open(from_path)
    template_file = open(template_path)
    markdown_text = markdown_file.read()
    template_text = template_file.read()
    html_node = markdown_to_html_node(markdown_text)
    title = extract_title(markdown_text)
    template_text = template_text.replace("{{ Title }}", title).replace("{{ Content }}", html_node.to_html())
    markdown_file.close()
    template_file.close()
    html_file = open(dest_path, "w")
    html_file.write(template_text)
    html_file.close()


if __name__ == "__main__":
    main()