
 # Open source file in read mode
"""with open("C:\\Users\\mylar\\OneDrive\\Documents\\python text files\\source.txt", "r") as source_file:

     # Open destination file in write mode
     with open("C:\\Users\\mylar\\OneDrive\\Documents\\python text files\\destination.txt", 'w') as dest_file:
        # Read all lines from source file
        contents = source_file.read()
        print(contents)
         # Write contents to destination file
        dest_file.write(contents)

print("Contents copied successfully!")"""

"""import pandas as pd
from tabulate import tabulate

file_path = "C:\\Users\\mylar\\Downloads\\data.csv"

df = pd.read_csv(file_path)

print(tabulate(df, headers='keys', tablefmt='grid'))"""

import csv

file_path ="C:\\Users\\mylar\\Downloads\\data.csv"


# Function to get user input and write it to the CSV file
"""def add_row_to_csv(file_path):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, city])
    print("Row added successfully!")


# Run the function to add a row
add_row_to_csv(file_path)"""

"""import json

file_path = "C:\\Users\\mylar\\Downloads\\json.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)

    for key, value in data.items():
        print(f"{key}: {value}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")"""