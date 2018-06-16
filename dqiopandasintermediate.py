# Data Analysis with Pandas: Intermediate
# 6. Calculating Summary Statistics

passenger_classes = [1, 2, 3]
fares_by_class = {}

# Use a for loop to iterate over passenger_classes
for x in passenger_classes:
    # Assign the rows in titanic_survival where pclass value is equal to x
    # titanic_survival["pclass"] is the syntax to select that column
    # You've created a subset of titanic_survival on just pclass == x
    pclass_rows = titanic_survival[titanic_survival["pclass"] == x]
    # Subset that subset further by selecting the fare column
    pclass_fares = pclass_rows["fare"]
    # Calculate the mean of the pclass_fares subset using Series.mean()
    fare_for_class = pclass_fares.mean()
    # Add the mean of the Series.mean() subset to the fares_by_class dictionary
    fares_by_class[x] = fare_for_class
