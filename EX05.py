#Shubham EX05

#Importing Libraries
import csv
import pandas as pd
import matplotlib.pyplot as plt

#Defining parts function
def get_index(parts):
    if parts[0] == "COVID-19":
        return 8
    else:
        if parts[3] == "0-24":
            return 0
        if parts[3] == "25-34":
            return 1
        if parts[3] == "35-44":
            return 2
        if parts[3] == "45-54":
            return 3
        if parts[3] == "55-64":
            return 4
        if parts[3] == "65-74":
            return 5
        if parts[3] == "75-84":
            return 6
        if parts[3] == "85+":
            return 7
x = ['0-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+']
y= [0,0,0,0,0,0,0,0,]
file = open("covid_comorbidities_USsummary.csv","r")
csv_reader = csv.reader(file)
for row in csv_reader:
        index = get_index(row)
        if index is not None:
            if index != 8:
                y[index] += int(row[4])

#Print Count of people per class of age
for i in range(0,8):
    print("The count of death in",x[i],'age group is',y[i])
print()

#Print the comorbidity with the highest number of "COVID-19 Deaths"
df=pd.read_csv('covid_comorbidities_USsummary.csv')
p=(df["COVID-19 Deaths"].iloc[0:220])
maxnew=str(p.max())
file = open("covid_comorbidities_USsummary.csv","r")
csv_reader = csv.reader(file)
for m in csv_reader:
    if maxnew == m[4]:
       print("The Comorbidity with highest number of COVID-19 Deaths is of",m[1],"which is",p.max())

#To plot graphs
x = ['0-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+']
y = y
fig, ax=plt.subplots(1,2)

#To plot Bar Graph
ax[0].bar(x=x ,height=y, width=0.4)
ax[0].set_xlabel('Age Group')
ax[0].set_ylabel('No. of Deaths')

#To plot Pie Chart
ax[1].pie(y,labels = x,autopct='%1.1f%%',radius=1.3,textprops={'fontsize': 7},)
plt.suptitle('Covid-19 Comorbidities US Summary')
plt.legend(loc=(1,1))
plt.tight_layout()
plt.show()