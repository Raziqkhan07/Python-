# # Program to show various ways to read and
# # write data in a file.
# file1 = open("myfile.txt","w")
# L = ["This is Delhi \n","This is Paris \n","This is London \n,This is INDIA\n"]
#
# # \n is placed to indicate EOL (End of Line)
# file1.write("Hello \n")
# file1.writelines(L)
# file1.close() #to change file access modes
#
# file1 = open("myfile.txt","r+")
#
# print("Output of Read function is ")
# print(file1.read(5 ))
# print()
#
# # seek(n) takes the file handle to the nth
# # bite from the beginning.
# file1.seek(0)
#
# print( "Output of Readline function is ")
# print(file1.readline())
# print(file1.readline())
# print(file1.readline(),end='')
# print(file1.readline())
# print()
#
# file1.seek(0)
#
# # To show difference between read and readline
# print("Output of Read(9) function is ")
# print(file1.read(9))
# print()
#
# file1.seek(0)
#
# print("Output of Readline(9) function is ")
# print(file1.readline())
# print(file1.readline())
# print(file1.readline(),end='')
# print(file1.readline())
#
#
# file1.seek(0)
# # readlines function
# print("Output of Readlines function is ")
# print(file1.readlines())
# print()
# file1.close()


# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()

# The file should exist in the same directory as the python program file else, full address of the file should be written on place of filename.Note: The r is placed before filename to prevent the characters in filename string to be treated as special character. For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in same directory and address is not being placed.

