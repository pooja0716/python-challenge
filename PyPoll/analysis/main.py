import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv=os.path.join("..","Resources","election_data.csv")


Total_Votes =0
Candidate_Khan=0
Candidate_Correy=0
Candidate_Li=0
Candidate_OTooley=0


#open and read input file

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header =next(csvreader)
    print (csv_header)


#Hydrate the lists...
    for row in csvreader:
        Total_Votes=Total_Votes+1
        if row[2]=="Khan":
            Candidate_Khan=Candidate_Khan+1
        elif  row[2] == "Correy":
            Candidate_Correy=Candidate_Correy+1
        elif row[2] == "Li":
            Candidate_Li=Candidate_Li+1
        elif row[2] == "O'Tooley":
            Candidate_OTooley=Candidate_OTooley+1

Khan_Percentage=round((Candidate_Khan/Total_Votes)*100,0)
Correy_Percentage=round((Candidate_Correy/Total_Votes)*100,0)
Li_Percentage=round((Candidate_Li/Total_Votes)*100,0)
OTooley_Percentage=round((Candidate_OTooley/Total_Votes)*100,0)

Winner_dic={
            "Khan":Candidate_Khan,
            "Correy":Candidate_Correy,
            "Li":Candidate_Li,
            "OTooley":Candidate_OTooley
}

Winner_Name= max(Winner_dic, key=Winner_dic.get)

print("Election Results")
print("-------------------------------------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------------------------------------")
print(f"Khan : {Khan_Percentage}% ({Candidate_Khan})")
print(f"Correy : {Correy_Percentage}% ({Candidate_Correy})")
print(f"Li : {Li_Percentage}% ({Candidate_Li})")
print(f"O'Tooley : {OTooley_Percentage}% ({Candidate_OTooley})")
print("-------------------------------------------------------")
print(f"Winner : {Winner_Name}")
print("-------------------------------------------------------")


#Write to File
output_path = os.path.join("..", "analysis", "election_data_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Write into the file
    csvfile.write("Election Results:")
    csvfile.write("\n")
    csvfile.write("-------------------------------------------------------")
    csvfile.write("\n")
    csvfile.write(f"Total Votes: {Total_Votes}")
    csvfile.write("\n")  
    csvfile.write("-------------------------------------------------------")
    csvfile.write("\n")
    csvfile.write(f"Khan : {Khan_Percentage}% ({Candidate_Khan})")
    csvfile.write("\n")
    csvfile.write(f"Correy : {Correy_Percentage}% ({Candidate_Correy})")
    csvfile.write("\n")
    csvfile.write(f"Li : {Li_Percentage}% ({Candidate_Li})")
    csvfile.write("\n")
    csvfile.write(f"O'Tooley : {OTooley_Percentage}% ({Candidate_OTooley})")
    csvfile.write("\n")
    csvfile.write("-------------------------------------------------------")
    csvfile.write("\n")
    csvfile.write(f"Winner : {Winner_Name}")
    csvfile.write("\n")
    csvfile.write("-------------------------------------------------------")