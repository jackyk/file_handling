from PIL import Image
import shutil,os
from abc import ABCMeta, abstractmethod

file_read = open("files/TEXT/NOTICE.txt", "r")
count = 5
# files = file_read.readlines(count)
# print files
for lines in file_read.readlines():
    # data = lines.split()
    # print data[0:count]
    print line


# for im in os.listdir("files/PNG"):
#     # my_image= Image.open(im)
#     # print im
#     if im.endswith(".png"):
#         New = list(im)
#         print New
#
# im = os.listdir("files/PNG")
# image_1 = im[0]
# print image_1.size
# #
# # for f in im:
# #     print f










#
# class Files(object):
#     __metaclass__=ABCMeta
#     #this class and function cannot be instantiated but can be overiden in the next class that is inheriting
#     @abstractmethod
#     def check_csv():
#         pass
#
# class FileSpecification(files):
#     class OSError:
#         "File already Exists"
#         pass
# # Overiding an abstactmethod
#
#     try:
#         os.mkdir("files/CSV")
#         @classmethod
#         def csv_files(self):
#             storage = "files/"
#             for files_1 in os.listdir("files"):
#                 if files_1.endswith(".csv"):
#                     new_storage = storage + files_1
#                 else:
#                     raise FileSpecification.CheckCSV
#
#             shutil.move(new_storage, "files_1/CSV")
#         def csv_columns:
#             for files_2 in os.listdir("files/CSV"):
#
#     except:
#         return "File already exists"
#
# moving = Files()
# moving.csv_files()
# # filename = "files/PNG"
# # print filename
# # for images in os.listdir(filename):
# #     # img = Image.open(images)
# #     width, height = im.size
# # # print img
# filename = "files/PNG"
# for images in filename:
#     example = Image.open(images)
#     images.show()

# size = ("width", "height")
# for my_image in os.listdir("files/PNG"):
    # i = Image.open(my_image)
    # if my_image.endswith(".png"):
        # i = Image.open(my_image)
        # fn, fext = os.path.splitext(my_image)
        # i.picture(size )
    # print my_image

# im = Image.open("/home/keem/Documents/Python/file-categories/file_handling/files/PNG")
# # im.size
# with Image.open('files/PNG') as im:
#     width,height = im.size
#     print im.size
