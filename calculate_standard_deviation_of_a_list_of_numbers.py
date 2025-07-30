import statistics

data=[1,2,3,4,5]
std_dev= statistics.stdev(data)
print(f"The standard deviation of the list {data} is: {std_dev:.2f}")