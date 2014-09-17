def Lfindwhile (Shahruzisterrible,duh):
    pos=0
    while pos<len(Shahruzisterrible):
        if duh==Shahruzisterrible[pos]:
            return pos
        pos+=1
    return -1 
##print Lfindwhile([1,2,3,4,5],3)
##print Lfindwhile([1,2,3],'shahruz')

def Lfindnowhile (L,Ele):
    
    if Ele not in L:
        return -1
    else:
        return L.index(Ele)
print Lfindnowhile([1,2,3,4,5],3)
print Lfindnowhile([1,2,3],'shahruz')
