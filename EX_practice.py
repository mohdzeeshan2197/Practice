#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+1


# In[2]:


print("Hello World")


# In[3]:


print("This is My First Class")


# In[4]:


print("this is PWskill Class of data Science")


# In[5]:


a = 10


# In[6]:


sudh = 20


# In[7]:


a+sudh


# In[8]:


type(a)


# In[9]:


type(sudh)


# In[10]:


b = 10.3


# In[11]:


type(b)


# In[12]:


n = True    # value 1


# In[13]:


type(n)


# In[14]:


name = 'Zeeshan'


# In[15]:


type(name)


# In[16]:


n


# In[17]:


m = False     # value 0


# In[18]:


m


# In[19]:


type(m)


# In[20]:


n+m


# In[21]:


n-m


# In[22]:


n/m     #   1 / 0 ---- infinity  core python gives error division by zero but numpy gives infinity


# In[23]:


#  Complex Number

c = 2 + 4j


# In[24]:


type(c)


# In[25]:


c.imag


# In[26]:


c.real


# In[27]:


c.conjugate()


# In[28]:


s = 'pwskills'


# In[29]:


print(s)
type(s)


# In[30]:


s


# In[31]:


s[0]


# In[32]:


s[1]


# In[33]:


s[1:4]


# In[34]:


s[::-1]


# In[35]:


s[0:4]


# In[36]:


s[0::2]


# In[37]:


s


# In[38]:


s


# In[39]:


s[0:900]


# In[40]:


s[:-900:-1]


# In[41]:


c = 200


# In[42]:


s1 = "this is my string class"


# In[43]:


s1


# In[44]:


len(s1)


# In[45]:


s1.find('s')


# In[46]:


s1.find('i')


# In[47]:


s1.find('is')


# In[48]:


s1.capitalize()


# In[49]:


s1.endswith('d')


# In[50]:


s1.count('s')


# In[51]:


s1.count('st')


# In[52]:


s1.count('z')


# In[53]:


s1.upper()


# In[54]:


s1.lower()


# In[55]:


s1.title()


# In[56]:


s1.capitalize()


# In[57]:


s1


# In[58]:


s2 = 'and it is very beneficial'


# In[59]:


s1 +3


# In[60]:


s1+ str(23)


# In[61]:


s1 + " and it is Good class"


# In[62]:


s1*3


# In[63]:


l = [ 23,55,65,78.9, 'Sudh', 5+7j,True]


# In[64]:


l


# In[65]:


type(l)


# In[66]:


l[0:6]


# In[67]:


l[4]


# In[68]:


l[4][2]


# In[69]:


l[4][2:4]


# In[70]:


l[::-1]


# In[71]:


l[-6:-1]


# In[72]:


l


# In[73]:


l[::2]


# In[74]:


s


# In[75]:


l +s


# In[76]:


l+list(s)


# In[77]:


l.append(s)


# In[78]:


l


# In[79]:


type(l[6])


# In[80]:


l[6]


# In[81]:


str(l[6])[0:2]


# In[82]:


l


# In[83]:


l1 = [3,4,5]


# In[84]:


l+l1


# In[85]:


l1 *3


# In[86]:


len(l)


# In[87]:


len(l1)


# In[88]:


l1


# In[89]:


l1.append(99)


# In[90]:


l1


# In[91]:


len(l1)


# In[92]:


s


# In[93]:


l1.append(s)


# In[94]:


l1


# In[95]:


len(l1)


# In[96]:


l1


# In[97]:


l


# In[98]:


l1.append(l)


# In[99]:


l1


# In[100]:


l1[-1][-1][1:3]


# In[101]:


l1


# In[102]:


l1.extend(23)


# In[103]:


l1.extend('Aman')


# In[104]:


l1


# In[105]:


l1.extend([1,2,3])


# In[106]:


l1


# In[107]:


l


# In[108]:


l.insert(0,9)


# In[109]:


l


# In[110]:


l3= [7,8,9]


# In[111]:


l


# In[112]:


l.insert(2,l3)


# In[113]:


l


# In[114]:


l.insert(-1,99)


# In[115]:


l


# In[116]:


l.pop()


# In[117]:


l


# In[118]:


l.pop()


# In[119]:


l.pop()


# In[120]:


l


# In[121]:


l.pop(1)


# In[122]:


l


# In[123]:


l.remove(9)


# In[124]:


l


# In[125]:


l.remove(5+7j)


# In[126]:


l


# In[127]:


l.remove(l[0][1])


# In[128]:


l[0].remove(8)


# In[129]:


l


# In[130]:


l.reverse()


# In[131]:


l


# In[132]:


l.sort()


# In[133]:


l4= [3,5,2,6,23,1,5]


# In[134]:


l4.sort()


# In[135]:


l4


# In[136]:


l4.sort(reverse= True)


# In[137]:


l4


# In[138]:


l3 = ['khan','faranhiet','kumar sanu','data science']


# In[139]:


l3.sort()


# In[140]:


l3


# In[141]:


l3.count('khan')


