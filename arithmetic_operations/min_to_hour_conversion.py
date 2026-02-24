#conversion of min into hours
minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)
#Output 
"""Enter total minutes: 60
Hours: 1
Remaining Minutes: 0"""