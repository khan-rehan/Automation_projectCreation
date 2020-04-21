import sys
import os
from github import Github

path = "/Users/your-Homedirectory/Downloads/Projects/"

username = "" # Your github username
password = "" # Your github password


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))


if __name__ == "__main__":
    create()
