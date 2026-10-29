print("STUDENT PERFORMANCE PREDICTOR")

attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter study hours per day: "))
assignment = float(input("Enter assignment mark: "))
internal = float(input("Enter internal mark: "))

score = (attendance + assignment + internal) / 3

if score >= 85 and study_hours >= 3:
    performance = "Excellent"
elif score >= 70:
    performance = "Good"
elif score >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("\nPredicted Performance:", performance)
