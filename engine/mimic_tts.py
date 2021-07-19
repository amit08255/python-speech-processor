import os

def talk(text):
    path = os.path.join(os.path.dirname(".."), 'mimic')
    os.popen('./' + path +  ' -t "' + text + '" -voice slt')
