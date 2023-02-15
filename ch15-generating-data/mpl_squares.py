# https://matplotlib.org/

# --------
# plotting a simple graph

# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()

# --------
# changing the label type and line thickness

# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)

# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # set size of tick labels
# ax.tick_params(labelsize=14)

# plt.show()

# --------
# correcting the plot

# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # set size of tick labels
# ax.tick_params(labelsize=14)

# plt.show()

# --------
# using built-in styles

# import matplotlib.pyplot as plt
# plt.style.available

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# to use any built-in styles, add one line of code before calling subplots()
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # set size of tick labels
# ax.tick_params(labelsize=14)

# plt.show()