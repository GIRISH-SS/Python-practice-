dict = {
    'id' : 101,
    'name' : "mohan",
    'sal' : 4500.45
}
print(dict)
print(type(dict))

dict1 = {
    'id' : 102,
    'name' : "rohit",
    'sal' : 4500.45
}
dict1["loc"] = "mumbai"
print(dict1)
dict1.pop('sal')
print(dict1)