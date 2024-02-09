# قم بإضافة إسم من أصدقائك للقائمة في أول القائمة أولا ثم قم بإضافة إسم آخر في نهاية القائمة

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


friends.insert(0, "Nasser")
friends.append("Salem")

print(friends)