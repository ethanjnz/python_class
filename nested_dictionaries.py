x = [[5, 2, 3], [10, 8, 9]]

# students = [
#     {"first_name": "Michael", "last_name": "Jordan"},
#     {"first_name": "John", "last_name": "Rosales"},
# ]

# sport_directory = {
#     "basketball": ["kobe", "Jordan", "James", "Curry"],
#     "Soccer": ["Messi", "Ronaldo", "Rooney"],
# }

z = [{"x": 10, "y": 20}]
# 1.----------------------------
# x[1][0] = 15
# print(x)
# 2.----------------------------
# students[0]["last_name"] = "Bryant"
# print(students[0])
# 3.------------------------------
# sport_directory["Soccer"][0] = "Andres"
# print(sport_directory["Soccer"])
# ----------------------------------------------------
# students = [
#     {"first_name": "Michael", "last_name": "Jordan"},
#     {"first_name": "John", "last_name": "Rosales"},
#     {"first_name": "Mark", "last_name": "Guillen"},
#     {"first_name": "KB", "last_name": "Tonel"},
# ]


# def iterate_Dictionary(some_list):
#     for index in some_list:
#         for key, value in index.items():
#             print(key, value)


# iterate_Dictionary(students)


# def iterate_Dictionary2(key_name, some_list):
#     for index in some_list:
#         print(index[key_name])


# iterate_Dictionary2("last_name", students)

# -----------------------------------------------


dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def print_info(dojo):
    num = 0
    for key in dojo:
        print(key.upper())
        for value in dojo[key]:
            print(value)


print_info(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
