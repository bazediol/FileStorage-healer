import os, shutil, re

def initialization ():
    path = os.getcwd() + "\\FileStorage"
    if not os.path.exists(path):
        os.mkdir ('FileStorage')
    else:
        if  os.listdir('FileStorage'):
            for the_file in os.listdir('FileStorage'):
                file_path = os.path.join('FileStorage', the_file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)


def creator (list):
    for folder, file in list:
        file_path = os.path.join ('FileStorage', folder)
        os.mkdir(file_path)
        open (os.path.join (file_path, file), 'x')
    
def parcer ():
    file = open ('logs.txt', 'r')
    pattern = "FileStorage checking result\. File .*FileStorage\\\\(.{4})\\\\(.+) is"
    parced_list = re.findall (pattern, file.read())
    for dir, file_name in parced_list:
        print ("dir name: ", dir, " file: ", file_name, "\n")
    file.close()
    return parced_list
        
initialization()
creator (parcer())
