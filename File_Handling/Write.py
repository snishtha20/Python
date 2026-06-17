# case 1 - if the file is not present
# f = open('sample.txt','w')
# f.write('Hello world')
# f.close()
# # since file is closed hence this will not work
# f.write('hello')

# # write multiline strings
# f = open('sample1.txt','w')
# f.write('hello world')
# f.write('\nhow are you?')
# f.close()

# # case 2 - if the file is already present
# f = open('sample.txt','w')
# f.write('Nishtha Singh')
# f.close()

# write lines
L = ['hello\n','hi\n','how are you\n','I am fine']

f = open('C:\Users\snish\Desktop\Python\File_Handling\sample2.txt','w')
f.writelines(L)
f.close()