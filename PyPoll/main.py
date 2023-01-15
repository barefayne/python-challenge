import os
import csv

# csv file path
election_csv = r"C:\Users\Bethelhem\Desktop\HomeWork\python-challenge\PyPoll\Resources\election_data.csv"
# Output path
output_path = r'C:\Users\Bethelhem\Desktop\HomeWork\python-challenge\PyPoll\analysis\results.txt'
# List/ variables
total_votes = 0
c_list = []
c_votes = {}
winner= ""
w_count = 0
w_percentage = 0

# open csv and read
with open(election_csv, 'r', encoding='utf-8') as election_file:
    election_rows = csv.reader(election_file, delimiter= ',')
    headers = next(election_rows)
    
    # Read each row 
    for row in election_rows:

        # Add to the total votes 
        total_votes += 1

        # Candidate name from each row
        c_name = row[2]

        # Get list of candidates who received votes
        if c_name not in c_list: 
            c_list.append(c_name)
            c_votes[c_name] = 0
        c_votes[c_name] += 1
# Open the output file
with open(output_path, 'w') as text_file:
    e_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n")
    print(e_results)
    text_file.write(e_results)
 
    # The total number of votes each candidate won
    for c_name in c_votes: 
        # The number of votes each candidate won
        votes = c_votes[c_name]
        # The percentage of votes each candidate won
        vote_prcentage = round((float(votes)/float(total_votes)) * 100, 3)

        c_result = (f"{c_name}: {vote_prcentage}% ({votes})\n")
        print(c_result)
        text_file.write(c_result)
        

      # The winner of the election based on popular vote
        if votes > w_count: 
            w_count = votes
            winner = c_name

    w_results = (
        f"-----------------------\n"
        f"Winner: {winner}\n"
        f"-----------------------\n")
    print(w_results)
    text_file.write(w_results)




 





    