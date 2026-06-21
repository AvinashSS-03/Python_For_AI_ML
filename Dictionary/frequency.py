#this program is used to find the frequency of the list

n = [1, 2, 3, 2, 1, 1, 4]
freq={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)