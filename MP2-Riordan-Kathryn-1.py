import my_mod 
    
# PART ONE - main menu and user interaction 

# main
print("\nHellloooo, Metalheads!!!")
print("Let's learn a little bit about your favorite Metal artists. \nPick an option below. (Enter Quit to leave)\n")

#while loop to allow program to run until user wants to quit

while True: 
    print()
    print("A: Bands per country")
    print("B: Bands formed in year")
    print("C: Bands with keyword")
    print("D: Longest rocking bands")
    print("Q: Quit\n")

    
#makes sure user inputs match if-else conditions
    user_choice = input().upper()


#calls the appropriate functions from your data module to print a table with countries in the first column and the number of bands formed in that country in the second column
    if user_choice == "A":
        print("Which country has birthed the most metal bands?")
#calls function from my_mod to create a new dictionary with the number of bands per country 
        country_bands = my_mod.get_bands_per_country()
#prints the results in a formatted table with print_table()
        my_mod.print_table(country_bands, "Band Name", "Count", 35)
        
         
    elif user_choice == "B":
#makes sure user input is a four digit integer
        while True:
            try:
                year = int(input("Want to see how Metal a given year was? \nEnter a year and check out which bands formed that year: "))
                user_year = str(year)
    
                if len(user_year) != 4:
                    print("Please enter a valid 4 number year.")
#loops until user enters a 4 digit integer
                else:
                    break
            except:
                print("Please enter an integer")

                
        print("Bands formed in {}:".format(year))
#checks if user input is 1964 or later, the earliest bands in the csv
        if year < 1964:
            year = int(input("Sorry, that year is too early. \nEnter a year after 1964 and check out which bands formed that year: "))

#calls get_bands_formed_in_year from my_mod with user input as argument
        year_bands = my_mod.get_bands_formed_in_year(year)
            
        my_mod.print_table(year_bands, "Band Name", "Country of Origin", 30)



    elif user_choice == "C":
#sets user input to the syle desired
        style = input("Looking for a specific flavor of Metal? Enter a keyword: ")
# calls get_bands_with_style using deisred style as the argument 
        bands_style = my_mod.get_bands_with_style(style)


        print("Bands with {} style:".format(style))
        my_mod.print_table(bands_style, "Band Name", "Styles", 35)
        
       
    elif user_choice == "D":
        bands_to_display = int(input("How many bands do you want to see? "))

        
        if bands_to_display < 1:
            bands_to_display = input("That is not a number. How many bands do you want to see? ")

        longest_lived = my_mod.get_longest_lived_bands(bands_to_display)
        my_mod.print_table(longest_lived, "Band Name", "Years Active", 30)
        #print(bands_to_display)
            
        
#once user inputs q or Q, the program will quit 

    elif user_choice == "Q":
        break

#gives user option to select another choice
    else:
        print("Invalid choice. Please select A, B, C, D, or Q to quit.")
        
