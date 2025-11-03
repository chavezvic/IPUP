my_dict = {"name":"Alice", "age":30, "city":"New York"}
name = my_dict["name"]
age = my_dict.get("age")
my_dict["age"] = 31
my_dict["country"] = "USA"
del my_dict["city"]
print(my_dict)
