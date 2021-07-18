import os

def talk(text):
    os.popen('./mimic -t "' + text + '" -voice slt')
