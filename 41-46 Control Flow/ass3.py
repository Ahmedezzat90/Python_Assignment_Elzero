# قم بعمل Input يقبل منك العمر الخاص بالشخص
# تأكد أن المدخل عبارة عن Integer
# المطلوب طباعة عمرك بالشهور والأسابيع والأيام والساعات والدقائق والثواني
# المطلوب طباعة كل وحدة من وحدات الوقت في سطر منفصل
# يجب التأكد من أن العمر أكبر من 10 وأقل من 100 وفي حالة غير ذلك إطبع رسالة تفيد أن العمر خارج النطاق.
# # Input Example 38

# # Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

age = int(input("Enter your age: ").strip())
if age > 10 and age < 100:
    print(f"Your Age In Months Is {age * 12} Months")
    print(f"Your Age In Weeks Is {age * 52} Weeks")
    print(f"Your Age In Days Is {age * 365} Days")
    print(f"Your Age In Hours Is {age * 365 * 24} Hours")
    print(f"Your Age In Minutes Is {age * 365 * 24 * 60} Minutes")
    print(f"Your Age In Seconds Is {age * 365 * 24 * 60 * 60} Seconds")
else:
    print("Your Age Is Out Of Range")