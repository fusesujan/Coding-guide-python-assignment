"""
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older.
"""

import csv
import os


def filter_adults(input_file: str, output_file: str):
    """
    Filter adults from a CSV file and create a new CSV file with the results.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    print(input_file, output_file)
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        adults_data = [row for row in reader if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(adults_data)


def main():
    """
    Test the filter_adults function with "data.csv" as input and "adults.csv" as output.
    """
    script_directory = os.path.dirname(os.path.abspath(__file__))
    inputfile = os.path.join(script_directory, "data.csv")
    outputfile = os.path.join(script_directory, "adults.csv")
    filter_adults(inputfile, outputfile)
    print(f"Filtered adults data written to '{outputfile}'.")


if __name__ == "__main__":
    main()
