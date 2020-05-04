#!/usr/bin/env python
# coding: utf-8

# In[1]:


###task1###ass1
print('mohan')


# In[5]:


#####task1####ass2
x=int(input('enter starting number:'))
y=int(input('enter ending number:'))
z=[]
for i in range( x,y+1):
    if i%7==0 and i%5!=0:
        z.append(i)
        
print(z)       


# In[11]:


####task1##ass3
x=input('enter ur first name:')
y=input('enter ur last name:')
my_name=x+' '+y
print(my_name)
print('reversed my name;',my_name[::-1])
print(' method1------reversed my name ...first surname and second my name....',y+' '+x)
mynameList=my_name.split(' ')
print(' method2------reversed my name ...first surname and second my name....',mynameList[1]+' '+mynameList[0])


# In[12]:


pi=22/7
rad = float(input('Radius of sphere: '))
volume = (4/3) * (pi * rad ** 3)
print("Volume of sphere: ", volume)


# In[16]:


x=[int(each) for each in input('enter comma separated values:').split(',')]
print(x)


# In[20]:


num=int(input('enter a number:'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print('*',end=' ' )
    print()
for a in range(1,num+1):
    for k in range(1,num+1-a):
        print('*',end=' ')
    print()
    


# In[21]:


x=input('enter ur name:')
print('reversed my name;',x[::-1])


# In[22]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


# In[ ]:




