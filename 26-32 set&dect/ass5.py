# do dictionary and update it and print all elements 

# Needed Output
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"


# Create Dictionary
skills = {"HTML": 90, "CSS": 80, "Python": 30}

all=skills.keys()

for i in all:
    print(i+" Progress Is "+str(skills[i])+"%")



# Print each skill with its percentage

# print("HTML Progress Is " + str(skills["HTML"]) + "%")
# print("CSS Progress Is " + str(skills["CSS"]) + "%")
# print("Python Progress Is " + str(skills["Python"]) + "%")

# Add a new skill to the dictionary
skills["AI"] = 20

# Print the new skill with its percentage
print("AI Progress Is " + str(skills["AI"]) + "%")
