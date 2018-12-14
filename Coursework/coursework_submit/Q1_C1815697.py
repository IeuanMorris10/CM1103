#Code for modeling sailor race results using mean and standard deviation

import random, operator, csv
from collections import OrderedDict


def series_score(sailor_results, discard=1):
    '''
    Taking the results for a single sailor over a series as a tuple, and returning their total place take away
    the lowest place finish. An argument can also be changed to dictate the number of worst results to remove,
    this is set at 1 initially.
    '''

    #Takes the list of scores out the tuble
    scores = sailor_results[1]
    #Check if discard value is valid
    if discard >= len(scores) or discard < 0:
        return ("Please input a valid number of discards")

    #Sorts list and slice off required values
    sorted_list = sorted(scores, reverse=False)
    for i in range(discard):
        sorted_list.pop()
    #Returns total
    total = (sum(sorted_list))
    return total


def sort_series(results):
    '''
    Taking a list of tuples that contain the sailors name and their results and returning a list that is sorted
    by their series score.
    '''
    results_copy = results.copy()
    #Sorts the copied scores in ascending order
    formatted_output_list = sorted(results_copy, key=lambda x: (series_score(x), x[1][0]))
    #Returns sorted list
    return formatted_output_list


def read_sailor_data(file):
    '''
    Reading data from a CSV file directley into an ordered dictionary.
    '''
    #Output dictionary created
    output_dict = OrderedDict()

    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        next(csvfile) #Skips the title rows of the csv file
        for row in reader:
            #Adds to dictionary with key as name and a tuple of the mean and standard deviation
            output_dict[row[0]] = (float(row[1]), float(row[2]))
    #Returns full dictionary
    return output_dict


def generate_performances(sailor_data):
    '''
    Producing a random number based on mean and standard deviation values using a normal
    distribution
    '''
    #Output dictionary created
    output_dictionary = {}
    for key, value in sailor_data.items():
        normal_result = random.normalvariate(int(value[0]), int(value[1]))
        output_dictionary[key] = normal_result
    #Returns built dictionary
    return output_dictionary


def calculate_finishing_order(generated_sailor_data):
    '''
    Calculating the finishings order from a list of sailors results
    '''
    sorted_list = sorted(generated_sailor_data.items(), key=lambda keyvalue: keyvalue[1])
    #Ony returning the names of sailors
    return [i[0] for i in sorted_list][::-1]


def run_series(num_races, file_name="sailors_values.csv"):
    '''
    Runs a given number of race simulations on a provided set of data
    '''
    #Gets the names from the CSV file
    name_list = list(read_sailor_data(file_name).keys())
    #Creates a dictionary with the names as keys and empty lists as values
    results = {key:[] for key in name_list}
    #Variable i set to 0 to iterate through races
    i = 0
    while i < num_races:
        #Calculates the finishing order of race i
        order = calculate_finishing_order(generate_performances(read_sailor_data(file_name)))
        #Adds each sailors position to the dictionary
        for index, value in enumerate(order):
            results[value].append(index + 1)
        i += 1
    #Creates output list with name and series score
    output = [(key, series_score((key, value))) for key, value in results.items()]
    sorted_output = sorted(output, key=operator.itemgetter(1))
    #List of names in order is then returned
    return [i[0] for i in sorted_output]


print(run_series(6))

#A - print(series_score(("bob", [2, 4, 1, 1, 2, 5])))

#B - print(sort_series([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])]))

#C - print(read_sailor_data("sailors_values.csv"))

#D - print(generate_performances(read_sailor_data("sailors_values.csv")))

#E - print(calculate_finishing_order(generate_performances(read_sailor_data("sailors_values.csv"))))
