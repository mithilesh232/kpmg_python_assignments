from zipfile import *
f=ZipFile("threads1.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print( "File Name: ",name)
    print("The Content of this file is:")
    f1=open(name,'r')
    print(f1.read())
    print() 