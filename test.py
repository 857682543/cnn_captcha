import os
import re


filename_list = os.listdir("./sample/test/")
count = 0
for filename in filename_list:
    # if filename == ".DS_Store":
    #     print(filename)
    #     os.remove("./sample/test/" + filename)

#     # char = filename.split("_")[0]
#     # print(char)
#     # if re.search(r"\d+", char):
#     #     print(char, filename)
#     #     print()
#
    char_count = len(filename.split("_")[0])
    if char_count < 6:
        count += 1
        print(count)
        print(filename)


