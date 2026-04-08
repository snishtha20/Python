# Practice 1
# f= open("practice.txt", "a")
# f.write("Hi everyone")

# f.write("\nwe are learning File I/O")
# f.write("\nusing Java.")
# f.write("\nI like programming Java")


# f.close()

# Practice 2
# f= open("practice.txt", "r")
# data = f.read()

# new_data = data.replace("Java", "python")
# print(new_data)

# f= open("practice.txt", "w")
# f.write(new_data)


# Practice 3
word = "learning"
f = open("practice.txt", "r")
data = f.read()
if(data.find(word) !=-1):
    print("found")
else:
    print("not found")
