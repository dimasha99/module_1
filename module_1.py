grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades0=sum(grades[0])/len(grades[0])
grades1=sum(grades[1])/len(grades[1])
grades2=sum(grades[2])/len(grades[2])
grades3=sum(grades[3])/len(grades[3])
grades4=sum(grades[4])/len(grades[4])
students=list(students)
students=sorted(students)
ball_={students[0]:grades0, students[1]:grades1, students[2]:grades2, students[3]:grades3, students[4]:grades4}
print(ball_)