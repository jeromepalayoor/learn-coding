# Writing to a non-delimited file
with open("non_delimited.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")

# Reading from a non-delimited file
with open("non_delimited.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


import csv
# Writing to a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Alice', '25', 'Los Angeles']
]

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import json
# Writing to a JSON file
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from a JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

"""
Theory Question:
Describe the differences between non-delimited text files, CSV files, and JSON files in terms of their 
structure and usage in file I/O operations. Discuss the advantages and disadvantages of each file format 
and provide examples of scenarios where each format would be most suitable.

Practical Question:
Design a Python program for a simple data management system that demonstrates reading from and writing to 
files in different formats (non-delimited text files, CSV files, and JSON files). 
The program should have the following functionalities:

Allow the user to input data for a specific entity (e.g., person, product).
Implement options for the user to save the entered data to a file in the desired format (non-delimited text, CSV, or JSON).
Provide options for the user to load and display the saved data from each file format.
Include validation checks to ensure that the user inputs are in the correct format and that the files are properly read and written.

"""