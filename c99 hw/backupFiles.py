import os
import shutil

source =  input ("Enter source folder name : ")
destination = input ("enter destination folder name : ")
source = source + '/'

destination = destination + '/'

listOfFiles = os.listdir (source)