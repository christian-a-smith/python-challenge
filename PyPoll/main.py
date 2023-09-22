#What the assignment is asking for:
#Total number of votes cast (add up all rows minus the header row)
#Complete list of candidates who received votes (Need list of unique names of all rows in index [2])
#Percentage of votes each candidate won (Add up all rows with name of candidate in index [2] divided by (total rows minus header row))
#Total number of votes each candidate won (Add up all rows with name of candidate in index [2], probably easier to do this step before previous step)
#Winner of the election based on popular vote (print name of candidate with most votes. Will need to store # each candidate got in separate variables)

#start by importing the modules
import csv
import os

#define the paths for both the csv and the text file
#if these don't work, please try opening the folder and then running. It works on my end when I do that
electionfile = os.path.join('Resources', 'election_data.csv')
outputfile = os.path.join('analysis','election_analysis.txt')

#create and store variables for total votes cast, unique dictionary of candidates as well as their votes
#I threw a filter on the csv to see the unique candidates, and only found 3. But will still not cheat and find/store their names the old fashioned way

totalvotecount = 0
candidatetracker = {}

#open the file
with open(electionfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csv_header = next(csvreader)
    #loop
    for row in csvreader:
        #create variables for candidate name row/index for convenience sake
        candidate = str(row[2])
        #check if candidate name is stored in dictionary or not. If is not, add and count first vote. Otherwise add a vote
        if candidate not in candidatetracker:
            candidatetracker[candidate]=1
        else:
            candidatetracker[candidate]+=1
        #add 1 to total vote counter
        totalvotecount+=1

#start printing to text file
with open(outputfile,'w') as txtfile:
    #print the header and the lines first
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("------------------------------")
    txtfile.write("\n")
    #print total votes
    txtfile.write(f"Total Votes: {totalvotecount}")
    txtfile.write("\n")
    txtfile.write("------------------------------")
    txtfile.write("\n")
    #loop through the values in the dictionary
    for name,value in candidatetracker.items():
        #print out the name, percentage, and total votes for each candidate
        txtfile.write(f"{name}: {(value/totalvotecount):.3%} ({value})")
        txtfile.write("\n")
    txtfile.write("------------------------------")
    txtfile.write("\n")
    #make a final check for who got the most votes and print the winner
    finaltally = 0
    finalwinner = ""
    for name,value in candidatetracker.items():
        if value > finaltally:
            finaltally = value
            del finalwinner
            finalwinner = name
    txtfile.write(f"Winner: {finalwinner}")
    txtfile.write("\n")
    txtfile.write("------------------------------")