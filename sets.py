# Set stores multiple item in single variables.
# Set items are unordered,unchangeable and doesnot allow duplicate values.

# my_set = {1, 2, 3, 4, 5, 6, 7, 5}
# print(my_set)

# this_set = {"apple", "ball", True, 1, 2}            #True and 1 are
# print(this_set)
#
# a={"npj","skt"}
# a.add("Ktm")
# print(a)
# a.remove("npj")
# print(a)


# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_3=set_1.union(set_2)
# print(f"Union:{set_3}")
# set_4=set_1.intersection(set_2)
# print(f"Intersection:{set_4}")


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "banana", "cherry"}
# myset = set1 | set2 | set3 | set4                  #Union of all sets/////////////////
# print(myset)


# set1 = {1, 2, 3,4,5,6,7}
# set2 = {2, 8, 3,4,5}
# set3 = {0,9,9,8,1,2,3}
# set4 = set1.intersection(set2)
# set5 = set4.intersection(set3)
# print(set5)


set_1 = {"apple", "google"}
set_2 = {"microsoft", "apple"}
set_3 = set_1.difference(set_2)
print(set_3)

fruits = {"Apple", "Ball", "Cat", "kiwi"}
basket = frozenset(fruits)
# print("Unique elements:",basket)
#Add new fruit throws an error
# basket.add("orange")
# print(basket)


city = {"npj", "ktm", "skt"}
place = frozenset(city)
city_place = basket.union(place)
print(city_place)
city_place.add("hello")
print(city_place)
