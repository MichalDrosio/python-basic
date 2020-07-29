us = ['ola', 'magda', 'michal']
conf_us= ['1','2','3']
l =[]
while us or conf_us:
    if len(us) != 0:
        l.append(us[0])
        us.pop(0)
    if len(conf_us) != 0:
        l.append(conf_us[0])
        conf_us.pop(0)

print(l)

li1 = ['ola', 'magda', 'michal']
li2= ['1','2','3']
li3 =[]
while li1:
    dana = li1.pop(-1)
    li3.append(dana)
    while li2:
        dana2 = li2.pop(-1)
        li3.append(dana2)
        break
print(li3)


