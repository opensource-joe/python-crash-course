# import the whole file
import pizza_module

# import specific function
from pizza_module import make_pizza

# import function with alias
from pizza_module import make_pizza as mp

# using as to give a module an alias
import pizza_module as p

# importing all functions in a module
from pizza_module import *

# ----------

# whole file or module call includes "." notation module_name.function_name
pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import specific function call includes only function_name
make_pizza(10, 'cheese')
make_pizza(12, 'pepperoni')

# import specific function with alias
mp(16, 'cheese')
mp(12, 'pepperoni')

# import module with alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(10, 'mushroom')

# import all functions in a module
make_pizza(10, 'mushroom')
make_pizza(12, 'cheese')