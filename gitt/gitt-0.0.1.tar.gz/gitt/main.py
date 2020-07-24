import requests
import os
from getpass import getpass
from termcolor import colored
import random
import string
import argparse
import json
import copy


BASE_URL = "https://github-clone-dj.herokuapp.com/api" # "https://github-clone-dj.herokuapp.com/api"

def clone(username=None, repo=None):
    downloadable_urls = {}

    if username == None and repo == None:
        username = input("Your GitHub Clone username here: (if you don't have one, first, click control-c, then, go to https://https://github-clone-dj.herokuapp.com/auth/register/ to register for an account): ")
        repo = input("Your Repository to clone: ")

        r = requests.get(f"{BASE_URL}/repo/?username={username}&repo={repo}")

        find_data = True
        try:
            r = r.json()
        except:
            find_data = False
            print(colored("Oops, your information is not correct, please try again.", "red", attrs=['bold']))

    if find_data:
        print(colored("We are cloning to current directory, this may take 0.5-5 minutes, depends on size and amount of file you have.", "yellow"))

        pathname = ""

        for key, val in r["directories"].items():

            index = False

            if val[0] != 0:
                pathname = val[2]
                pathname = pathname[:-1]
                pathname = pathname[1:]
                try:
                    os.mkdir(pathname)
                except FileExistsError:
                    pass

            for f in r["files"]:
                if str(f[3]) == str(key):
                        data = requests.get(f[2]).text
                        downloadable_urls[f"{pathname}/{f[1]}"] = f[2]
                        if len(pathname) == 0:
                            with open(f"{f[1]}", "w") as f:
                                f.write(data)
                            f.close()
                        else:
                            with open(f"{pathname}/{f[1]}", "w") as f:
                                f.write(data)
                            f.close()

        try:
            os.mkdir(".git-clone-dj")
        except FileExistsError:
            pass
        with open(f".git-clone-dj/info.txt", "w") as f:
            f.writelines("DON'T EDIT THIS FILE!\n")
            f.writelines(f"{username}/{repo}")
        f.close()
        with open(".git-clone-dj/struct.txt", "w") as f:
            dirs = set()
            data = {"struct": [], "downloadable_urls": downloadable_urls}
            for path, subdirs, files in os.walk("./"):
                if path.split(".")[1] == "/":
                    dirs.add(path.split(".")[1])
                else:
                    dirs.add(path.split(".")[1] + "/")
                for name in files:
                    data["struct"].append(os.path.join(path, name))
            data["dirs"] = list(dirs)
            f.write(str(data))
    print(colored("Your repository is cloned successfully!", "green"))

def random_str(digit=30):
    str = ""
    for i in range(digit):
        str += random.choice(string.ascii_letters)
    return str

