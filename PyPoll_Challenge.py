import csv
import os

# Assign variable for file to load and save
file_to_load = os.path.join('resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize variables
total_votes = 0

# Initialize Tracking Variables
counties, candidates = []
county_votes, candidate_votes = {}
top_county, winning_candidate = ''

# Initialize Winning variables
winning_candidate = ''
winning_count, wining_percentage = 0

# Open the election results file and read data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Reader & store headers
    headers = next(file_reader)
    # Read data
    for row in file_reader:
        # Set county and candidate name
        county_name = row[1]
        candidate_name = row[2]
        # Check if candidate name has been added to unique candidates list
        if candidate_name not in candidates:
            # Add candidate's name to unique list and set vote count to 0
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Check if county name has been added to unique county list
        if county_name not in counties:
            # Add county's name to unique list and set vote count to 0
            counties.append(county_name)
            county_votes[county_name] = 0

        total_votes += 1
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

# Open the election results file and read data
with open(file_to_save, 'w') as txt_file:
    # Print final vote count to terminal and write to file
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # TODO: create three if statements to print out voter turnout results for counties
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Calculate percentage of votes for each candidate
    for candidate in candidate_votes:
        # Store vote count
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
