a=input()
count=0
n=len(a)
for ch in a:
    if ch in "aeiouAEIOU":
        print(ch,"It is a vowel")
        count+=1;
    else:
        print(ch,"It is not a vowel")

print(count,"total vowels")