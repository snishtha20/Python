# reading from files
# -> using read()
# f = open('sample.txt','r')
# s = f.read()
# print(s)
# f.close()

# reading upto n chars
# f = open('sample.txt','r')
# s = f.read(7)
# print(s)
# f.close()

# readline() -> to read line by line
# f = open('sample1.txt','r')
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()

# Note: Read tab use hota h jab choti file h means usme text lines kam h. And readline tab use krna h jab badi file ho jisme line of text jyada ho.
# But we don't know how much lines are there in file:
# reading entire using readline without knowing total count of lines

# if u want to open a file via giving path then use double backslash or single forward slash or use r'..path..' (r means raw string)
f = open('C:\\Users\\snish\\Desktop\\Python\\File_Handling\\sample1.txt', 'r')
while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data, end='')
f.close()

# f = open("demo.txt", "r")
# data = f.read()
# data1 = f.read(5)
# data2 = f.readline()
# print(data)
# print(data1)
# print(data2)


# f.close()


# f2 = open("demo1.txt", "r+")
# # f2.write("abc")
# print(f2.read())
# f2.write("abc")
# f2.close()


    

