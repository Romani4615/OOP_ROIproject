class ReturnOnInvestment:
    def __init__(self):
        pass


    def income(self):
        self.inc = int(input('What is your income for the property? '))
        print(f"Your income is {self.inc}")
        #con = input("Type 'yes' to continue to Expenses ")
        #if con == 'yes':
        self.expenzes()
        #if con == 'exit':
         #   exit   

    def expenzes(self):
        self.expenses = []
        repairs = float(input('please enter monthly the $ cost of your Repairs '))
        self.expenses.append(repairs)
        tax = float(input('please enter the monthly $ cost of your Tax '))
        self.expenses.append(tax)
        cashex = float(input('please enter the monthly $ cost of your Cash expenses '))
        self.expenses.append(cashex)
        manager = float(input('please enter the monthly $ cost of your Property Manager '))
        self.expenses.append(manager)
        vacancy = float(input('please enter the monthly $ cost of your Vacancy expenses '))
        self.expenses.append(vacancy)
        mortgage = float(input('please enter the monthly $ cost of your Mortgage expenses '))
        self.expenses.append(mortgage)
        print(self.expenses)
        self.exp = sum(self.expenses)
        print(self.exp)
        #con1 = input("Type 'yes' to continue to Cashflow ")
        #if con1 == 'yes':
        self.cashflow()
        #if con1 == 'exit':
         #   exit   

    def cashflow(self):
        self.cash = self.inc - self.exp
        print(f'Your monthly cash flow is: ${self.cash}')
       # con2 = input("Type 'yes' to continue to find out the whole enchalada, the big cheddar.. your total CASH ON CASH RETURN!!! ")
       # if con2 == 'yes':
        self.cash_on_cash()
        #if con2 == 'exit':
         #   exit
        

        

    def cash_on_cash(self):
        self.coc = []
        dp = int(input("What was your $Cash Dollar down payment for the property? "))
        self.coc.append(dp)
        cc = int(input("What was $Cash Dollhair closing costs for this beast? "))
        self.coc.append(cc)
        rb = int(input("What're we working with as far as the rehab budget goes? "))
        self.TotalInvestment = sum(self.coc)
        print(f'The total cost of your Down Payment, Closing Costs, and Rehab Budget is: {self.TotalInvestment}!')
        self.Anual_cashflow = int(self.cash) * 12
        print(f"Congradulations! The ammount that you're bringing in anually is: {self.Anual_cashflow}!")
        self.cash_on_cash_ROI = self.Anual_cashflow / self.TotalInvestment
        print(f'Here we are, at last. Here is your Cash on cash ROI:\n {self.cash_on_cash_ROI}%')
       #end or repeat loop
        end = input("Type 'yes' to find the cash on cash ROI of another property, or you can exit! ")
        if end == 'yes': 
            roi.income()
        
        elif end == 'exit':
            exit
        else:
            exit


roi = ReturnOnInvestment()

#driver code
while True:
    user_input = input("Welcome.. a litte cash on cash ROI is what the doctor(Sam.. the teacher) ordered, type: yes to find out how much youre making. By typing 'exit', I will ALLOW you to leave lol. ")
    if user_input == 'yes':
        roi.income()

    #getting income input for 
    #income_input = input()
    #income_input = int(income_input)

    if user_input == 'no':
        exit
    else:
        print("wrong input pal")

