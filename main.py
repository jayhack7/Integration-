# Josil Petit-Frere Integration project check 1
# this program is a simple mortgage cost program that aks for user salary, house price and esitmates loan
# if user debt/income is 45%, higher than industry recommendations, the program will reject loan application

# Debt to Income (DTI) ratio
# https://www.investopedia.com/terms/d/dti.asp

#Welcome message
class AstroMortgage:
 # ----------------------------------------------------------------------------------------
 # STEP 1 - welcome User
 print("Hello, welcome to Astro Mortgage, the world's #1 mortgage lender!")
 user_name = input("Please enter your name to begin this application: ")
 print("Hello, " + user_name + "!")
 user_occupation = input("What is your occupation? Please enter: ")

 # ----------------------------------------------------------------------------------------
 # STEP 2 - ask User salary

 # + String concaenation to group Strings and Varaibles toether on same line.
 user_salary = int(input("Please enter your annual salary (in whole dollars): "))
 print("You make $" + format(user_salary, "0.2f") + "?", "Nice!")

 # Floor division operator // . I am using this to divide the user's annual salary by 12 months to get monthly salary to whole number amount.
 user_salary_monthly = user_salary // 12

 print("Our calculator estimates your monthly salary is an estimated $" + format(user_salary_monthly, "0.2f") + ".")
 print(
  "How much do you spend paying off debt per month? For example, anything such as credit cards, student loans, existing mortgages, etc.")
 user_debt_monthly = int(input(("Please enter in whole dollar amount: ")))

 # make sure debt is lower than actual income. otherwise it would be impossible
 while (user_debt_monthly >= user_salary_monthly):
  print("ERROR. Are you sure your total monthly debt is higher than your monthly income?")
  user_debt_monthly = int(input(("Please enter total monthly debt in whole dollar amount: ")))

 print("Do you have any other source of income? Such as Social Security income, divinds, etc?")
 user_otherIncome_monthly = 0
 boolean_declareOtherIncome = int(input(("Choose 1 for yes, any other key for no: ")))
 if boolean_declareOtherIncome == 1:
   user_otherIncome_monthly = int(input(("Please enter the amount of this extra income per month, in whole dollar figures: ")))
  else:
   print("That's fine!")

 # ----------------------------------------------------------------------------------------
 # STEP 6 - ask for new House costs
 new_house_cost = int(input("Now, please enter your new house mortgage (in whole dollar amount): "))
 new_house_mortgage_length = int(input("How long is the mortgage period? The usual length is 30 years. Please enter: "))
 # Multiply operator * - finding typical down payment by finding 20% of the mortgage
 print("Now we need to find your down payment. The usual one is 20%. That would be about " + str(
  new_house_cost * 0.20) + " for you.")
 print("Anything lower, we will need to add Private Mortgage Insurance to your costs.")
 user_down_payment_input = int(input("What percent do you plan to put down as down payment? Please enter: "))
 # force input to 1-99
 while (user_down_payment_input <= 0 or user_down_payment_input >= 100):
  user_down_payment_input = int(input(("invalid. Please choose a number between 1-99: ")))
 # use DIVIDE / to convert to decimal

 down_payment = new_house_cost * (user_down_payment_input / 100)

 print("Your downpayment of  $" + format(down_payment, "0.2f") + " will be required before close")



 #divide


 if(user_salary_monthly < new_house_cost):
 # new house cost should not be higher than salary
  print("Your new house payment cant be higher than your salary! How can you afford that?")

 for x in range(2):
  print('Processing your application...')
  # print END function modifies space after entire output is done
  print("NAME:", user_name, "JOB:", user_occupation, end=', ')
  # print SEP function modifies the space between outputs
  print("SALARY:", user_salary_monthly, "MORTGAGE:", new_house_monthly_mortgage, sep=', ')

 #add part sayig NAME, USER INPUT

 # Addition operator + - we are adding User's monthly salary to their monthly other salary to get total monthly cash flow
 user_monthly_cashflow = user_otherIncome_monthly + user_salary_monthly
 # Modulo operator % - to find the reminder o  monthly salary and monthly debt.
 user_debt_ratio = user_monthly_cashflow % user_debt_monthly
 print(user_debt_ratio)

 if (user_debt_ratio) <= 43 :
  # we will APPROVE- below 43% DTI ratio . approve
  print("Congratalations, " + user_name + ", you are approved!")
  print("Your debt-income ratio is " + format(user_debt_ratio, "0.2f") + " is very healthy!"   )
  print("Enjoy your new house!")

 else:
  # we will REJECT - total assets above 43% debt. reject
  print("Unfortunately " + user_name + ", we cannot approve your application at this time")
  print("Your debt-income ratio is " + format(user_debt_ratio, "0.2f") + " is too risky for us to underwrite your loan.")
  print("Your monthly cashflow is " + format(user_monthly_cashflow, "0.2f") + "however, your monthly debt is "  + format(user_debt_monthly, "0.2f"))
  # Subtraction - subtracting User's total monthly cashflow by monthly debts pay to find money remanining
  user_true_monthly_assets = user_monthly_cashflow - user_debt_month
  print("After paying off that debt, you are only left with " + format(user_monthly_cashflow, "0.2f") + ". Astro Mortgage would like to see a more healthy balance.")
  print("Please try again later.")
