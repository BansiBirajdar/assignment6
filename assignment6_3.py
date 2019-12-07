'''3. Write a program which contains one class named as Arithmetic.Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().Accept method will accept value of Value1 and Value2 from user.Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.After designing the above class call all instance methods by creating multiple objects.'''


class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0
    
    def Accept(self):
        self.value1=int(input("enter the value1="))
        self.value2=int(input("enter the value2="))
    def Addition(self):
        return(self.value1+self.value2)
    def Subtraction(self):
        return(self.value1-self.value2)
    def Multiplication(self):
        return(self.value1*self.value2)
    def Division(self):
        if self.value2==0:
            return
        else:
            return(self.value1//self.value2)
    
def main():
    global count
    Obj =[]
    no=int(input("enter the how many object="))
    for i in range(0,no):
        Obj.append(Arithmetic())
    for OBJ in Obj:
        count+=1
        print()
        print("--OBJECT--",count)
        OBJ.Accept()
        print("ADDITION      =",OBJ.Addition())
        print("Subtraction   =",OBJ.Subtraction())
        print("Multiplication=",OBJ.Multiplication())
        if OBJ.Division()==None:
            print("Enter the positive Number")
        else:
            print("Division      =",OBJ.Division())
count=0
if __name__=="__main__":
     main()