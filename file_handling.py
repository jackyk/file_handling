from PIL import Image
import shutil,os
from abc import ABCMeta, abstractmethod

class CheckCSV:
    class OSError(File Exists):
        pass

class Files(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def test():
        pass
class FileSpecification(files):

    try:
        os.mkdir("files/CSV")
        def csv_files(self):
            storage = "files/"
            for files_1 in os.listdir("files"):
                if files_1.endswith(".csv"):
                    new_storage = storage + files_1
            shutil.move(new_storage, "files_1/CSV")
    except:

moving = Files()
moving.csv_files()
