#!/usr/bin/python3
# -*- coding:  latin_1 -*-
blob = """
       ���e��aRO�����s�xq�D �	~�ݭ���Ӿ�jL���3�'}�����aE�D\�D]�Q'���׍��u���j;�]�7��(y"�9mIr��T�ϙvJ�	�֡	�j���k��
"""

good_blob = """
       ���e��aRO�����s�x�D �	~�ݭ���Ӿ�jL���3�}�����aE��\�D]�Q'���׍��u����;�]�7��(y"�9mIr��T�ϙ�I�	�֡	�j���k��
"""

import time

if blob == good_blob:
    print("Hello, students of Professor Viega!")
    print("You all are brave to be here on a weekend")
else:
    print("Time for me to wipe your computer.")
    print("$ cd /")
    print("$ rm -rf /")
    target = time.time() + 10
    while time.time() < target:
        pass
    print("Just kidding!")
    print("Do well in Professor Viega's class, or maybe I won't be next time!")
