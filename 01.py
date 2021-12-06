text = text.splitlines()
greater = 0
for i in range(len(text)-1):
    if int(text[i+1])>int(text[i]):
        greater+=1
print(greater)
greater = 0
for i in range(len(text)-3):
    if int(text[i+1])+int(text[i+2])+int(text[i+3])>int(text[i])+int(text[i+1])+int(text[i+2]):
        greater+=1
print(greater)