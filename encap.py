#ENCAPSULATION.
class Bank:
    def __init__(self):
        self.__balance=0
    def Acc(self):
        self.__balance=0
    def deposit(self,am):
        if am>0:
            self.__balance+=am
            print("Amount is Deposited.")
            print("total Balance is ",self.__balance)
    def view(self):
        print("Total amount=",self.__balance)


acc1=Bank()
acc1.deposit(10000)
acc1.view()
