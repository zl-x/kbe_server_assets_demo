# -*- coding: utf-8 -*-

import os
import sys
import shutil

src_folder = "scripts_work"
dst_folder = "scripts"

def copy_folder_tree():
    if os.path.exists(dst_folder):
        if os.path.isdir(dst_folder):
            shutil.rmtree(dst_folder)
        else:
            os.remove(dst_folder)

    shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)

def dfs_dir(cur_dir):
    all_item = os.listdir(cur_dir)

    for v in all_item:
        tmp_path = cur_dir + "/" + v
        if os.path.isdir(tmp_path):
            dfs_dir(tmp_path)
            continue

        if len(v) < 3 or v[-3:] != ".py":
            continue

        change_import(tmp_path)

def change_import(file_path):
    if not os.path.isfile(file_path):
        return

    path_list = file_path.split("\/")
    if len(path_list) < 2:
        return

    
    fd = open(file_path)
    all_content = fd.read()

def get_changed_content(sec_folder_name):
    return "1", "2"

if __name__ == "__main__":
    copy_folder_tree()

    dfs_dir(dst_folder)


