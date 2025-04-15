# Nesting   dictionaries having list values and dictionaries values inside a dictionaries for storing complex data in a simple way
dict_val = {
    "name" : ["apple" , "mango" , "grapes"],
    "age" : 24,
    "education" : {"school" : "abc",
                   "college" : "xyz"} 
}

# print(dict_val["name"][1]) to get list values from the dict , same use key and use index for specific vslue from the list
# print(dict_val['education']["school"])  to get dict values you need to use the key for to calling the value

# dict_val[1] = 4
# print(dict_val)    to add a key and value pair in the dict , thids is one way to do
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s
# how to loop dictionaries 
# for key in dict_val:   
#     print(key)
#     print(dict_val[key]) 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# to edit the value in the dict
# dict_val["age"] = 23
# print(dict_val)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key in student_scores:
    
#     if student_scores[key] > 90:
#         student_grades.update({key : "Outstanding"})
#     elif student_scores[key] > 80 and student_scores[key] < 91:
#         student_grades.update({key : "Exceeds Expectations"})
#     elif student_scores[key] > 70 and student_scores[key] < 81:
#         student_grades.update({key : "Acceptable"})
#     elif student_scores[key] <= 70:
#         student_grades.update({key : "Fail"})

# print(student_grades)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
