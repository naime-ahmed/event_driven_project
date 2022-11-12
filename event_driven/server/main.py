""" 
project name: zip file handling
project type: event driven
purpose: Assignment
Author Name: Naime Molla
time spent: 4 hour

"""
import glob
import shutil
import os
import sys

# create tmp dir at exe time for doing zip operation
isExist = os.path.exists("./tmp")
if not isExist:
    os.mkdir("tmp")
source_path = "../source/*"
destination_path = "../destination"
tmp_dir = "./tmp"
z = "../destination.zip"
postfix = [1, 2, 3]

while True:
    source_obj = glob.glob(source_path)
    file_content = []

    if len(source_obj) > 0:
        object_path = source_obj[0]
        with open(object_path, "r") as file:
            file_content = file.readlines()

        shutil.copy(object_path, ".")

        object_name = object_path.split("/")[-1].split(".")
        prefix = object_name[0]
        postfix2 = object_name[1]

        # If file is a python file
        if postfix2 == "py":
            try:
                exec(open(object_path).read())
            except:
                print("Oops!", sys.exc_info()[0], "occurred")
                os.remove(object_path)
                os.remove(object_path.split("/")[-1])
            else:
                os.remove(object_path)
                os.remove(object_path.split("/")[-1])

        elif postfix2 == "txt":  # if file is a txt file
            count = 1
            for item in range(len(postfix)):
                filename = prefix + "_" + str(item + 1) + "." + postfix2

                with open(f"{tmp_dir}/{filename}", "w") as tmp_file:
                    for i in range(10 * count):
                        tmp_file.writelines(file_content[i])
                    count += 1

            shutil.make_archive("hidden_content", "zip", tmp_dir)
            print()
            print("File zipped and sended to destination")
            print()

            shutil.copy("./hidden_content.zip", destination_path)

            shutil.unpack_archive(
                f"{destination_path}/hidden_content.zip", destination_path, "zip"
            )
            os.remove("./hidden_content.zip")
            os.remove(f"{destination_path}/hidden_content.zip")
            print()
            print("unzipped them successfully!")
            print()
            os.remove(object_path)
            os.remove(object_path.split("/")[-1])

            tmp_content = glob.glob(f"{tmp_dir}/*")
            for tmp_file in tmp_content:
                os.remove(tmp_file)

        else:
            # if file formate is not .py or .txt
            print()
            print("Unsupported file")
            os.remove(object_path)
            os.remove(object_path.split("/")[-1])
            print()
