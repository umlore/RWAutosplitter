from PIL import Image
from pathlib import Path
import sys
import os

#TODO: find a better way to diff an image other than a per-pixel operation!  Per-pixel takes 2s per comparison on full resolution
#TODO: figure out how to take screenshots of a specific application window, and also how to choose that window
#TODO: draw the rest of the autosplitter

def rgbdif(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])

#create the difference between two images
def imgdif(im1, im2):
    assert (im1.size == im2.size)
    imgdif = Image.new('RGB', (1920, 1080))

    pixel1 = im1.load()
    pixel2 = im2.load()
    pixeldif = imgdif.load()

    for i in range(0, im1.size[0]):
        for j in range(0, im1.size[1]):
            pixeldif[i,j] = rgbdif(pixel1[i,j], pixel2[i,j])

    imgdif.save('images\\testdif.jpg')

#get path to the application folder (RWAutosplit)
path = os.path.dirname(sys.path[0])

im1 = Image.open(path + '\\images\\test1.jpg')
im2 = Image.open(path + '\\images\\test2.jpg')

pix1 = im1.load()

imgdif(im1, im2)
