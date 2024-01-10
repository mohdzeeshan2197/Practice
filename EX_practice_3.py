#!/usr/bin/env python
# coding: utf-8

# ### Comprehension

# In[1]:


l = [1,2,3,4,45,5]
new_l = []
for i in l:
    new_l.append(i**2)
print(new_l)


# In[2]:


[i**2 for i in l]


# In[3]:


[i for i in l if i % 2 == 0]


# In[4]:


l1 = ['pwskill','sudh','kumar','data science'] 


# In[5]:


[i.upper() for i in l1]


# In[6]:


l


# In[7]:


(i**2 for i in l )


# In[8]:


tuple((i**2 for i in l ))


# In[9]:


list((i**2 for i in l ))


# In[10]:


d = {"key1": 1, "key2": 2, "key3": 3,"key4":4}


# In[11]:


d


# In[12]:


{k:v**2 for k,v in d.items()}


# In[13]:


{k:v for k,v in d.items() if v > 1}


# ### functions

# In[14]:


def test():
    pass


# In[15]:


def test1():
    print("This is my very very first function")


# In[16]:


test1()


# In[17]:


test1 + 'sudh'


# In[18]:


def test2():
    return "This is my very first return"


# In[19]:


test2()


# In[20]:


test2() + ' sudh'


# In[21]:


def test3():
    return 25,45.5,"sudh",[22,33,44,55]


# In[22]:


test3()


# In[23]:


a,b,c,d = test3()


# In[24]:


a


# In[25]:


b


# In[26]:


c


# In[27]:


d


# In[28]:


def test4():
    a = 5*6/7
    return a


# In[29]:


test4()


# In[30]:


def test5(a,b,c):
    cal = (a +b)/c
    return cal


# In[31]:


test5()


# In[ ]:


test5(2,5,8)


# In[32]:


def test6(a,b):
    s = a+b
    return s


# In[33]:


test6(7,8)


# In[34]:


test6('hello',' my friend')


# In[35]:


test6([22,3,5,63,52,4],[54,6,55,44,33])


# In[36]:


l = [2,23,4,3,5,"sudh","kumar",[3,4,5,3],3.4,55.6,45.3]


# In[37]:


l


# In[38]:


def test7(l):
    '''This Function helps you to extract integers and string in seprate list'''
    int_l = []
    str_l = []
    flt_l = []
    for i in l:
        if type(i) == int:
            int_l.append(i)
        elif type(i) == str:
            str_l.append(i)
        elif type(i)== list:
            for j in i:
                if type(j) == int:
                    int_l.append(j)
        elif type(i) == float:
            flt_l.append(i)
    return int_l,str_l,flt_l




# In[39]:


test7(l)


# In[40]:


def test8(*args):
    return args


# In[41]:


test8(2,3,4)


# In[42]:


type(test8())


# In[43]:


test8(3,4,55,[4,5,6,4],'sudh')


# In[44]:


def test9(*zee):
    '''Asterisk(*) only works, we take any name '''
    return zee


# In[45]:


test9(23.3,45,6,7,4,6,4,[3,4,5,'singh'],'hello')


# In[46]:


def test10(*args,a):
    return args, a


# In[47]:


test10(22,23,4,5,6)


# In[48]:


test10(2,3,4,53,a = 36)


# In[49]:


def test11(c,d,a= 25,b = 50):
    return a,b,c,d


# In[50]:


test11()


# In[51]:


test11(3,4)


# In[52]:


test11(c= 33,d= 44, a= 55, b = 66)


# In[53]:


def test12(**kwargs):
    return kwargs


# In[54]:


test12()


# In[55]:


type(test12())


# In[56]:


test12(name = 'sudhanshu', key = 'pair', c = 33, l = ['wow',23,34,'hello'])


# ### Create a function to return a list of odd numbers in the range of 1 to 25.

# In[57]:


def odd_number(start,end):
    return [i for i in range(start,end+1) if i % 2 != 0]


# In[59]:


odd_number(1,20)


# ###  Write a List Comprehension to iterate through the given string: ‘pwskills’.
# #Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[60]:


string = 'pwskills'


# In[61]:


[i for i in string]


# ### Write a python program to check whether a given number is Palindrome or not using a while loop.

# In[63]:


# palindrome number like 121, 141 that are similar after reverse


# In[70]:


def palindrom_checker(n):
    n= str(n)
    reverse_num = n[::-1]
    if reverse_num == n:
        return True
    else:
        return False        


# In[74]:


palindrom_checker(151)


# In[75]:


palindrom_checker(142)


# In[122]:


n = int(input("Enter Number: "))
tem = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n//10
if rev == tem:
    print("It is Palindrome",rev)
else:
    print("Sorry Not a Palindrome")
    
    


# ### Write a code to print odd numbers from 1 to 100 using list comprehension.
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# out odd numbers.

# In[124]:


[i for i in range(1,101)]


# In[125]:


[i for i in range(1,101) if i % 2 != 0]

