# defining the data types
integer_var = 10
float_var = 21.3
str_var = "Alvin"
complex_var = 3+5j
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
set_var = {1, 2, 3, 4, 5}
dictionary_var = {"name": "Alvin", "age": 25}
boolean_var = True

# printing the data types
print(integer_var, ": ", type(integer_var))
print(float_var, ": ", type(float_var))
print(str_var, ": ", type(str_var))
print(complex_var, ": ", type(complex_var))
print(list_var, ": ",type(list_var))
print(tuple_var, ": ",type(tuple_var))
print(set_var, ": ",type(set_var))
print(dictionary_var, ": ",type(dictionary_var))
print(boolean_var, ": ",type(boolean_var))

# converting the data types
float(integer_var)
int(float_var)
