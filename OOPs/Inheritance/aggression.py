# Class Relationships
# ~Aggregation
# ~Inheritance

# Aggregation(Has-A relationship)
# example

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)
    
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)



class Address:
    def __init__(self, city, pin, state):
        self.__city =city
        self.pin =pin
        self.state =state

    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state



add1 = Address('Gulabpura', 311021, 'Rajasthan')
cust = Customer('Nishtha', 'female', add1)
cust.print_address()
print(cust.name)

# if we want to implement same case of encapsulation, we want to make city private but customer class can't access private variables directly so we will use getter function 

cust.edit_profile('Deepika', 'Jaipur', 302038, 'Rajasthan' )
cust.print_address()

# Class diagram: https://www.youtube.com/live/bEWwM4hXZg8?si=7QXtNsDH1X-vmHQ0