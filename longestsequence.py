n=int(input())
songs=list(map(int,input().split()))
dic={}
maxi=0
i=0
j=0
while j<len(songs):
    if songs[j] in dic and dic[songs[j]]>=i:
        i=dic[songs[j]]+1
    maxi=max(maxi,j-i+1)
    dic[songs[j]]=j
    j+=1
print(maxi)

