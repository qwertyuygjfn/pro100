class AtmBank:
  
    def __init__(self,cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
       

    def balanceinquiry(self):
        print("yout balance is:Rs.1000")

    def cashwidthdrwal(self,amount):
        new_amount=1000-amount
        print("your withdrwed is : "+str(amount)+"your remaning balance is :"+str(new_amount))
def main():
     name=input("hello what is your name?:") 
     print("hello....."+name)      
     cardnumber = input("insert your card number-")
     pin=input("enter your pin-")
     newuser = AtmBank(cardnumber,pin)

     print("choose your activity:")
     print("1 balace inquiry")
     print("2.cashwidthdrwal")
     activity=int(input("ebter activity choice----"))

     if(activity== 1):
         newuser.balanceinquiry()

     elif(activity==2):
        amount=int(input('enter the amount--'))
        newuser.cashwidthdrwal(amount)  

     else:
        print("error!!!number not valid") 
if __name__ =="__main__":
    main()                      
