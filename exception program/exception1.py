num=int(input("enter number "))
# raise used to own type exception
try:
      if num<0:
        raise Exception("you entered negative number  please enter positive number")
      else:
        print("you entered  {}".format(num))
except Exception as identifier:
    print(identifier)