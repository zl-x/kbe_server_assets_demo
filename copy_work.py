# -*- coding: utf-8 -*-

import os
import sys
import shutil

src_folder = "scripts_work"
dst_folder = "scripts"

debug_change_dict = dict(
    old="from kbengine import debug\n",
    new="import KBEDebug as debug\n")

app_right_import = "import KBEngine as kbe\n"
app_change_dict = dict(
    base="import kbengine.base as kbe\n",
    bots="import kbengine.bots as kbe\n",
    cell="import kbengine.cell as kbe\n",
    db="import kbengine.db as kbe\n",
    interface="import kbengine.interface as kbe\n",
    logger="import kbengine.logger as kbe\n",
    login="import kbengine.login as kbe\n",
)


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

    path_list = file_path.split("/")
    if len(path_list) < 2:
        return

    if path_list[1] not in app_change_dict:
        return

    fd = open(file_path, encoding='UTF-8')
    all_lines = fd.readlines()
    fd.close()

    os.remove(file_path)

    fd = open(file_path, mode="w", encoding='UTF-8')

    for i, content in enumerate(all_lines):
        if content == debug_change_dict["old"]:
            all_lines[i] = debug_change_dict["new"]
        elif content == app_change_dict[path_list[1]]:
            all_lines[i] = app_right_import

    fd.writelines(all_lines)
    fd.close()


if __name__ == "__main__":
    copy_folder_tree()

    dfs_dir(dst_folder)
