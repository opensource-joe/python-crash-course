# initial set up
# from die import Die

# # create a D6
# die = Die()

# # make some rolls, and sotre results in a list
# results = []
# for roll_num in range(100):
#     result = die.roll()
#     results.append(result)

# print(results)

# -------------------------------
# analyzing the results

# from die import Die

# # create a D6
# die = Die()

# # make some rolls, and sort results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # analyze the results
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

# -------------------------------
# making a histogram

# import plotly.express as px

# from die import Die

# # create a D6
# die = Die()

# # make some rolls, and sort results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # analyze the results
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # visualize the results
# fig = px.bar(x=poss_results, y=frequencies)
# fig.show()

# -------------------------------
# customizing the plot

# import plotly.express as px

# from die import Die

# # create a D6
# die = Die()

# # make some rolls, and sort results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # analyze the results
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # visualize the results
# title = "Results of Rolling one D6 1,000 times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()