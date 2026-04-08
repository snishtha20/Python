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

# with Syntax
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

with open("sample.txt", "w") as f:
    f.write("new data")
    
