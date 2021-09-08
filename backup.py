import os 
import shutil

source= input(" Enter the Path that you want to create backup for: ")
destination_path= input("Enter the path where you want to deliver the folder: ")

source= source + '/'
destination_path= destination_path + '/'

list_of_files= os.listdir(source)

for file in list_of_files:
    shutil.copy((source + file), destination_path)
    