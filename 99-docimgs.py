import os
from urllib.parse import quote
urlroot = 'https://raw.githubusercontent.com/mutazag/godzilla-sina/master/docimgs/'


root = 'docimgs'
filepaths = [os.path.join(root, f) for f in os.listdir(root)]
# [os.path.basename(f) for f in os.listdir(root)]
datasets = [os.path.splitext(f)[0] for f in os.listdir(root)]

imgs = [os.path.splitext(f)[0] + ',' + (urlroot + quote(f)) for f in os.listdir(root)]


for img in imgs:
    print(img)
