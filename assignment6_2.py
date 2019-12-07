'''Write a program which contains one class named as Circle. Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea(),CalculateCircumference(), Display().
Accept method will accept value of Radius from user. CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.And Display() method will 
display value of all the instance variables as Radius , Area,Circumference.After designing the above class call all instance methods by creating multiple objects.'''
count=0
class Circle:

    PI=3.24
    def __init__(self):
        Radius=0.0
        Area=0.0
        Circumference=0.0
    def Accept(self):
        self.Radius=float(input("enter the radius="))
        
    def CalculateArea(self):
        self.Area=self.PI*self.Radius*self.Radius
        
    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Radius
         
    def Display(self):
        global count
        count=count+1
        print("____OBJECT____",count)
        print("Circle radius is ",self.Radius)
        print("circle of area is",self.Area)
        print("circle of Circumference is",self.Circumference)
        print()
        
def main():
    Obj = []
    no=int(input("enter the how many object crate"))
    for i in range(0,no):
        Obj.append(Circle())
        
    for object in Obj:
        object.Accept()
        object.CalculateArea()
        object.CalculateCircumference()
        object.Display()
    
if __name__=="__main__":
    main()