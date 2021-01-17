#===========================================================
#
#  Title:       <Pays and Taxes>
#  Course:      CPS 120
#  Homework:    <number 1>
#  Author:      <Anthony Nielsen>
#  Date:        <1/14/2021>
#  Description:
#       <This program contains a function that finds net pay
#       given two inputs: hourly_rate and time_worked. It also
#       contains several print functions. These print functions
#       print the net_pay function and also each variable and
#       calculation requested in the homework.>
#
#===========================================================
#===========================================================
# Use this formula to represent currency accurate to two decimals:
# '${:,.2f}'.format(variable)# (Just a note to self.)
#
# I initially used str(round()) to get two decimals but noticed it
# didn't print the '0' at the end of gross pay and FICA taxes. My question
# is why does this - '${:,.2f}'.format(variable) - do what it does?
# Can you explain what's going on with that function? I understand that
# .format(variable) does something to the variable. But I am struggling
# to wrap my head around {:,.2f} and how that cuts the decimals correctly.
#
# P.S. Is it okay to ask questions (like the one above) in the code like this?
#      Also - I tried to add comments for everything. Some comments feel 
#      redundant. Is this how you want us to comment on our code?
#      
#      Thanks!
#===========================================================
#===========================================================
# Net pay function. Defines gross pay, all taxes, and gives net pay.
 
def net_pay(hourly_rate, time_worked):
    gross_pay = hourly_rate * time_worked
    fed_tax = gross_pay * 0.15
    FICA = gross_pay * .0765
    state_tax = gross_pay * .0435
    net_pay = gross_pay - fed_tax - FICA - state_tax
    return ('Your net pay is ${:,.2f}'.format(net_pay) + '.')
    
print(net_pay(17.68, 80), '\n') # Prints the net_pay function with
# (17.68, 80) as inputs for hourly_rate and time_worked.

# Hourly rate variable. Input the hourly pay rate here. Used same value
# as above to check accuracy.
hourly_rate = 17.68 
print('Your hourly rate is $' + '{:,.2f}'.format(hourly_rate) + ' per hour.')

# Time worked variable. Input the time worked in hours here. Used same
# value as above to check accuracy.
time_worked = 80
print('You worked ' + str(time_worked) + ' hours.')

# Gross pay calculation.
gross_pay = hourly_rate * time_worked
print('Your gross pay was $' + '{:,.2f}'.format(gross_pay) + '.')

# Federal tax calculation.
fed_tax = gross_pay * 0.15
print('You paid $' + '{:,.2f}'.format(fed_tax) + ' in federal taxes.')

# FICA tax calculation.
FICA = gross_pay * .0765
print('You paid $' + '{:,.2f}'.format(FICA) + ' in FICA taxes.')

# State tax calculation.
state_tax = gross_pay * .0435
print('You paid $' + '{:,.2f}'.format(state_tax) + ' in state taxes.')

# Net pay calculation
net_pay = gross_pay - fed_tax - FICA - state_tax
print('You made $' + '{:,.2f}'.format(net_pay) + ' after taxes.')

