import os
import shutil

def fresh_port(src_path='./static'):
    dest_path = src_path.replace("static", "public")
    if src_path == "./static" and os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        os.mkdir(dest_path)
    for path in os.listdir(src_path):
        full_src_path = os.path.join(src_path, path)
        full_dest_path = os.path.join(dest_path, path)
        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path, full_dest_path)
        else:
            if not os.path.exists(full_dest_path):
                os.mkdir(full_dest_path)
            fresh_port(src_path=full_src_path)