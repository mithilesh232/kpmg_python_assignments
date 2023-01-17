#it will create the file and write the content into file

f_demo = open("kpmg.txt", "w") 
f_demo. write("Welcome to python programming kpmg")
f_demo.close()
 
 #append data to file exsisting file
myfile=open("kpmg.txt", "a")
myfile.write("appended text")	
	
print('')
# Let me open the file and check
f_demo = open("PythonSample.txt", "r")
print(f_demo.read())
f_demo.close()

print('')

print('--mutiple lines write')
f_writedemo = open("PythonSample2.txt", "w")
f_writedemo. write("Python")
f_writedemo. write("\n Welcome")
f_writedemo. write("\nHappy Coding!")
f_writedemo. write("\nHi \nHello \nCheers")
f_writedemo.close()
 
# Let me open the file and check
f_writedemo = open("PythonSample2.txt", "r")
print(f_writedemo.read())
f_writedemo.close()

print('')
print('--write lines--')

f_writelinesdemo = open("PythonSample3.txt", "w")
text = ["First Line\n", "Second Line\n", "Third Line\n", 
                                               "Fourth Line"]
f_writelinesdemo. writelines(text)
f_writelinesdemo.close()
 
# Let me open the file and check
f_writelinesdemo = open("PythonSample3.txt", "r")
print(f_writelinesdemo.read())