import csv
import os

# Assign variable for file to load and save
file_to_load = os.path.join('resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the election results file and read data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Reader & store headers
    headers = next(file_reader)
    # Read data
    for row in file_reader:
        print(row)
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote

# Open the election results file and read data
with open(file_to_save, 'w') as txt_file:
    txt_file.write("Hello World")
