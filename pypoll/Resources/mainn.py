import os
import csv
csvpath = os.path.join('election_data.csv')
with open (csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    csv_header= next(csv_reader)

    vote_count = {}
    vote_per = {}
    vote_total = 0


    for row in csv_reader:
        vote_total += 1
        if row[2] in vote_count:
            vote_count[row[2]] += 1
        else:
            vote_count[row[2]] = 1
winner_count = 0
for candidate in vote_count:
     vote_per[candidate] = (vote_count[candidate]/ vote_total)* 100
     if vote_per[candidate] > winner_count:
          winner_count  = vote_count[candidate]
     winner = candidate
print(f"Election Results")
print(f"-----------------------------------")
print(f" Total vote: {vote_total}")
print(f"------------------------------------")
for candidate, votes in vote_count.items():
     print(candidate,':', str(vote_per[candidate]),'%',' ' ,'(',vote_count[candidate],')')
print(f"----------------------------------------------------------")
print(f"Winner: {winner}")
print(f"--------------------------------------------------")


with open("Election Results.text", 'w') as txtfile:
        txtfile.write(f" Election Results\n")
        txtfile.write(f"-----------------------------------------")
        txtfile.write(f"Total Votes: {vote_total}\n")
        txtfile.write(f"------------------------------------------")

        
        for candidate, votes in vote_count.items():
            txtfile.write(f"{candidate}: {str(vote_per[candidate])}%     ({vote_per[candidate]})\n")
            txtfile.write(f"-------------------------------------\n")
            txtfile.write(f"Winner: {winner}\n")
            txtfile.write(f"---------------------------------------\n")


            


