class test:
    def __init__(self, num1,num2):
        print("from constructor 2")
        print(num1)
        print(num2)
    def shi(self):
        print("from sh")
    def shi(self,a):
        print("from sb")
t=test(2,"sdjfh")
t.shi()  
t.shi(2)