from PIL import Image
import os
filename = input()
img = Image.open(filename)
newfilename = filename.replace('.png', '.ico')
img.save(newfilename)
newfile = open(newfilename)