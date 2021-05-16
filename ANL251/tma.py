"""
Version: 1.01
Project Title: TMA ANL251 Python Programming July 2020 Presentation
Submission Dateline: 4 August 2020, 2355hrs

Main Algorithms
- Intrate = spend + salarycredit + invest + insurance + billPayment
- Estimated Interest = (dailybalance+salarycredit-spend)*Intrate/12
"""

import os

def clearScreen():
    print("Invalid entry!")
    os.system('cls')
    main() 

class tma:
    def __init__(self, initialBalance ,spendAmt, salaryAmt, investChoice, insuranceChoice, billChoice):
        self.initialBalance = initialBalance
        self.spendAmt = spendAmt
        self.salaryAmt = salaryAmt
        self.investChoice = investChoice
        self.insuranceChoice = insuranceChoice
        self.billChoice = billChoice
        self.interest = 0.00

    """    
    def test_datatype(self):
        print("Initial Balance data type is {}".format(type(self.initialBalance)))
        print("Spend Amount is data type {}".format(type(self.spendAmt)))
        print("Salary Amount is data type {}".format(type(self.salaryAmt)))
        print("Investment Choice is data type {}".format(type(self.investChoice)))
        print("Insurance Choice is data type {}".format(type(self.insuranceChoice)))
        print("Bill Choice is data type {}".format(type(self.billChoice)))
        print("Interest is data type {}".format(type(self.interest)))
    """

    def spending(self):
        if (0<= self.spendAmt<500):
            self.interest = self.interest + 0.0005      # 0.05% Interest
            #print(self.interest)        # logic testing
        elif (500 <= self.spendAmt <=1999):
            self.interest = self.interest + 0.003       # 0.3% Interest
            #print(self.interest)        # logic testing
        elif (self.spendAmt >= 2000 ):
            self.interest = self.interest + 0.008       # 0.8% Interest
            #print(self.interest)        # logic testing
        
       
    def salary(self):
        if (self.salaryAmt<3000):
            self.interest = self.interest + 0.00
            #print(self.interest)        # logic testing
        elif (self.salaryAmt>=3000):
            self.interest = self.interest + 0.004       # 0.4% Interest
            #print(self.interest)        # logic testing

    def invest(self):
        if (self.investChoice == 'Y'):
            self.interest = self.interest + 0.0085      # 0.85% Interest
            #print(self.interest)        # logic testing
        elif (self.investChoice == 'N'):
            self.interest = self.interest + 0.00
            #print(self.interest)        # logic testing
        else:
            clearScreen()

    def insurance(self):
        if (self.insuranceChoice == 'Y'):
            self.interest = self.interest + 0.0085      # 0.85% Interest
            #print(self.interest)        # logic testing
        elif (self.insuranceChoice == 'N'):
            self.interest = self.interest + 0.00
            #print(self.interest)        # logic testing
        else:
            clearScreen()

    def bill(self):
        if (self.billChoice == 'Y'):
            self.interest = self.interest + 0.001       # 0.1% Interest
            #print(self.interest)        # logic test
        elif (self.billChoice == 'N'):
            self.interest = self.interest + 0.00
            #print(self.interest)        # logic test
        else:
            clearScreen()
    
    """
    def bonus_average(self):
        total_amt = self.initialBalance + self.salaryAmt - self.spendAmt
        average_amt = total_amt / 28
        if (average_amt >=80000):
            self.interest = self.interest + 0.03
            print("Average is {}".format(average_amt))
        else:
            self.interest = self.interest + 0
            print("Unfortunately, Average is {}".format(average_amt))
    """
    

    def finalAlgorithm(self):
        print("Total interest is: {} percent per year".format(self.interest*100))
        print("Total interest is: {} percent per month".format((self.interest/12)*100))
        sumBalance = self.initialBalance + self.salaryAmt - self.spendAmt
        sumTotal = sumBalance * (1+(self.interest/12))
        print("You would expect: {}".format(sumTotal))

def welcomeMessage():
    print("Welcome to TMA Interest Calculator")
    print("Every amount you entered is assumed to be in Singapore Dollar and salary credit is after CPF contribution ")
    print("For questions on starting balance, spending and salary, do enter positive numbers")
    print("For the question of Yes or No, Do enter Y for Yes and N for No")
    print("Do take note that unacceptable input will initiate restarting of the program.\n\n")


def invest_Input():
    # This function checks the input for the invest question.
    # It ensures the input should only result to 'Y', 'y', 'N' or 'n'
    # It disallows other inputs, initiating 'clearScreen()' function

    var4 = input("Do you wish to invest? Y/N ").upper()
    if (var4 == 'Y') | (var4 == 'N'):
        return(var4)
    else:
        clearScreen()

def insurance_Input():
    # This function checks the input for the insurance question.
    # It ensures the input should only result to 'Y', 'y', 'N' or 'n'
    # It disallows other inputs, initiating 'clearScreen()' function

    var5 = input("Do you wish to buy insurance plan(s)? Y/N ").upper()
    if (var5 == 'Y') | (var5 == 'N'):
        return(var5)
    else:
        clearScreen()

def bill_Input():
    # This function checks the input for the bill question.
    # It ensures the input should only result to 'Y', 'y', 'N' or 'n'
    # It disallows other inputs, initiating 'clearScreen()' function
    var6 = input("Would you pay 3 bills via the bank? Y/N ").upper()
    if (var6 == 'Y') | (var6 == 'N'):
        return(var6)
    else:
        clearScreen()

def main():
    
    welcomeMessage()
    try:
        var = float(input("Enter your deposit on first day : "))
        if (var < 0): clearScreen()
        var2 = float(input("Enter your estimated spending for the month : "))
        if (var2 < 0): clearScreen()
        var3 = float(input("Enter your credited salary for the month : "))
        if (var3 < 0): clearScreen()

    except ValueError:
        clearScreen()

    finally:
        callOn = tma(var, var2, var3, invest_Input() , insurance_Input(), bill_Input())
        #callOn.test_datatype() 
        #Uncomment to test the datatype of the input generated. This is to verify entries for Question A
        
        
        callOn.spending()
        callOn.salary()
        callOn.invest()
        callOn.insurance()
        callOn.bill()
        

        #callOn.bonus_average() 
        # This calculation is included in the FAQ of the source website. However, since the question does not cover 'eligible' transactions 
        # or when salary is credited in the money, it is not possible to calculate or verify the amount of 'eligible' transactions.
        # The function is created to illustrate the formula if this calculation is included in the algorithm
        
        callOn.finalAlgorithm()
    

if __name__ == "__main__":
    main()

