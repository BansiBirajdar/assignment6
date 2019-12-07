'''Write a program which contains one class named as Demo.Demo class contains two instance variables as no1 ,no2.That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance variables.Initialise instance variable in init method by accepting the values from user.
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()'''

class demo:
    def __init__(self,value1,value2):
        self.no1=value1
        self.no2=value2
        print("inside init")
    def Fun(self):
        print("inside the Fun")
        print("no1=",self.no1)
        print("no2=",self.no2)
    def Gun(self):
        print("inside the Gun")
        print("no1=",self.no1)
        print("no2=",self.no2)
    
        
def main():
    print("inside main")
    no1=int(input("enter the no1="))
    no2=int(input("enter the no2="))
    Obj1=demo(no1,no2)
    no1=int(input("enter the no1="))
    no2=int(input("enter the no2="))
    Obj2=demo(no1,no2)
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if (__name__=="__main__"):
    main()