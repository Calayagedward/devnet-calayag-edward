"""
Module 2 — Activity: File Sorting with os and shutil
Student: Calayag, Edward P.
Date: 09/23/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================

I built a script that sorts a messy file/directories in a working computer. 
It ask the user like me, to type or paste a sample path so it would check if the path/folder/files exists or not.
If the path/fodler/file exists/real, it will dispay a text "The Folder/File/Path is real!" and ask again a user to type a path/folder/file to check if it exists or not. If the path/folder/file exists, it will display the path of the folder/file. 
However, if the path/folder/file doesn't exists, it will display text "Errorrrrrr! Don't continue!" and the script/loop will stop.

============================================
KEY VOCABULARY
============================================
- os module: it entering your operating system and it can be used to manipulate files and directories locations.
- shutil module: a modules that allows you to move files/directories to another path or locations.
- file path: is text-like; where your fie is specified where it's located in your woking drive/directory.
- directory: is folder that contains files and another folders/directories.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# os.path.exists()
# os.mkdir("newdir")

# var1 = 'randomfile.zip'
# var2 = 'slides.pptx'
# var3 = 'ward.txt'
# var4 = 'oww.png'

# list_of_file = os.listdir()
# print(list_of_file)

store =input("Enter your Folder/File/Path: ")
if os.path.exists(store):
    print("The Folder/File/Path is real!")
    print("")
    print("All folders & files:", os.listdir())

    enter = input("Please enter a Path/Folder/File: ")

    path = os.path.join(os.path.join
                        ,enter)
    print(path)
else:
    print("Errorrrrrr! Don't continue!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

I've got so many mistakes while building this. I was really confused because I didn't notice the learning tool that our prof provided us, even though it's already on the screen/page we are using. 
Btw, about in te script; I was really confused about the os.path.join() function because I didn't know how to use it properly. I was really confused about the syntax of the function. 
I didn't know how to use it, and that's also one of the reason why my scipts didn't work properly. But I know for sure (not 100%) that it connects to the path/folder/file that the user typed or pasted.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

It connects to os and util modules, because it has functions that can be used to manipulate path/folder/file. 
"""

