# from abc import ABCMeta, abstactmethod
from PIL import Image
import shutil, os
from abc import ABCMeta, abstractmethod

class FileHandling(object):
    __metaclass__= ABCMeta

    @abstractmethod
    def create_directories():
        pass

    @abstractmethod
    def check_csv_files():
        pass

    @abstractmethod
    def check_txt_files():
        pass

    @abstractmethod
    def check_png_files():
        pass

class FileSpecification(FileHandling):
    class MakeFolder:
        "File already exists"
        pass

    # def __init__(self,):
    #
    def create_directories(self):
        super(FileSpecification, self).__init__
        try:
            folders = ["PNG","CSV","TEXT"]
            # folders= []
            location = "files/"
            for directory in folders:
                os.mkdir(os.path.join(location, directory))

            # for folders in os.listdir("files"):
            #     if folders = folders:
            #         raise FileSpecification.MakeFolder

        except:
            return "File already exists"
    #
    def check_csv_files(self):
        super(FileSpecification, self).__init__
        try:
            for file in os.listdir("files"):
                src_csv = "files/"
                if file.endswith(".csv"):
                        new_src_csv = src_csv + file
                        shutil.move(new_src_csv, "files/CSV")
        except:
            return "File already Exists"

    def check_txt_files(self):
        super(FileSpecification, self).__init__
        try:
            for file in os.listdir("files"):
                src_txt = "files/"
                if file.endswith(".txt"):
                    new_src_txt = src_txt + file
                    shutil.move(new_src_txt, "files/TEXT")
            read_file =open("files/TEXT/copying.txt", "r")
            test = read_file.readlines()
            new_line = []
            for i in test:
                lines = i.split()
                new_line.append(lines)
            line_by_line = new_line[:5]
            for c in line_by_line:
                print " ".join(c)
            read_file.close()
        except:
            return "File already Exists"

    def check_png_files(self):
        super(FileSpecification, self).__init__
        try:
            for file in os.listdir("files"):
                src_png = "files/"
                if file.endswith(".png"):
                    new_src_png = src_png + file
                    shutil.move(new_src_png, "files/PNG")
            #     with Image.open(file) in im:
            #         width, height = im.size
            # return im.size
            # print im.size


        except:
            return "File already Exists"


creatingdirs = FileSpecification()
print creatingdirs.create_directories()

print creatingdirs.check_csv_files()
print creatingdirs.check_txt_files()
print creatingdirs.check_png_files()











# class Files:

#     # def csv_files(self):
# os.mkdir("files/PNG")
#  # "files/CSV", "files/TEXT")
# for file in os.listdir("files"):
#     src = "files/"
#     # if file.endswith(".png"):
#     #     nsrc = src + file
#     #     shutil.move(nsrc, "files/PNG")
#     #     # print file
#     if file.endswith(".txt"):
#         text_files = src + file
#         shutil.move(text_files, "files/TEXT")
# # os.mkdir("files/Keem")
# # os.system("mkdir Test")


# # check_file = Files()
# images_1 = []
# for image in os.listdir("files/PNG"):
#     #  images_1.append(image)
#     print image
#     x = image
#     print x
#     images_2=Image.open("files/PNG/", image  )
#     print images_2.size
#
#          print width and height(images_1[0])
# images_2 = Image.open("files/PNG")
