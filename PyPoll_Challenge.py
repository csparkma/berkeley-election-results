import csv
import os

# Assign variable for file to load and save
file_to_load = os.path.join('resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize data structures
counties = []
candidates = []
county_votes ={}
candidate_votes = {}

# Initialize Top name variables
top_county = ''
top_candidate = ''

# Initialize tracking variables
total_votes = 0
top_candidate_count = 0
top_candidate_percentage = 0
top_county_count = 0

# Functions to calculate percent of total votes
def calculate_percentage(votes, total_votes):
    """Returns percentage of total votes."""
    return votes/total_votes * 100

# Function to format results for file
def format_results(name, percentage, votes):
    """Returns string of formatted results."""
    return (f'{name}: {percentage:.1f}% ({votes:,})\n')

# Print to terminal and write to text file
def write_to_file(file_writer, formatted_tuple):
    """Writes {formatted_tuple} to text file given by {txt_file} parameter."""
    file_writer.write(formatted_tuple)
    print(formatted_tuple, end="")


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

        # Add a vote tally to total, county & candidate's count
        total_votes += 1
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

# Open the election results file and read data
with open(file_to_save, 'w') as txt_file:
    # Print final vote count to terminal and write to file
    write_to_file(
        file_writer=txt_file,
        formatted_tuple= (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
        )
    )
    # Loop through each county and calculate total votes and percent of total votes
    for county in county_votes:
        # Store vote count
        total_county_votes = county_votes[county]
        # Print/Write County section header before first county is printed
        if top_county_count == 0:
            write_to_file(
                file_writer=txt_file,
                formatted_tuple=("\nCounty Votes:\n")
            )

        # Print each county, voter count, & percentage in Terminal and write to file
        write_to_file(
            file_writer=txt_file,
            formatted_tuple=format_results(
                name=county,
                percentage=calculate_percentage(total_county_votes, total_votes),
                votes=total_county_votes
            )
        )

        if total_county_votes > top_county_count:
            top_county_count = total_county_votes
            top_county = county
    # Format Top County summary to be printed/written to file
    write_to_file(
        file_writer=txt_file,
        formatted_tuple= (
            f"\n-------------------------\n"
            f"Largest County Turnout: {top_county}\n"
            f"-------------------------\n"
        )
    )


    # Loop through each candidate and calculate total votes and percent of total votes
    for candidate in candidate_votes:
        # Store vote count
        total_candidate_votes = candidate_votes[candidate]

        # Calculate the percentage of total candidate votes and format results
        vote_percentage = calculate_percentage(total_candidate_votes, total_votes)
        candidate_results = format_results(candidate, vote_percentage, total_candidate_votes)

        # Print each candidate, voter count, and percentage to the terminal and save to file.
        write_to_file(
            file_writer=txt_file,
            formatted_tuple= candidate_results
        )

        # Determine winning vote count and candidate
        if total_candidate_votes > top_candidate_count:
            top_candidate_count = total_candidate_votes
            top_candidate_percentage = vote_percentage
            top_candidate = candidate

    # Print & Wrte winning candidate summary to file
    write_to_file(
        file_writer=txt_file,
        formatted_tuple= (
            f"-------------------------\n"
            f"Winner: {top_candidate}\n"
            f"Winning Vote Count: {top_candidate_count:,}\n"
            f"Winning Percentage: {top_candidate_percentage:.1f}%\n"
            f"-------------------------\n"
        )
    )
