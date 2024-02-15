import re

# The search() function searches the string for a match, and returns a Match object if there is a match.

txt="Steve Rogers is Captain America"
x=re.search("^Steve.*America$",txt)  #Check if the string starts with "The" and ends with "Spain":

if x:
    print("We have a Match")
else:
    print("We don't have a Match")

# The findall() function returns a list containing all matches.

y=re.findall("[a,m]",txt)  #Find all lower case characters alphabetically between "a" and "m":
print(y)

txt1="Iron Man's latest armour is Mark 44"
z=re.findall("\d",txt1)  #Find all digit characters:
print(z)

a=re.findall("latest|oldest",txt1)  #Check if the string contains either "falls" or "stays":
print(a)

if a:
    print("Correct")
else:
    print("Not Correct")

b=re.findall("\D",txt1)  #Return a match at every no-digit character:
print(b)

if b:
    print("Correct")
else:
    print("Not Correct")

c=re.findall("\s",txt1)  #Return a match at every white-space character:
print(c)

if c:
    print("Correct")
else:
    print("Not Correct")

d=re.findall("\S",txt1)  #Return a match at every NON white-space character:
print(d)

if d:
    print("Correct")
else:
    print("Not Correct")

e=re.findall("\w",txt1)  #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
print(e)

if e:
    print("Correct")
else:
    print("Not Correct")

f=re.findall("\W",txt1)  #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
print(f)

if f:
    print("Correct")
else:
    print("Not Correct")

g=re.findall("\AIron",txt1)  #Check if the string starts with "Iron":
print(g)

if g:
    print("Correct")
else:
    print("Not Correct")

h=re.findall("[a-n]",txt1)  #Check if the string has any characters between a and n:
print(h)

if h:
    print("Correct")
else:
    print("Not Correct")

i=re.findall("[a,r,n]",txt1)  #Check if the string has any a, r, or n characters:
print(i)

if i:
    print("Correct")
else:
    print("Not Correct")

j=re.findall("[^a,r,n]",txt1)  #Check if the string has other characters than a, r, or n:
print(j)

if j:
    print("Correct")
else:
    print("Not Correct")

k=re.findall("[0,1,2,3,4,5]",txt1)  #Check if the string has any 0, 1, 2, 3, 4 or 5 digits:
print(k)

if k:
    print("Correct")
else:
    print("Not Correct")

l=re.findall("[0-9]",txt1)  #Check if the string has any digits:
print(l)

if l:
    print("Correct")
else:
    print("Not Correct")

m=re.findall("[0-5][0-9]",txt1)  #Check if the string has any two-digit numbers, from 00 to 59:
print(m)

if m:
    print("Correct")
else:
    print("Not Correct")

n=re.findall("[a-zA-Z]",txt1)  #Check if the string has any characters from a to z lower case, and A to Z upper case:
print(n)

if n:
    print("Correct")
else:
    print("Not Correct")

# The split() function returns a list where the string has been split at each match:

o=re.split("\s",txt1)  #Split the string at every white-space character:
print(o)

p=re.split("\s",txt1,1)  #Split the string at the first white-space character:
print(p)

# The sub() function replaces the matches with the text of your choice:

q=re.sub("\s","9",txt1)  #Replace all white-space characters with the digit "9":
print(q)

