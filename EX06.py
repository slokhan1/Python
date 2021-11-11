#Q1
from bokeh.plotting import figure, output_file, show
import csv
semesters_name = ['Spring 18', 'Fall 18', 'Spring 19','Fall 19','Spring 20','Fall 20']
with open('SSE_Courses.csv', newline='') as file:
     reader = csv.reader(file)
     data = []
     for row in reader:
          data.append(row)
#Line Plot
output_file("EM_by_semester.html")
p = figure(x_range=semesters_name, plot_width=600, plot_height= 600, title='EM by semester', x_axis_label="Semesters", y_axis_label="EM enrollments")
p.line(semesters_name,data[1][1:], line_width=3, line_color="green")
show(p)

#Scatter Plot
from bokeh.plotting import figure, output_file, show
import csv
with open('SSE_Courses.csv', newline='') as file:
     reader = csv.reader(file)
     data = []
     for row in reader:
          data.append(row)
output_file("EM_by_semesters.html")
p = figure(title='EM vs SYS', x_axis_label="EM", y_axis_label="SYS")
p.scatter(data[1][1:],data[5][1:], fill_alpha=0.3, size=9, fill_color='red',line_color='red')
show(p)

#Bar Chart
import numpy as np
from bokeh.plotting import figure, output_file, show
import csv
with open('SSE_Courses.csv', newline='') as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
output_file("Average enrolment by program.html")
EM_path = [float(i) for i in data[1][1:]]
EM = np.mean(EM_path)
ES_path = [float(i) for i in data[2][1:]]
ES = np.mean(ES_path)
ISE_path = [float(i) for i in data[3][1:]]
ISE = np.mean(ISE_path)
SSW_path = [float(i) for i in data[4][1:]]
SSW = np.mean(SSW_path)
SYS_path = [float(i) for i in data[5][1:]]
SYS = np.mean(SYS_path)
Final_list = [EM, ES, ISE, SSW, SYS]
Subjects = ['EM', 'ES', 'ISE', 'SSW', 'SYS']
p = figure(x_range=Subjects, height=560, title="Average enrollment by program over the years",
           toolbar_location=None, tools="")
p.vbar(x=Subjects, top=Final_list, width=0.4,color= 'green')
p.xgrid.grid_line_color = None
p.y_range.start = 0
show(p)

#Pie Chart
from bokeh.plotting import figure, output_file, show
import csv
import math
with open('SSE_Courses.csv', newline='') as file:
     reader = csv.reader(file)
     data = []
     for row in reader:
          data.append(row)
EM_Total = float(data[1][5]) + float(data[1][6])
ES_Total = float(data[2][5]) + float(data[2][6])
ISE_Total = float(data[3][5]) + float(data[3][6])
SSW_Total = float(data[4][5]) + float(data[4][6])
SYS_Total = float(data[5][5]) + float(data[5][6])
total = EM_Total + ES_Total + ISE_Total + SSW_Total + SYS_Total
output_file("piechart.html")
graph = figure(title = "Enrollment for the 5 programs for 2020")
sectors = ['EM', 'ES', 'ISE', 'SSW', 'SYS']
percentages = [(EM_Total/total)*100, (ES_Total/total)*100, (ISE_Total/total)*100, (SSW_Total/total)*100, (SYS_Total/total)*100]
radians = [math.radians((percent / 100) * 360) for percent in percentages]
start_angle = [math.radians(0)]
prev = start_angle[0]
for i in radians[:-1]:
    start_angle.append(i + prev)
    prev = i + prev
end_angle = start_angle[1:] + [math.radians(0)]
x = 0
y = 0
radius = 0.6
color = ["red", "pink", "green", "blue", "yellow"]
for i in range(len(sectors)):
    graph.wedge(x, y, radius,
                start_angle = start_angle[i],
                end_angle = end_angle[i],
                color = color[i],
                legend_label = sectors[i])
show(graph)