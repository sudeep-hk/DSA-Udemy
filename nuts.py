match= ['!', '#', '$','%', '&', '*','@', '^', '~']
N=3
nuts=['^', '&', '%']
bolt=['&', '^', '%']

b=0
rank_nut=[]
for i in nuts:
    if i in bolt:
        a=True
    else: 
        b+=1
if b >0:
    print('Not one to one mapped')
else:
    for i in nuts:
        lent=len(match)
        for j in range(lent):
            if i==match[j]:
                rank_nut.append(j)
rank_nut.sort()
for i in rank_nut:
    print (match[i],end=' ')

