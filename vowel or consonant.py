A=input("Enter any Letter= ").lower()
if A.isalpha():
    if A in 'aeiou':
        print("vowels")
    else:
        print("consonant")
else:
    print("neither digits or special Characters")