# In[142]:


len(l3)


# In[143]:


l3


# In[144]:


l3.index('khan')


# In[145]:


s


# In[146]:


s[0] = 'a'


# In[147]:


l


# In[148]:


l[1] = 100


# In[149]:


l


# In[150]:


s


# In[151]:


s.replace('p','Z')


# In[152]:


s


# In[153]:


t= (2,3,4,5,78+8j,True,[5,6,7],'Sudh')


# In[154]:


t


# In[155]:


type(t)


# In[156]:


len(t)


# In[157]:


t[2]


# In[158]:


t[6][2]


# In[159]:


t


# In[160]:


t.count('Sudh')


# In[161]:


t[::-1]


# In[162]:


t.index([5,6,7])


# In[163]:


t


# In[164]:


t[0] = 33


# In[165]:


t[::-1]


# In[166]:


t


# In[167]:


s= {}


# In[168]:


type(s)


# In[169]:


s= {2,4,5,6,'sudh',78.9,9+8j}


# In[170]:


type(s)


# In[171]:


s


# In[172]:


len(s)


# In[173]:


s1 = {1,1,1,1,3,3,3,3,4,9,5,5,5,5,5,6,0,6,6,6,7,7,9}


# In[174]:


s1        #only gives unique values


# In[175]:


l6 = [1,1,1,1,3,3,3,3,4,9,5,5,5,5,5,6,0,6,6,6,7,7,9]


# In[176]:


l6


# In[177]:


l6 = list(set(l6))


# In[178]:


l6


# In[179]:


s[0]


# In[180]:


s[::-1]


# In[181]:


s


# In[182]:


s.add(55)


# In[183]:


s.add(55)


# In[184]:


s


# In[185]:


s.remove(2)


# In[186]:


s


# In[ ]:





# In[187]:


d = {}


# In[188]:


type(d)


# In[189]:


d = {'key': 'pair'}


# In[190]:


d


# In[191]:


d = {'name':'Zeeshan','Age': 25,'mobile':999888222,}


# In[192]:


d


# In[193]:


d1 ={'Name':'Sudhanshu','Email':'ss@gmail.com','@hello':'This is my Line','_welcome':'In india',454:'This is number',True:'Boolean Value'}


# In[194]:


d1


# In[195]:


d1['Name']


# In[196]:


d1['Email']


# In[197]:


d1[1]      # 1 or True Same 


# In[198]:


d1 ={'Name':'Sudhanshu','Email':'ss@gmail.com','@hello':'This is my Line','_welcome':'In india',454:'This is number',True:'Boolean Value','Name':'Sudh'}


# In[199]:


d1


# In[200]:


d2 = {'Company': 'Pwskills','Courses':['Web Developement','Data Science Masters','Java'],}


# In[201]:


d2


# In[202]:


d2['Courses'][1]


# In[203]:


len(d2)


# In[204]:


d3 = {'Number': [2,2,3,3,2],'Assignments':(1,2,3,4,5,6),'Date':{22,34,12}}


# In[205]:


d3


# In[206]:


d4 = {'Number': [2,2,3,3,2],'Assignments':(1,2,3,4,5,6),'Date':{22,34,12},'course': {'Web Developement':6,'Data Science Masters':7,'Java':8,}}


# In[207]:


d4


# In[208]:


d4['course']['Java']


# In[209]:


d4['Mentor'] = ['Sudhanshu','Krish','gagan']


# In[210]:


d4


# In[211]:


del d4['Number']


# In[212]:


d4


# In[213]:


d4.keys()


# In[214]:


d4.values()


# In[215]:


list(d4.keys())


# In[216]:


list(d4.values())


# In[217]:


list(d4.items())


# In[227]:


d4.pop('Assignments')


# In[228]:


d4


# In[229]:


marks = int(input("Enter Your Marks "))

if marks >= 80:
    print('You are with the A0 Batch')
elif marks >= 60 and marks < 80:
    print("You are with the A1 Batch")
elif marks >= 40 and marks < 60:
    print("You are with A Batch")
else:
    print("You are Start With Basics")

    


# In[230]:


price = int(input("Enter Your Price Please: "))


if price >= 1000:
    print("I will not Purchase")
else:
    print("I will Purchase")


# In[231]:


price = int(input("Enter your Price: "))
if price > 1000:
    print("I will not Purchase")
    if price >= 5000:
        print("Because It is Very Expensive")
else:
    print("I will Purchase")


# In[232]:


l = [2,3,4,5,6,7,8]


# In[233]:


l


# In[234]:


l[0]+1


# In[235]:


l
new_l = []
for i in l:
    new_l.append(i+1)
print(new_l)


# In[236]:


l


# In[237]:


for i in l:
    print(i+1)


# In[238]:


k = ['sudh','kumar','sanjeev','kelash']


# In[239]:


k


# In[240]:


k[0].upper()


# In[241]:


new_k = []
for i in k:
    new_k.append(i.upper())
new_k


# In[242]:


l = ['words', 343,'Name',868,'Noun',45,'malaya',33,86.45]


