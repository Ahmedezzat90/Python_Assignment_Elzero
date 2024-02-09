# print the first input in submain in the last element in the main list (the submain is in the end of list)
# print the last input in submain in the first element in the main list (the submain is in the end of list)
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web

print(technologies[-1][0])
print(technologies[-1][-1])