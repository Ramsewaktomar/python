name= input("plz enter your name: ")
print("hello",name)
message="""
may i help you sir!
plz select one of them>>>>
type 1>>>check balence
type 2>>>deposite
type 3>>>withdrawl"""
print(message)
available_balence=5000
task=int(input("plz choose one of them: "))
print(task)
#print(type(task))
if task>=1 and task<=3:
    print("welcome to in virtual bank")
    if task==1:#check balence
        print("thanks for visiting us,your available amount is: ",available_balence)
    elif task==2:# deposite
        deposit_amount=int(input("plz enter your deposit amount: "))
        if deposit_amount>=500:
           available_balence=available_balence+deposit_amount
           print("thanks for deposite your amount: ",deposit_amount)
           print("thanks for visiting us, your available amount is: ",available_balence)

    else: #withdrawl
        withdrawl_amount=int(input("plz enter your withdrawl amount: "))
        if available_balence>withdrawl_amount:
            available_balence=available_balence-withdrawl_amount
            print("thank for withdrawl your amount: ",withdrawl_amount)
            print("thank for visiting us,your available amount is: ",available_balence)
        else:
            print("you have not sufficeint amount")
else:
    print("plz choose correct option")
