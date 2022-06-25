# CALCULATING YEARLY INTEREST USING PYTHON

print("How many years you want to save?")
years = int(input('Enter years: '))


print('How much money do you have in your account?')
principal = float(input('Enter amount: '))


print('How much do you plan to invest monthly?: ')
monthly_invest = float(input('Enter amount: '))

print('Estimate of yearly interest on investment')

interest = float(input('Enter Interest: '))

print(' ')

monthly_invest = monthly_invest * 12 


final_amount = 0 


for i in range(0, years) :
    if final_amount == 0 :
        final_amount == principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)


print(f"you'll have {final_amount}  after {years} year/s")