import os

def list_file():
    directory_name = input("milline kausta sul on vajalik")
    fileList = os.listdir(directory_name)
    for elem in fileList:
        print(elem)
    
def makeDirectory():
    directory_name = input("milline kausta sul on vajalik?")
    os.mkdir(directory_name)
    print("kaust" ,directory_name, "oli edukalt tehtud")
    return directory_name

def deleteFolder(folder):
    directory_name = input("milline kausta sul on vajalik?")
    os.rmdir(directory_name)
    print(f"kaust {directory_name } oli edukalt tehtud")






def chose_command(userInput):
    if userInput == "ls":
        return list_file
    elif userInput == "mkdir":
        return makeDirectory
    elif userInput == "rm":
        return deleteFolder
    else:
        return None



cmd = input("PS C:\\Users\\opilane>")
command = chose_command(cmd)

if command:
    command()
else:
    print("tundmatu käsk")

# makeDirectory()
# 
# result = makeDirectory()
# deleteFolder(result)