# enter yor age type integer and check if up of 16 or not 

Age = int(input("Enter Your Age: "))

if(Age < 16):
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You") # If Age < 16
else:
    print(f"Hello Your Age Is {Age} If Larger Than 16 , All Articles Is Suitable For You") # If Age Is 16+