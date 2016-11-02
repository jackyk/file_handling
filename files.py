# import files
from PIL import Image
import shutil, os
# # class Files:
#
#     # def csv_files(self):
# os.mkdir("files/PNG")
# for file in os.listdir("files"):
#     src = "files/"
#     if file.endswith(".png"):
#         nsrc = src + file
#         shutil.move(nsrc, "files/PNG")
#         # print file
# os.mkdir("files/Keem")
# os.system("mkdir Test")

# # check_file = Files()
# images_1 = []
for image in os.listdir("files/PNG"):
#     #  images_1.append(image)
    # print image
    # x = image
    # print x
    images_2=Image.open("files/PNG/", image  )
    print images_2.size

        #  print width and height(images_1[0])
# images_2 = Image.open("files/PNG")
