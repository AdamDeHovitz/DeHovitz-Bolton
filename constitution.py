#! /usr/bin/python
import cgi
import cgitb; cgitb.enable()

HTML_head='Content-type: text/html\n\n'
top='''
<html><head>
<title>Constituional!</title>
</head>
<body style="background-color:#E68080">
'''
bottom='</body></html>'
bad_input='''
<center><b>We were unable to work with the information provided<p>
Please go back and refill the form</b></center>'''

def main():
    print HTML_head
    print top
    elements=cgi.FieldStorage()
    keys=elements.keys()
##    for akey in keys:
##        print akey + ' = ' + elements[akey].value + '<br>'
    checked=0
    Dict={'one':[],'two':[]}
    one=1
    two=2
    if elements.has_key('iran'):
        Dict['one'].append('Iranian constitution')
        a=open('Iran.txt')
        iran=a.read()
        iran=iran.lower()
        iran=iran.split()
        Dict['one'].append(iran)
        
        checked+=1
    if elements.has_key('usa'):
        b=open('unitedstates.txt')
        usaw=b.read()
        usaw=usaw.lower()
        usaw=usaw.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("USA's constitution")
            Dict['one'].append(usaw)
        else:
            Dict['two'].append("USA's constitution")
            Dict['two'].append(usaw)
       
    if elements.has_key('seventeen'):
        c=open('1791France.txt')
        revolution=c.read()
        revolution=revolution.lower()
        revolution=revolution.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("French constitution of 1791")
            Dict['one'].append(revolution)
        else:
            Dict['two'].append("French constitution of 1791")
            Dict['two'].append(revolution)
            
    if elements.has_key('Russia'):
        d=open('russia.txt')
        rus=d.read()
        rus=rus.lower()
        rus=rus.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("Russian Federation' constitution")
            Dict['one'].append(rus)
        else:
            Dict['two'].append("Russian Federation' constitution")
            Dict['two'].append(rus)
        
    if elements.has_key('ussr'):
        e=open('USSR.txt')
        ussr=e.read()
        ussr=ussr.lower()
        ussr=ussr.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("Union of Soviet Socialist Republic's constitution")
            Dict['one'].append(ussr)
        else:
            Dict['two'].append("Union of Soviet Socialist Republic's constitution")
            Dict['two'].append(ussr)
        
    if elements.has_key('france'):
        f=open('France.txt')
        france=f.read()
        france=france.lower()
        france=france.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("French constitution")
            Dict['one'].append(france)
        else:
            Dict['two'].append("French constitution")
            Dict['two'].append(france)
            
    if elements.has_key('manifesto'):
        g=open('manifesto.txt')
        manifesto=g.read()
        manifesto=manifesto.lower()
        manifesto=manifesto.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("Communist Manifesto")
            Dict['one'].append(manifesto)
        else:
            Dict['two'].append("Communist Manifesto")
            Dict['two'].append(manifesto)
            
    if elements.has_key('magna'):
        h=open('Magnacarta.txt')
        magna=h.read()
        magna=magna.lower()
        magna=magna.split()
        checked+=1
        if Dict['one']==[]:
            Dict['one'].append("Magna Carta")
            Dict['one'].append(magna)
        else:
            Dict['two'].append("Magna Carta")
            Dict['two'].append(magna)
    checker=0     
    if checked!=2:
        print '<br><center><font size="10"> <b> I said two gosh darn it!<br> </b> <font size="7"> <a href="constitutionoptions.html">Go back</a>'
        return bottom
    10
    print '<br><center> You have chosen to compare the '+Dict['one'][0]+' with the '+Dict['two'][0]
    if elements.has_key('yestopwords'):
        checker+=1
        print  '<br><br><b><font size="5">Top ' +elements['topwords'].value+' Words</font><br><br>'
        print Dict['one'][0]+':</b><br>'
        top50(Dict['one'][1],elements['topwords'].value)
        print '<br><br><b>'+Dict['two'][0]+':</b><br>'
        top50(Dict['two'][1],elements['topwords'].value)
    if elements.has_key('total'):
        checker+=1
        print '<br> <br><b><font size="5">Total Words</font></b><br><br>'
        print Dict['one'][0]+': '+str(len(Dict['one'][1])) +'<br>'
        print Dict['two'][0]+': '+str(len(Dict['two'][1]))
    uniqueone=[]
    uniquetwo=[]
    for x in Dict['one'][1]:
        if x not in uniqueone:
            uniqueone.append(x)
    for x in Dict['two'][1]:
        if x not in uniquetwo:
            uniquetwo.append(x)
    if elements.has_key('unique'):
        checker+=1
        print '<br> <br><b><font size="5">Total Unique Words</font></b><br><br>'
        print Dict['one'][0]+': '+str(len(uniqueone)) +'<br>'
        print Dict['two'][0]+': '+str(len(uniquetwo))
    if elements.has_key('percentage'):
        checker+=1
        print '<br> <br><b><font size="5">Percentage of Unique Words</font></b><br><br>'
        print Dict['one'][0]+': '+str(float(len(uniqueone))/len(Dict['one'][1])*100) +'%<br>'
        print Dict['two'][0]+': '+str(float(len(uniquetwo))/len(Dict['two'][1])*100) +'%'
    if elements.has_key('common'):
        checker+=1
        print '<br> <br><b><font size="5">All Common Words</font></b><br><br>'
        new=[]
        for x in uniqueone:
             if x in uniquetwo:
                 new.append(x)
        print 'There are '+ str(len(new))+" common words and they are:<br>"
        r=0
        new.sort()
        
        for word in new:
            print word+'  '
            r+=1
            if r==6:
                print '<br>'
                
                r=0
    if elements.has_key('letters'):
        checker+=1
        print '<br> <br><b><font size="5">Total number of letters</font></b><br><br>'
        print Dict['one'][0]+': '
        letters(Dict['one'])
        print "<br>"+ Dict['two'][0]+": "
        letters(Dict['two'])
    if elements.has_key('wordlength'):
        checker+=1
        print '<br> <br><b><font size="5">Average word length</font></b><br><br>'
        print Dict['one'][0]+': '
        letters(Dict['one'])
        print "<br>"+ Dict['two'][0]+": "
        letters(Dict['two'])   
    if checker==0:
        print '<br><br><br><font size="5"> <b> But you forgot to check off actions to take!</b>'
        print '<br>  <a href="constitutionoptions.html">Go back!</a>'
        return bottom
    print '<br><br> <br> <b> Resources</b><br> All constitutions taken from <a href="http://www.constitution.org/cons/natlcons.htm">here</a>'
    print '<br> manifesto taken from <a href="http://www.gutenberg.org/ebooks/61"> here</a>'
    print '<br> French constitution of 1791 taken from <a href="http://ic.ucsc.edu/~traugott/hist171/readings/1791-09ConstitutionOf1791"> here</a>'
    print '<br> and Magna Carta taken from <a href="http://www.constitution.org/eng/magnacar.htm"> here</a>'
def top50(filen,number):
    
    
    cm=filen
    d={}
    x=0

    while x<len(cm):
        cm[x]=cm[x].strip(".,?[]!();:-")
        x+=1

    for x in cm:
        if x in d:
            d[x]+=1
        else:
            d[x]=1

    x=sorted(d.values())
    x=x[::-1]
    y=0
    n=0
    
    dr=0
    while y<int(number):
        for w in d:
            if y!=n:
                n+=1
                dr+=1
                if dr==4:
                    dr=0
                    print '<br>'
            
            if d[w]==x[y]: 
                print str(y+1)+') '+w+': '+str(x[y])
                
                y+=1
def letters(x):
    constitution=x[1]
##    constitution.split()
    d=[]
    for word in constitution:
        for l in word:
            d.append(l)
    
    print len(d)

main()
print bottom
