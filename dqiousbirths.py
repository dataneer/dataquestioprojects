# Guided Project in dataquest.io
# Explore U.S. Births

# Read in the file and split by line
f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
read = f.read()
split_data = read.split("\n")

# Refine reading the file by creating a function instead
def read_csv(file_input):
    file = open(file_input, "r")
    read = file.read()
    split_data = read.split("\n")
    no_header = split_data[1:len(split_data)]
    final_list = list()
    for i in no_header:
        string_fields = i.split(",")
        int_fields = []
        for i in string_fields:
            int_fields.append(int(i))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

# Create a function that takes a list of lists argument
def month_births(input_lst):
    # Store monthly totals in a dictionary
    births_per_month = {}
    for i in input_lst:
        # Label the columns
        month = i[1]
        births = i[4]
        # Check if item already exists in dictonary list
        if month in births_per_month:
            # Add the current number of births to the new integer
            births_per_month[month] = births_per_month[month] + births
        # If the item does not exist, create it with integer of births
        else:
            births_per_month[month] = births
    return births_per_month
cdc_month_births = month_births(cdc_list)

# This function uses day of the week instead of month
def dow_births(input_lst):
    births_per_day = {}
    for i in input_lst:
        dow = i[3]
        births = i[4]
        if dow in births_per_day:
            births_per_day[dow] = births_per_day[dow] + births
        else:
            births_per_day[dow] = births
    return births_per_day
cdc_day_births = dow_births(cdc_list)

# This function is more superior because it is a generalized form
def calc_counts(data, column):
    sums_dict = {}
    for row in data:
        col_value = row[column]
        births = row[4]
        if col_value in sums_dict:
            sums_dict[col_value] = sums_dict[col_value] + births
        else:
            sums_dict[col_value] = births
    return sums_dict

