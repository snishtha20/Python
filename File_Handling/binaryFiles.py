# Problems with working in text mode
# can't work with binary files like images
# not good for other data types like int/float/list/tuples

# working with binary file
# with open('image.jpg', 'r') as f:
#     f.read() #will throw error because 'r' used to read text files not binary files

# working with binary file
#  first will create copy of image here
with open('image.jpg', 'rb') as f: #this will read binary file
    with open('image_copy.jpg', 'wb') as g: #this will write in binary file
        g.write(f.read()) #f jo bhi read krega saath ke saath hi g usse nayi file me write kr dega

# working with other data types
with open('sample.txt','w') as f:
  f.write(5) #will throw error text files only read string no primitive & complex data like list, dict

# Still if we want to print 5
with open('sample.txt','w') as f:
  f.write('5')

with open('sample.txt','r') as f:
  print(f.read() + 5) #throw error because f.read() will read 5 as a string & string and int cannot add

with open('sample.txt','r') as f:
  print(int(f.read()) + 5)

# more complex data
d = {
    'name':'Nishtha',
     'age':21,
     'gender':'female'
}

with open('sample.txt','w') as f:
  f.write(d) #throw error because it cannot take dict as input

with open('sample.txt','w') as f:
  f.write(str(d)) #we have to convert into string


with open('sample.txt','r') as f:
  print(f.read()) #read dict as string
  print(type(f.read())) #string

with open('sample.txt','r') as f:
  print(dict(f.read())) #throw error because we cannot convert string back to dict and we cannot perform dict's operation

# The soultion of all these problems is serialization & deserialization