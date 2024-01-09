#!/usr/bin/env python
# coding: utf-8

# ### While and for Loops

# In[14]:


# summision


# In[16]:


n = int(input("Enter Your Number: "))
s = 0

i = 0
while i <= n:
    s = s+i
    i += 1
print("The Total Sum 0 Till ",n," is: ",s)


# In[17]:


# factorial


# In[47]:


n = int(input("Enter Your Number: "))
i = 1
pro = 1

if n > 0:
    while i <= n:
        pro = pro * i
        i += 1
    print("Factorial of",n,"is: ",pro)
else:
    print("Enter Positive Number Please")
    


# In[53]:


n = int(input("Enter Your Number: "))
pro = 1

if n > 0:
    for i in range(1,n+1):
        pro = pro * i
    print("Factorial of",n,"is: ",pro)
else:
    print("Enter Positive Number Please")


# In[56]:


# Fibonacci Series
# 0 1 1 2 3 5 8 13.........


# In[78]:


n = int(input("Enter Your Number: "))
n= n-2
i = 1
if n > 0:
    a = 0
    b = 1
    print(a)
    print(b)
    while i <= n:
        c = a + b
        a = b
        b = c
        print(c)
        i +=1


# In[77]:


n = int(input("Enter Your Number: "))
n = n-2

if n > 0:
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a +b
        a = b
        b = c
        print(c)
    


# In[79]:


# Reverse a string


# In[93]:


s


# In[94]:


s[::-1]


# In[98]:


s = "This is my strings"

for i in range(len(s)-1,-1,-1):
    print(s[i])


# In[108]:


s


# In[107]:


n = input("Enter Your Words for Reverse: ")
new_s = ''
for i in range((len(n)-1),-1,-1):
    new_s = new_s + n[i]
print(new_s)


# In[11]:


n = input("Enter Your words: ")
l = len(n)-1
new_s = ''
while l >= 0:
    new_s = new_s + n[l]
    l -= 1
print(new_s)


# In[12]:


# Tables


# In[20]:


n = int(input("Enter Table Number: "))

for i in range(1,11):
    p = i * n
    print(n ,'*', i, '=' ,p)


# In[26]:


n  = int(input("Enter Number of Table: "))
i = 1
while i <= 10:
    p = i * n
    print(n ,'*',i,'=',p)
    
    i +=1


# In[27]:


# while and else


# In[29]:


i = 0
n = 5
while i <= n:
    print(i)
    i +=1
else:
    print("This will be executed once when while completed successfully")


# In[32]:


i = 0
n = 5
while i <= n:
    print(i)
    if i == 3:
        break
    i +=1
else:
    print("This is not executed because while loop did not completed succesfully")
    

