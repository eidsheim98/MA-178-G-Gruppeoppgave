import os
import subprocess
import platform

def run_file(filename):
    """
    Kjører spesifisert fil hvis funnet i hierarkiet
    :param filename: Filnavnet uten .py
    :return: None
    """
    found = False
    # Se etter fila
    for path, subdirs, files in os.walk(os.getcwd() + '/matte'):
        # For hvert filnavn funnet
        for name in files:
            # Hvis filnavnet stemmer med filnavet som ble skrevet inn
            if name == filename:
                # Sett fila som funnet
                fullpath = path + '/' + name
                found = True
                break
        if found:
            break

    # Hvis fila ble funnet, kjør fila
    if found:
        print("Running " + filename + '\n')

        # Hvis man er på windows, kjør python kommando, hvis ikke kjør python3 kommando
        # Usikker på om dette fungerer i MacOS, men kjører samme kommando som Linux fordi begge er UNIX
        if 'windows' in platform.system().lower():
            subprocess.Popen(['python', fullpath])
        else:
            subprocess.Popen(['python3', fullpath])

    # Hvis fila ikke ble funnet, gi beskjed om dette
    else:
        print("Could not find " + filename + '\n')


if __name__ == '__main__':
    while True:
        filename = input("Insert file to run: ")
        run_file(filename + '.py')