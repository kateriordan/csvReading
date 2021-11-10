import csv

# globals
# strings for the columns names in the csv file and for the file name
style = 'style'
year_formed = 'formed'
year_split = 'split'
band_name = 'band_name'
origin_country = 'origin'
file_end_date = 2017
metal_file_name = 'metal_bands_2017_MP2.csv'

def read_data(file_name):
#open and read the file
    with open(file_name, 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        csv_list = [row for row in reader]
#returns all the file data as a list 
    return csv_list

                          

def get_bands_formed_in_year(year):
#gets the data from the csv using the read_data() function
    band_data = read_data(metal_file_name)

    bands_formed_in_year = [(row[band_name], row[origin_country]) for row in band_data if row[year_formed] == str(year)]
        
   
#returns a tuple for each element in the nested list in the form of (band_name, country)

    return bands_formed_in_year

#return a nested list of tuples or lists containing info for bands with a given keyword in their style
def get_bands_with_style(style_keyword):
    band_data = read_data(metal_file_name)

#iterates through the nested list, looking at the data in the band's 'style' column
    bands_with_style = [(row[band_name], row[style].replace(",",", ")) for row in band_data if style_keyword.upper() in row[style].upper()] 
    
    return bands_with_style


#looks at the 'origin' column of each row, and counts up the number of bands who claim that country as an origin
def get_bands_per_country():
    band_data = read_data(metal_file_name)

    bands_per_country = {}
    
    for row in band_data:
        country = row[origin_country]

        if country == "":
            country = "Unaffiliated"
        if country not in bands_per_country:
            bands_per_country[country] = 1
        else:
            bands_per_country[country] += 1
 
        #bands_per_country[row[band_name]] = country
    bands_sorted = sort_by_dict_value(bands_per_country)
    
    return bands_sorted


def get_longest_lived_bands(num_bands):
#returns the data from the file with read_data()
    band_data = read_data(metal_file_name)


    band_len = {}
    for row in band_data:
        years_formed = row[year_formed]
        if years_formed != "-":
            split = row[year_split]
            if split == "-":
                split = file_end_date
            years_together = int(split) - int(years_formed)
            if years_together == 0:
                years_together = 1

            band_len[row[band_name]] = years_together

    longest_bands = sort_by_dict_value(band_len)
#returns a splice of the sorted dictionary depending on how many bands the user wants to see
    return longest_bands[:int(num_bands)]
    
    
#sorts the dictionaries into ascending lists     
def sort_by_dict_value(dict_to_sort):
    new_list = [[value, key] for key, value in dict_to_sort.items()]
    new_list = sorted(new_list)
    new_list.reverse()
    new_list = [[value, key] for key, value in new_list]
    return new_list


#Prints all the elements of a nested list in two collumns
def print_table(new_list, col_1_name, col_2_name, width = 10):
     
    print_template = "{:<{}}{:<{}}"
#takes the list name, column 1 & two names, and width as arguments 
    print(print_template.format(col_1_name, width, col_2_name, width))
    print("-" * width * 2)
    for couple in new_list:
        print(print_template.format(couple[0], width, couple[1], width))
    print("")