# In[243]:


l


# In[244]:


type(l[1])


# In[245]:


type(l[0])


# In[246]:


print("This is Given List ",l)
l_int = []
l_str = []

for i in l:
    if type(i) == int or type(i) == float:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
print(l_int)
print(l_str)


# In[247]:


l = ['Krish','Naik','Sudhanshu','Kumar']


# In[248]:


l


# In[249]:


for i in l:
    print(i)


# In[250]:


for i in l:
    print(i)
else:
    print("This else will be executed when your 'for loop' completed itself")


# In[251]:


l


# In[252]:


for i in l:
    if i == 'Naik':
        break
    print(i)


# In[253]:


l


# In[254]:


for i in l:
    if i == 'Sudhanshu':
        break
    print(i)
else:
    print("This else statement is only Executed when for loop completed itself")


# In[255]:


for i in l :
    if i == 'Hello':
        break
    print(i)
else:
    print("Now it is executed")


# In[256]:


l


# In[257]:


for i in l:
    if i == "Naik":
        continue
    print(i)


# In[258]:


for i in l:
    if i == "Sudhanshu":
        continue
    print(i)
else:
    print("Else executed")


# In[259]:


range(5)


# In[260]:


list(range(5))


# In[261]:


list(range(0,20,2))


# In[262]:


list(range(-20,0,2))


# In[263]:


l


# In[264]:


len(l)-1


# In[265]:


range(len(l)-1, 0)


# In[266]:


list(range(len(l)-1,-1,-1))


# In[267]:


l_arrange = []
for i in range(len(l)-1,-1,-1):
    l_arrange.append(l[i])
print(l_arrange)


# In[268]:


l2 = [22,3,4,3,5,6,677,4,99,3,6,7,7,43,54,56,67,55,665,7]


# In[269]:


l2


# In[270]:


len(l2)


# In[271]:


for i in range(len(l2)):
    if i % 2 == 0 :
        print(l2[i])


# In[272]:


for i in range(0,len(l2),2):
    print(l2[i])


# In[273]:


k = [1,2,3,4,5,6,7,8,98]
len(k)


# In[274]:


submission = 0
for i in range(len(k)):
    submission = submission+ k[i]
print(submission)


# In[275]:


sum(k)


# In[276]:


t = (1,2,3,4,56,5,4,4)


# In[277]:


for i in t :
    print(i)


# In[278]:


s= {1,2,3,4,5,6,6,'sudh','hello'}


# In[279]:


s


# In[280]:


for i in s :
    print(i)


# In[281]:


st = 'String Class'


# In[282]:


for i in st:
    print(i)


# In[283]:


d = {"Name":"Sudh",'Class':"Data Science","Topics": ["Python","Stats","Machine Learning","DL","CV","NLP"]}


# In[284]:


d


# In[285]:


d.keys()


# In[286]:


for i in d.keys():
    print(d[i])


# In[287]:


for i in d.values():
    print(i)


# In[288]:


for i in d.items():
    print(i)


# In[289]:


su = 0
pro = 1
for i in range(1,21):
    su = su+i
    pro = pro * i
print("The sum of first 20 elements is: ",su)
print("The product of 20 elements is: ",pro)    


# In[290]:


sum(range(1,21))


# In[291]:


list(range(1,21))


# In[292]:


p = 1
s = 0
i = 1
while i <= 20:
    p = p * i
    s = s + i
    i += 1
print(p)
print(s)


# Q3. Create a python program to compute the electricity bill for a household.
# 
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.

# In[293]:


'''
first 100 unit  ====    4.5
next 100 unit   ====    6
next 100 unit   ====    10
after 300 unit  ====    20
'''


# In[294]:


unit = int(input("Enter Electricity Unit: "))
if unit <= 100:
    bill = 4.5 * unit
    print('Bill: ',bill)
elif unit > 100 and unit <= 200:
    remain = unit - 100
    re_unit = remain * 6
    bill = (re_unit+ 4.5 *100)
    print("Bill: ",bill)
elif unit > 200 and unit <= 300:
    remain = unit - 200
    re_unit = remain * 10
    bill = (100*4.5) + (100*6) + (re_unit)
    print("Bill: ",bill)
elif unit > 300:
    remain = unit - 300
    re_unit = remain * 20
    bill = (100 * 4.5) + (100 * 6) + (100 * 10) + (re_unit)
    print("Bill: ",bill)

    


# In[295]:


divisible = []
for i in range(1,101):
    i = i*i*i
    if i % 4 == 0 or i % 5 == 0:
        divisible.append(i)
print(divisible)


# In[296]:


di = []
i = 1
while i <= 100:
    c = i*i*i
    if c % 4 ==0 or c % 5 == 0:
        di.append(c)
    i +=1    
print(di)


# In[297]:


string = "I want to become a data scientist"


# In[298]:


string.lower()


# In[299]:


v =['a','e','i','o','u']


# In[300]:


c = 0
for i in string:
    for j in v:
        if i == j:
            c += 1
print(c)

