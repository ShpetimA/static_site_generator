import os
import shutil
from copy_static import copy_dir_conent 
from generate_html_markdown import (extract_title,generate_pages_recursive)

public_path = './public'
static_path = './static'
template_path = './template.html'
content_path = './content'

def main():
    if os.path.exists(public_path):
        shutil.rmtree('./public')
    markdown = '''# Hello there i am a header
    and i am another line in here please be kind  
    '''

    extract_title(markdown)
    copy_dir_conent(static_path, public_path)
    generate_pages_recursive(content_path,template_path, public_path)



main()

