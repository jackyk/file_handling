from PIL import Image
import shutil,os
from abc import ABCMeta, abstractmethod
import csv

with open("files/CSV/us-500.csv", "rb") as f:
# f = open("files/CSV/data.csv", "rb")
    reader = csv.reader(f)
    for row in reader:
        print "-".join(row)

# Reading inside a test file
# **************************************************************************
# with open("files/TEXT/NOTICE.txt", "r") as read_file:
# read_file = open("files/TEXT/copying.txt", "r")
# test = read_file.readlines()
# # test = read_file
# # print len(test)
#
# new_line = []
# for i in test:
#     test1 = i.split()
#     new_line.append(test1)
# single_list = new_line[:5]
# # print single_list
# for c in single_list:
#     print " ".join(c)
#     print "***************"
# read_file.close()
# ********************************************************************
# Checking inside a .csv and printing its columns
