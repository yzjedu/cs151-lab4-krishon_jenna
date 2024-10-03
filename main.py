# Programmed by Jenna and Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 3, 2024
# Lab Assignment: 04




sub_package = input('What is your cellular package?')
sub_package = sub_package.lower()

while sub_package !='Green' or sub_package !='Blue' or sub_package !='Purple':
    print('Input Invalid! Please enter a valid cellular package')
    sub_package = input('What is your cellular package?' )
    sub_package = sub_package.lower()

used_gigs = input('How many gigabytes have you used?:')