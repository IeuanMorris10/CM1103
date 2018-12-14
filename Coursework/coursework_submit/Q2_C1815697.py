import Q1_C1815697 as c
import matplotlib.pyplot as plt
import numpy as np

def count_wins(num_of_races, file_name = 'sailors_values.csv'):
    name_list = list(c.read_sailor_data(file_name).keys())
    #Creates a dictionary with the names as keys and empty lists as values
    results = {key:0 for key in name_list}
    for i in range(0, num_of_races):
        race_result = c.calculate_finishing_order(c.generate_performances(c.read_sailor_data(file_name)))
        for index, value in enumerate(race_result):
            results[value] += (index + 1)
    return sorted(results.items(), key=lambda keyvalue: keyvalue[1])

def average_modelling(num_of_models, race_result):
    output = {}
    for tuple in race_result:
        #Creates average score output and stores as tuple
        output[tuple[0]] = tuple[1] / num_of_models
    #Returns sorted avg results
    return sorted(output.items(), key=lambda keyvalue: keyvalue[1])


num_of_races = int(input("Number of models: "))
results = count_wins(num_of_races)
#Collects names and results from model
names = [value[0] for value in results]
totals = [value[1] for value in results]
#Calculates avg finsishing position based on the results
averages = average_modelling(num_of_races, results)
avg_values = [value for key, value in averages]


def plot_bar(x_data, y_data, title, x_label, y_label):
    index = np.arange(len(x_data))
    bar_list = plt.bar(index, y_data)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xticks(index, x_data, fontsize=10)
    plt.title(title, fontsize=15)
    x = -0.05 #Set X value for bar count data
    for value in y_data:
        plt.text(x, value * 0.5, value, fontsize=8)
        x += 1


fig_size = plt.rcParams["figure.figsize"] = [6.4, 4.8]
figure = plt.gcf()
plt.subplot(2, 1, 1)
plot_bar(names, totals, "Total Scores", "Names", "Total Score")
plt.subplot(2, 1, 2)
plot_bar(names, avg_values, "Average Position", "Names", "Average Positions")
plt.tight_layout()
plt.show()
