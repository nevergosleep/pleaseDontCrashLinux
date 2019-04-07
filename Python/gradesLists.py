last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

# Add entries to the end of a list
subjects.append("computer science")
grades.append(100)

# Combine two lists
gradebook = list(zip(subjects, grades))

# Add a list entry to a list of lists
gradebook.append(["visual arts", 93])

print(gradebook)

# Add two lists together
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
