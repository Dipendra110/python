##Dictionary stores data in key,value pairs.
##It is ordered,changeable and doesnt allow key duplicates


# info = {
#     "name": "abc",
#     "address": "npj",
#     "age": 21,
#     "is_verified":True,
# }
# print(info["name"])
# print(info)
# info["address"]="ktm"
# print(info)
# info.pop("is_verified")           ##Remove the desired key
# print(info)
# info["gender"]="male"             ##Add new key,value in dictionary
# print(info)
# for key,value in info.items():
#     print(f'"key:{key}":value:{value}')

# info_1=info
# info_1["email"]="abc@gmail.com"
# print(f"Info:{info}")
# print(f"Info_1:{info_1}")


my_family = {
    "child1": {
        "name": "Emilly",
        "year": 2000
    },
    "child2": {
        "name": "Dia",
        "year": 2009
    },
    "child3": {
        "name": "Chris",
        "year": 2029
    },
}
# del my_family['child3']['name']              ##Delete the selected key
my_family['child3']['age'] = 22
print(my_family)
# print(my_family['child3']['name'])
