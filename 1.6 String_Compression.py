s="abcdefaaag"
snew=""
count=1
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        count+=1
    elif(s[i]!=s[i+1]):
        snew+=s[i]+str(count)
        count=1
    if(i==len(s)-2):
        snew+=s[i+1]+str(count)
        
if(len(s)<len(snew)):
    print(s)
else: 
    print(snew)
