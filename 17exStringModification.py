a = 'ajay anand'
b = a.upper()  #lower to upper
print(b)

d ='STEVE ROGERS'
c = d.lower()  #upper to lower
print(c)  

e = ' Winter Soldier '
f = e.strip()  #stripped of the spaces at beginning and end
print(f)

g = 'Mark 2'
h = g.replace('2','85')  #replaced '2' with '85'
print(h)

i = 'James {} Barnes'  #placeholder in between a string
j = 'Bucky'
print(i.format(j))


k = '{} Steven {}'  #placeholder in between a string
l = 'Dr'
m = 'Strange'
print(k.format(l,m))

n = '{} {} Romanoff'
o = 'Natasha'
p = 'Agent'
print(n.format(p,o))

q = '{1} Vengeance, Im {0}, The name is {2}'  #placeholder in between a string using index 
r = 'Im'
s = 'Justice'
t = 'Batman'
print(q.format(s,r,t))



