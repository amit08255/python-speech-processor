import os

def play(filename):
    os.popen('mpg123 ' + filename)
