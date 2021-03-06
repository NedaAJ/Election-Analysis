#add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.   
file_to_save = os.path.join("analysis", "election_analysis.txt")

#setting total_votes to 0
total_votes=0

#candiate options / list
candidate_options=[]
#Declare a empty dictionary
candidate_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0


# Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file object with reader Function (function found in csv module)
    file_reader=csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #add the total vote count
        total_votes +=1
        
        #Print the candidate name from each row (column 3)
        candidate_name=row[2]

        #if the candidate is not already in the candidate list.
        if candidate_name not in candidate_options:
            # add the candidate name to candidate list
            candidate_options.append(candidate_name)

            #the tracking of candidates vote count
            candidate_votes[candidate_name]=0

        #add a vote to candidate's count
        candidate_votes[candidate_name] +=1

        # Save the results to our text file.
    with open (file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        Election_results=(f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
        print(Election_results, end="")

        # Save the final vote count to the text file.
        txt_file.write(Election_results)

        winning_count=0
        # iterate through the candidate dictionary.
        for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate
            votes=candidate_votes[candidate_name]
            #calculate the percentage of the vote count
            vote_percentage= float(votes)/float(total_votes)*100
            
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)


            #print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            #print(f"{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n")


            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count=votes
                # And, set the winning_candidate equal to the candidate's name.
                winning_percentage=vote_percentage
                winning_candidate=candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)