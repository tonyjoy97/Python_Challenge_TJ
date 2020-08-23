import csv
import os

cvspath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")

totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]

with open(cvspath) as revenueData:
   reader = csv.DictReader(revenueData)


   for row in reader:

           totalMonth = totalMonth + 1
           totalRevenue = totalRevenue + int(row["Revenue"])

           revenue_change = int(row["Revenue"]) - previousRevenue
           previousRevenue = int(row["Revenue"])
           month_of_change = month_of_change + [row["Date"]]

           if (revenue_change > greatestIncrease[1]):
               greatestIncrease[1] = revenue_change
               greatestIncrease[0] = row["Date"]

           if (revenue_change < greatestDecrease[1]):
               greatestDecrease[0] = row["Date"]
               greatestDecrease[1] = revenue_change
        
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)