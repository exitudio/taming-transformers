import glob
with open('customdata/train.txt', 'w') as f:
    paths = glob.glob("/home/epinyoan/git/MaskGIT-pytorch/ImageMask/data/*")
    f.writelines('\n'.join(paths))