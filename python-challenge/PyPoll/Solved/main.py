import os
import csv


# Set path for file
#csvpath = "C:\\Users\\C00979\\DataViz-Lesson-Plans\\01-Lesson-Plans\\03-Python\\2\\Activities\\08-Stu_ReadNetFlix\\Resources\\netflix_ratings.csv"
csvpath = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0 
khan_votes = 0 
correy_votes= 0 
li_votes = 0
tooley_votes = 0
winner = str
votes = []
index = 0


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Loop through looking for the video
    for row in csvreader:
            #print(row[0])
            #total = total + float(row[1])
            #num_months = num_months + 1
            total_votes = total_votes + 1 
            if str(row[2]) == "Khan":
                khan_votes = khan_votes + 1
            elif str(row[2]) == "Correy": 
                correy_votes = correy_votes + 1
            elif row[2] == "Li": 
                li_votes = li_votes + 1
            elif row[2] == "O'Tooley":
                tooley_votes = tooley_votes + 1
            
#            if row[2] in names:
#                    index = names.index(row[2])
#                    votes[index] = votes[index] + 1 
#                    #votes.index[name] = votes.index[name] + 1
#                    #print(name)
#            else:
#                    names.append(row[2])
#                    print(names)
    if khan_votes > correy_votes and khan_votes > li_votes \
        and khan_votes > tooley_votes: 
           winner = "Khan"
    elif correy_votes > khan_votes and correy_votes > li_votes \
        and correy_votes > tooley_votes: 
           winner = "Correy"
    elif li_votes > khan_votes and li_votes > correy_votes \
        and li_votes > tooley_votes: 
           winner = "Li"
    elif tooley_votes > khan_votes and tooley_votes > correy_votes \
        and tooley_votes > li_votes: 
           winner = "O'Tooley"
    else:
        "Uh-oh, runoff"
           
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"Khan Votes: {(khan_votes/total_votes):.2%} ({khan_votes})")
print(f"Correy Votes: {(correy_votes/total_votes):.2%} ({correy_votes})")
print(f"Li Votes: {(li_votes/total_votes):.2%} ({li_votes})")
print(f"O'Tooley Votes: {(tooley_votes/total_votes):.2%} ({tooley_votes})")
print("----------------------")
print(f"Winner is: {winner}")
print("----------------------")

output_path = os.path.join("..", "output", "PyPoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------\n")
    txtfile.write(f"Khan Votes: {(khan_votes/total_votes):.2%} ({khan_votes})\n")
    txtfile.write(f"Correy Votes: {(correy_votes/total_votes):.2%} ({correy_votes})\n")
    txtfile.write(f"Li Votes: {(li_votes/total_votes):.2%} ({li_votes})\n")
    txtfile.write(f"O'Tooley Votes: {(tooley_votes/total_votes):.2%} ({tooley_votes})\n")
    txtfile.write("----------------------\n")
    txtfile.write(f"Winner is: {winner}\n")
    txtfile.write("----------------------")
    
    
    
    
    
    