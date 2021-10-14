import os
import subprocess
import threading


def run_file(filename):
    found = False
    for path, subdirs, files in os.walk(os.getcwd() + '/matte'):
        for name in files:
            if name == filename:
                fullpath = path + '/' + name
                found = True
                break
        if found:
            break

    if found:
        print("Running " + filename + '\n')
        #os.system('start /wait cmd /k python ' + fullpath)
        subprocess.Popen(['python', fullpath])
    else:
        print("Could not find " + filename + '\n')


if __name__ == '__main__':
    while True:
        filename = input("Insert file to run: ")
        run_file(filename + '.py')