def commit():
    global repo
    global username
    with open(".git-clone-dj/info.txt") as f:
        f = f.read().splitlines(1)
        username = f[1].split("/")[0]
        repo = f[1].split("/")[1]

    print(colored(f"WARNING: Commit in progress, it will commit to: {username}/{repo}. Please don't click quit when you are commiting, it will cause an error to your repo. Rather, wait until it's finished, and then do what you need to do", "yellow"))

    global struct
    with open(".git-clone-dj/struct.txt", "r") as f:
        struct = f.read()
        struct = struct.replace("\'", "\"")
        struct = json.loads(struct)
    f.close()

    dirs = set()
    for path, subdirs, files in os.walk("./"):
        if path.split(".")[1] == "/":
            dirs.add(path.split(".")[1])
        else:
            dirs.add(path.split(".")[1] + "/")
    s_dir = struct["dirs"]

    dirs = list(dirs)
    struct3 = copy.deepcopy(struct)

    for i in dirs:
        if i in s_dir:
            s_dir.remove(i)
        else:
            # create dir
            requests.post(f"{BASE_URL}/create-directory/", data={
                "directory": i,
                "repo": repo,
                "username": username
            })
            struct3["dirs"].append(i)
            with open(".git-clone-dj/struct.txt", "w") as f:
                f.write(str(struct3))
            f.close()
            print(colored(f"create this dir: {i}", "green"))

    if len(s_dir) != 0:
        for i in s_dir:
            requests.post(BASE_URL + "/delete-directory/", data={
                "username": username,
                "repo": repo,
                "path": i
            })
            struct3["dirs"].remove(i)
            with open(".git-clone-dj/struct.txt", "w") as f:
                f.write(str(struct3))
            f.close()
            print(colored(f"delete this dir: {i}", "red"))
        # pass # delete all directories in this list

    struct2 = struct["struct"][:]
    for path, subdirs, files in os.walk("./"):
        for name in files:
            if os.path.join(path, name) in struct["struct"]:
                struct2.remove(os.path.join(path, name))
                if os.path.join(path, name) == "./.DS_Store" or os.path.join(path, name) == "./main.py" or path == "./.git-clone-dj":
                    continue
                with open(os.path.join(path, name), encoding="ISO-8859-1") as f:
                    try:
                        r = requests.get(struct["downloadable_urls"]["/" + os.path.join(path, name).split("./")[1]])
                    except KeyError:
                        r = requests.get(struct["downloadable_urls"][os.path.join(path, name).split("./")[1]])
                    if r.text == f.read():
                        f.close()
                        continue
                f.close()
            # modify file
            rs = random_str()
            try:
                ext = rs + "." + name.split(".")[1]
            except:
                ext = rs + "." + name
            with open(os.path.join(path, name), encoding="ISO-8859-1") as f:
                r = requests.post("https://github-clone-cdn.glitch.me/uploader", headers={
                    'enctype': 'multipart/form-data'
                }, data={
                    "filename": rs + "." + ext
                }, files={
                    "file": f
                })
            filename = os.path.join(path, name)[1:len(os.path.join(path, name))]
            if os.path.join(path, name) in struct3["struct"]:
                # if modified a file
                if filename.count("/") == 1:
                    directory = "/"
                    filename = filename.split("/")[1]
                else:
                    directory = "/"
                    f = filename.split("/")
                    for i in range(1, len(f)-1):
                        directory += f[i]
                    directory += "/"
                    filename = len(f)-1
                print(colored(f"Modified, {os.path.join(path, name)[1:len(os.path.join(path, name))]}", "yellow"))
                requests.post(BASE_URL + "/modify-file/", data={
                    "username": username,
                    "repo": repo,
                    "path": path,
                    "filename": filename,
                    "url": f"https://github-clone-cdn.glitch.me/uploads/{rs}.{ext}"
                })
                struct3["downloadable_urls"][os.path.join(path, name)[1:len(os.path.join(path, name))]] = f"https://github-clone-cdn.glitch.me/uploads/{rs}.{ext}"
                with open(".git-clone-dj/struct.txt", "w") as f:
                    f.write(str(struct3))
                f.close()
            else:
                # if created a new file
                print(colored(f"create new file, {os.path.join(path, name)[1:len(os.path.join(path, name))]}", "green"))
                filename = os.path.join(path, name)[1:len(os.path.join(path, name))]
                if filename.count("/") == 1:
                    filename = filename.split("/")
                    f = filename[1]
                    dir_path = "/"
                else:
                    filename = filename.split("/")
                    dir_path = "/"
                    for i in range(1, len(filename)-1):
                        dir_path += filename[i] + "/"
                    dir_path += "/"
                    f = filename[len(filename)-1]
                requests.post(BASE_URL + "/add-file/", data={
                    "username": username,
                    "repo": repo,
                    "path": dir_path,
                    "filename": f,
                    "url": f"https://github-clone-cdn.glitch.me/uploads/{rs}.{ext}"
                })
                struct3["struct"].append(os.path.join(path, name))
                filename = os.path.join(path, name)[1:len(os.path.join(path, name))]
                if filename.count("/") == 1:
                    struct3["downloadable_urls"][filename] = f"https://github-clone-cdn.glitch.me/uploads/{rs}.{ext}"
                else:
                    struct3["downloadable_urls"][filename[1:len(filename)]] = f"https://github-clone-cdn.glitch.me/uploads/{rs}.{ext}"
                with open(".git-clone-dj/struct.txt", "w") as f:
                    f.write(str(struct3))
                f.close()

    if len(struct2) != 0:
        for i in struct2:
            file = i[1:len(i)]
            filename = i[1:len(i)]
            if filename.count("/") == 1:
                filename = filename.split("/")
                f = filename[1]
                dir_path = "/"
            else:
                filename = filename.split("/")
                dir_path = "/"
                for i in range(1, len(filename)-1):
                    dir_path += filename[i] + "/"
                f = filename[len(filename)-1]
            requests.post(BASE_URL + "/delete-file/", data={
                "username": username,
                "repo": repo,
                "path": dir_path,
                "filename": f
            })
            print(colored(f"delete this file: {file}", "red"))
            struct3["struct"].remove("." + file)
            if filename.count("/") == 1:
                struct3["downloadable_urls"].pop(file)
            else:
                struct3["downloadable_urls"].pop("." + file[1:len(file)])
            with open(".git-clone-dj/struct.txt", "w") as f:
                f.write(str(struct3))
            f.close()
        # delete all the file within this list
        # pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command you want to use: clone or commit")
    args = parser.parse_args()
    if args.command == "clone":
        clone()
    elif args.command == "commit":
        commit()

if __name__ == "__main__":
    main()
