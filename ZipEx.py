from zipfile import *
f=ZipFile("threads2.zip",'w',ZIP_DEFLATED)
f.write("thread1.py")
f.write("thread2.py")
f.write("thread3.py")
f.write("thread4.py")
f.close()
print("files.zip file created successfully") 