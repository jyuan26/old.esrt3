import os
directory = os.fsencode('/Users/jasonyuan/ESRT/dataset/valx2')
count = 1
for file in os.listdir(directory):
    print(count)
    count += 1
    filename = os.fsdecode(file)
    newfilename = filename[:-4]
    newfilename = '/Users/jasonyuan/ESRT/dataset/valx2/' + newfilename + 'x2.npy'
    name = '/Users/jasonyuan/ESRT/dataset/valx2/' + filename
    os.rename(name, newfilename)
    print(name, 'renamed to', newfilename)
