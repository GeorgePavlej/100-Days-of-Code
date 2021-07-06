# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(numbers)
# print(new_numbers)

# range_list = [num*2 for num in range(1,5)]
# print(range_list)

# for num in range(1,5):
#     num *= 2
#     print(num)

import random

names = ["Alex", "George", "Viktoria", "Karoline", "Beth"]
student_score = {students:random.randint(1,100) for students in names}
print(student_score)

passed_students = {students:score for (students, score) in student_score.items() if score >= 30}
print(passed_students)


