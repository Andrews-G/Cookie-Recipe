#Title: recipe.py
#Author: Grant Andrews
#Date: 1/25/2022
#Description: This program asks a user how many cookies they would like to make,
# it then calculates the correct amount of ingredients needed to make "x" number
# of cookies and prints that to the screen along with the recipe directions.


molasses, butter, flour, rolled_oats = 1.5/48, 1/48, 2.75/48, 2/48                  # Assigning the amount of ingredients necessary to make 1 cookie, based on a recipe that will make 48 cookies.
cookies = float(input("How many cookies would you like to make? \n" ))              # Ask the user how many cookies they would like to make, assign user input to variable "cookies".
print ("To make", cookies, "cookies, you will need:")                               # Tell user than in order to make "cookies variable" cookies, they will need:.
print (format(cookies * molasses, '.3f'), "cup(s) of Molasses.")                    # Calculate and print the amount of molases required for "x" number of cookies   *All amounts are formatted to display 3 decimal places
print (format(cookies * butter, '.3f'), "cup(s) of Butter.")                        # Calculate and print amount of butter required for "x" number of cookies
print (format(cookies * flour, '.3f'), "cup(s) of Flour.")                          # Calculate and print amount of flour required for "x" number of cookies
print (format(cookies * rolled_oats, '.3f'), "cup(s) of Oats.")                     # Calculate and print amount of oats required for "x" number of cookies
print ("Directions: Mix all dry ingredients together, then add wet ingredients.\
 Roll into 3-in balls onto a baking sheet.")                                        # Print directions for recipe