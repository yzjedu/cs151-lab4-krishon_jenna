# Programmed by Jenna and Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 3, 2024
# Lab Assignment: 04

# Ask the user to input their cellular package
sub_package = input('What is your cellular package?').lower()

# Continue to ask the user to input their cellular package, if they input an invalid value
while sub_package not in ['green', 'blue', 'purple']:
    print('Invalid Input! Please enter valid package name!')
    sub_package = input('What is your cellular package?').lower()

# Ask user to input their used gigabytes
used_gigs = int(input('How many gigabytes have you used?:'))

# Make a decision on the necessary calculation and additional user inputs based on user input, completes the calculation,/
# and outputs the cellular cost and used gigabytes

if sub_package == 'green':
    coupon = input('Do you have a coupon?')
    coupon = coupon.lower()
    if coupon == 'yes':
        cellular_cost = (49.99 + 15 * (used_gigs - 2) - 20)
        rounded_cellular_cost = round(cellular_cost, 2)
        print('Your cellular cost for this month is $', rounded_cellular_cost, 'You used', used_gigs, 'gigabytes.')
    else:
            cellular_cost = (49.99 + 15 * (used_gigs - 2))
            rounded_cellular_cost = round(cellular_cost, 2)
            print('Your cellular cost for this month is $', rounded_cellular_cost, 'You used', used_gigs, 'gigabytes.')
if sub_package == 'blue':
        cellular_cost = (70 + 10 * (used_gigs - 4))
        rounded_cellular_cost = round(cellular_cost, 2)
        print('Your cellular cost for this month is $', rounded_cellular_cost, 'You used', used_gigs, 'gigabytes.')
if sub_package == 'purple':
        cellular_cost = 99.95
        print('Your cellular cost for this month is $', cellular_cost, 'You used', used_gigs, 'gigabytes.')


