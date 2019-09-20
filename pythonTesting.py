# Don't panic; head first python testing
print("Don't panic")

movies = ["The holy grail", 1781,
			[1, 2, 3, 4, 5],
		  "The life of Brian", 1834,
		  "The meaning of life", 1991]

print(movies)

names = ["Talon", "Armine", "Samantha", "Javi"]

print("len(names):", len(names))

# NOTE: print("len(names): " + len(names)) threw a type error: can only concatonate str (not "int") to str

names.append("Jose")

print(names, "============================")

# NOTE: didn't like adding a string to a list, either.
# I need to use the comma every time I want to add something to the end of a print statement RATHER THAN '+'


# else if syntax = elif
for item in movies:
	if isinstance(item, str):
		print("Year:", item)
	elif isinstance(item, int):
		print("POO:", item)
	else:
		print("block in block")
		for in_block in item: # Item is block within block
			print("SOME KINDA BOOGIN'", in_block)

# Block quotes are three quotes -> """
# Single line quotes are pound sign -> #

# Adding new code on checked out python branch