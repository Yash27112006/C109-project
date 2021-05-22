import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["score"].tolist()

mean = sum(data) / len(data)
std_dev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

std_1_deviation_start, std_1_deviation_end = mean-std_dev, mean+std_dev
std_2_deviation_start, std_2_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
std_3_deviation_start, std_3_deviation_end = mean-(3*std_dev), mean+(3*std_dev)

fig = ff.create_distplot([data], ["scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[std_1_deviation_start, std_1_deviation_start], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[std_1_deviation_end, std_1_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[std_2_deviation_start, std_2_deviation_start], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[std_2_deviation_end, std_2_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in data if result > std_1_deviation_start and result < std_1_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > std_2_deviation_start and result < std_2_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > std_3_deviation_start and result < std_3_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))