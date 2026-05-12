import matplotlib.pyplot as plt

students_name =["Shardul","Sharali","Shayna","Siddhartha","Sharol","Vedanshi","Vivian","Shingini"]
students_marks = [35,60,20,45,25,40,25,40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Student's Perecentage Graph")
    plt.xlabel("Student's Names")
    plt.ylabel("Student's Percentage")
    plt.show()

percentage_bar_chart()