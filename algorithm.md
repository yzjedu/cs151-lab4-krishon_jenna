# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Ask user what subscription package they use
2. Convert user input to lowercase value
3. While user has input invalid subscription package
   1. Inform them of this, and continue to prompt for valid input.
   2. Convert user input to lower
3. Ask user how much data they used
4. If user uses package green 
   1. Ask user if they have a coupon
   2. If user has a coupon AND GB >= 2, calculate (49.99 + 15(GB - 2) - 20)
   3. If user has a coupon AND GB < 2, calculate (49.99 + 15(GB - 2) - 20)
   4. Otherwise if user doesn't have a coupon, and GB < 2, calculate (49.99 + 15(GB - 2)
5. If user uses package blue
   1. Calculate (70 + 10(GB - 4)
6. If user uses package purple
    1. Calculate (99.95)
7. Output final amount due up to 2 decimal points, AND data used