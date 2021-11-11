#OOPS CONCEPTS IN PYTHON, methods-function, self-instance, init-constructor, attributes-variables


#1 - OBJECTS AND CLASSES 
class Person:
    
    #init constructor to initialise the objects and members 
    def __init__(self,name):
        self.name = name                #self represents instance of a class, to access methods, attributes of class
        
    
    #creating a method aka function
    def display(self):
        print("Name :",self.name)
        

#Creating objects
p = Person('Sreeram')
p.display()                 #calling a method
        
        

        
# 2 - INHERITANCE
print()
print("INHERITANCE")
#Capability of one class to derive or inherit the properties from some other class.
#A child class can also modify the behavior of the parent class 

#parent-class
class Car(object):
    def __init__(self,company,model):
        self.company = company
        self.model = model
        
    
    def display(self):
        print("Company : ",self.company)
        print("Name : ",self.model)
        
 
#child-class       
class specs(Car):
    def __init__(self,company,model,color,cost):
        self.color = color
        self.cost = cost
        
        Car.__init__(self,company,model)
        Car.display(self)                 #inheriting the method of parent class
        
    def display_s(self):
        print("Color :",self.color)
        print("Cost :",self.cost)
           
        
ob = specs('VW','Ameo',"green",10)
ob.display_s()



#3 - ENCAPSULATION
print()
print("Encapsulation")
#A class is an example of encapsulation as it encapsulates all the data that is member functions, variable

'''It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables. '''


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = 'GeeksforGeeks'          #__ represents private member
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of Base class
        Base.__init__(self)
        print(self.a)                                       #can be accessed as its public attribute
        print("Calling private member of base class: ")
        print(self.__c)                                     #cannot access because its private
  
  
# Driver code
obj1 = Derived()
print(obj1.a)
  
    

