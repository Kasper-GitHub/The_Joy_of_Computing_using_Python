str1=input("Enter the first string :\t").lower()
str2=input ("Enter the second string :\t").lower()

if(sorted(str1) == sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")