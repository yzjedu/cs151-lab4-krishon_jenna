# Programmed by Jenna and Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 3, 2024
# Lab Assignment: 04




sub_package = input('What is your cellular package?')
sub_package = sub_package.lower()

used_gigs = int(input('How many gigabytes have you used?:'))

while True:
    if sub_package == 'Green':
        coupon = input('Do you have a coupon?')
        if coupon == 'Yes':
            cellular_cost = ((49.99 + 15 * (used_gigs - 2) - 20))
        else:
            cellular_cost = ((49.99 + 15 * (used_gigs - 2))

    elif sub_package == 'Blue':
    cellular_cost = ((70 + 10 * (used_gigs - 4))
break
    elif sub_package == 'Purple':
            cellular_cost = 99.95
            break
        else:
            print('Input Invalid! Please enter a valid cellular package.')
            sub_package = input('What is your cellular package?')
            sub_package = sub_package.lower()
            break





# sub_package == 'Blue':
   # cellular_cost = (70 + 10 * (used_gigs - 4))


