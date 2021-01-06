import os
#the different options when opening are "x" to create, "a" to append info, "w" to write (overwriting) and "r" to read
#you can add a "b" or a "t" to specify binary or text form
# We will Create a file, using "w" option. If file is created it will just open it
myfile = open("myfile.txt", "w")

try:
    myfile.write("This is a file created in Python\n")
    myfile.write("Other kinds of files can also be handled\n")
    myfile.write("We will write and read from it, delete it at the end.\n")

finally:
    myfile.close()


#Now we read from the file, we can use a better method using "with"
with open("myfile.txt", "r") as reader:
    for line in reader.readlines():
        print(line, end="")


#Now we add a line or two
with open("myfile.txt", "a") as writer:
    writer.write("Here we can add a new line to the file.\n")
    writer.write("This is the last line in the file.\n")


#We read again
with open("myfile.txt", "r") as reader:
    for line in reader.readlines():
        print(line, end="")


# We will wait for input just to give time to see the generated file
input("Press enter to delete the file and end the program")


#finally we delete the file
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File removed")
else:
    print("File not found")