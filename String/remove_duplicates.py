a=input()
ans=""
for ch in a:
    if ch not in ans:
        ans+=ch
print(ans)