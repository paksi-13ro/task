grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(list(students))
average_score = [sum(sublist) / len(sublist) for sublist in grades]
student_grades = {key: average_score[i] if i < len(average_score) else default_value for i, key in enumerate(sorted_students)}
print(student_grades)