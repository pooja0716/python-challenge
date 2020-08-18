import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_csv=os.path.join("..","Resources","budget_data.csv")

Total_Months =[]
Total_Profit_Losses=[]
Average_Change=[]

#open and read input file

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header =next(csvreader)
    print (csv_header)

#Hydrate the lists...
    for row in csvreader:
        Total_Months.append(row[0])
        Total_Profit_Losses.append(int(row[1]))

#Calculate Average Change
    for i in range(len(Total_Profit_Losses)-1):
           Average_Change.append(Total_Profit_Losses[i+1] - Total_Profit_Losses[i])

#Find Greatest Increase in Profile/Losses
greatest_increase_pl = max(Average_Change)

#Find Greatest Decrease in Profile/Losses
greatest_decrease_pl = min(Average_Change)

#Find Average Change in Profile/Losses
PL_Average_Change=sum(Average_Change)/len(Total_Months)

#Find Index position of Greatest Increase in Profile/Losses
Max_AC_Index = Average_Change.index(max(Average_Change))
Months_G_Increase_Change=Total_Months[Max_AC_Index+1]

#Find Index position of Greatest Decrease in Profile/Losses
Min_AC_Index = Average_Change.index(min(Average_Change))
Months_G_Decrease_Change=Total_Months[Min_AC_Index+1]

#Print to terminal
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months:  {(len(Total_Months))}")

print(f"Total: $ {sum(Total_Profit_Losses)}")

print(f"Average Change: $ {str(PL_Average_Change)}")
print(f"Greatest Increase in Profits:  ({(str(Months_G_Increase_Change))}) (${(str(greatest_increase_pl))})")

print(f"Greatest Decrease in Profits: ({(str(Months_G_Decrease_Change))}) (${(str(greatest_decrease_pl))})")


#Write to output file
output_path = os.path.join("..", "analysis", "budget_analysis_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Write into the file
    csvfile.write("Financial Analysis")
    csvfile.write("\n")
    csvfile.write("--------------------------------------")
    csvfile.write("\n")
    csvfile.write(f"Total Months:  {(len(Total_Months))}")
    csvfile.write("\n")    
    csvfile.write(f"Total: $ {(sum(Total_Profit_Losses))}")
    csvfile.write("\n")
    csvfile.write(f"Average Change:  {str(PL_Average_Change)}")
    csvfile.write("\n")
    csvfile.write(f"Greatest Increase in Profits:  ({(str(Months_G_Increase_Change))}) (${(str(greatest_increase_pl))})")
    csvfile.write("\n")
    csvfile.write(f"Greatest Decrease in Profits: ({(str(Months_G_Decrease_Change))}) (${(str(greatest_decrease_pl))})")
    csvfile.write("\n")
