import json
import zipfile
import os

api_token={"username":"sandrajustiniano","key":"58f59c905377d769601296ff49365e46"}

with open("C:/Users/Usercx/.kaggle/kaggle.json","w") as file:
    json.dump(api_token, file)

location = "C:/Users/Usercx/Documents/parcialcertus/dataset"

if not os.path.exists(location):
    os.mkdir(location)
else:
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

os.system("kaggle datasets download -d henryshan/starbucks -p C:/Users/Usercx/Documents/parcialcertus/dataset")            

os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r")
    zip_ref.extractall()
    zip_ref.close()