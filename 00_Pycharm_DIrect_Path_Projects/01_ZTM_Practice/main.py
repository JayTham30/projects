# # Given the below class:
# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat("ragdoll", 5)
# cat2 = Cat("siamese", 10)
# cat3 = Cat("shorthair", 2)
#
#
# # 2 Create a function that finds the oldest cat
# def get_oldest_cat(*args):
#     return max(args)
#
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
#
# print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# #1 Add nother Cat
#
# class Taku(Cat):
#     def sing(self, sounds):
#         return f"{sounds}"
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
#
# my_cats = [Taku("Taku", 2), Sally("Sally", 4), Simon("Simon", 6)]
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
#
# my_pets = Pets(my_cats)
#
# #4 Output all of the cats walking using the my_pets instance
#
# my_pets.walk()
#
# print(Taku.is_lazy)


# class SuperList(list):
#     def __len__(self):
#         return 1000
#
#
# super_list1 = SuperList()
#
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1)
#
# from functools import reduce
#
# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
# def capitalize(item):
#     return item.capitalize()
#
# print(list(map(capitalize, my_pets)))
#
#
# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
#
# print(list(zip(my_strings, sorted(my_numbers))))
#
# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
#
# def good_score(score):
#     return score > 50
#
# print(list(filter(good_score, scores)))
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#
# def accumulator(acc, item):
#     return (acc + item)
#
# print(reduce(accumulator, (my_numbers + scores)))


# Square root using lambda experession

# my_list = [5, 4, 3]
#
# print(list(map(lambda item: item ** 2, my_list)))
#
# #List Sorting
#
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#
# a.sort(key=lambda x: x[1])
# print(a)

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True  # changing this will either run or not run the message_friends function.
# }
#
#
# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         if args[0]["valid"]:
#             return fn(*args, **kwargs)
#     return wrapper
#
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
#
# message_friends(user1)
