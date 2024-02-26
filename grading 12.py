score = []
for i in range(1, 5):
    marks = int(input(f"Enter marks for subject {i}: "))
    score.append(marks)

grading_scale = {
    "A+": (90, 100),
    "A": (80, 89),
    "B+": (70, 79),
    "B": (60, 69),
    "C": (50, 59),
    "F": (0, 49)
}

average_percentage = (sum(score) / len(score)) * 100

if average_percentage > 90:
    print("Overall Grade: A+")
elif 80 <= average_percentage <= 89:
    print("Overall Grade: A")
elif 70 <= average_percentage <= 79:
    print("Overall Grade: B+")
elif 60 <= average_percentage <= 69:
    print("Overall Grade: B")
elif 50 <= average_percentage <= 59:
    print("Overall Grade: C")
else:
    print("Overall Grade: F")
    