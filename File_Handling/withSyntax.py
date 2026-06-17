# Using Context Manager (With)
# It's a good idea to close a file after usage as it will free up the resources
# If we dont close it, garbage collector would close it
# with keyword closes the file as soon as the usage is over

# with 
# with open('C:\\Users\\snish\\Desktop\\Python\\File_Handling\\sample2.txt', 'w') as f:
#     f.write('Nishtha Singh')

# f.write('hello') #will throw an error because file has closed and when file is closed you can't write in that file anymore.

# try f.read() now
# with open('C:\\Users\\snish\\Desktop\\Python\\File_Handling\\sample1.txt', 'r') as f: 
#     print(f.read())

# moving within a file -> 10 char then 10 char: We have limited RAM and if we have to download a large size file, we will download it in chunks. 
# with open('C:\\Users\\snish\\Desktop\\Python\\File_Handling\\practice.txt', 'r') as f:
#     print(f.read(10))
#     print(f.read(10)) #print next 10 characters
# benefit? -> to load a big file in memory
# big_L =['hello world ' for i in range(1000)]
# with open('big.txt', 'w') as f:
#     f.writelines(big_L)

# with open('big.txt', 'r') as f:
#     chunk_size =10
#     while len(f.read(chunk_size)) > 0:
#         print(f.read(chunk_size), end='***')
#         f.read(chunk_size)


# seek and tell function: tell is used to show the position/index where you are. Seek helps to reach wherever u wanna go
# with open('big.txt', 'r') as f:
#     print(f.read(10))
#     print(f.tell()) #it will show 10 because text from 0 to 9 has printed.
#     f.seek(0)
#     print(f.read()) #it will print initial 10 letters including spaces
#     print(f.tell())
#     f.seek(15)
#     print(f.read())


# seek during write
with open('sample.txt', 'w') as f:
    f.write("Helloo")
    f.seek(0)
    # f.write('A')
    f.write('Xa')

