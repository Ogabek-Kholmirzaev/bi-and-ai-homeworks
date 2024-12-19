txt = input()

done = "aeiouAEIOU"
cnt = 0
ans = []

for i in range(len(txt)):
    cnt += 1
    ans.append(txt[i])

    if i != len(txt) - 1 and cnt >= 3 and txt[i] not in done:
        done += txt[i]
        ans.append("_")
        cnt = 0

print(''.join(ans))