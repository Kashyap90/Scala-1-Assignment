
# coding: utf-8

# In[1]:


# Task2:

#1.Given a list of strings - List[String] (“alpha”, “gamma”, “omega”, “zeta”, “beta”)
#- find count of all strings with length 4.


# In[2]:


a = ['alpha', 'gamma', 'omega', 'zeta', 'beta']
print(a)


# In[3]:


# Count of all strings with length 4

count=0
for item in a:
    if(len(item)==4):
        count=count+1
        
print("string with length 4 is {}".format(count))


# In[4]:


# 2. convert the list of string to a list of integers, where each string is mapped to its corresponding length:

a_len=[]
for item in a:
    a_len.append(len(item))
    
print("List corresponding to a is: {}".format(a_len))


# In[5]:


# 3.Find count of all strings which contain alphabet ‘m’.

count=0
for item in a:
    for index in range(0,len(item)):
        if(item[index]=='m'):
            count=count+1
            break
            
print("Count of all strings which contain alphabet 'm' is: {}".format(count))


# In[6]:


# 4.Find the count of all strings which start with the alphabet ‘a’.

count=0
for item in a:
    if(item[0]=='a'):
        count=count+1
        break
        
print("Count of all strings which start with the alphabet 'a' is: {}".format(count))


# In[7]:


# Task 3:

# Create a scala application to find the GCD of two numbers.


# In[8]:


# Firstly two find GCD of two numbers:

number1= int(input(" Enter the first number "))
number2= int(input(" Enter the second number "))
smallest= number2 if(number1> number2) else number1

# candidate_gcd=[i for i in range(1,smallest+1)]

while(smallest>=1):
    if(number1% smallest==0 and number2% smallest==0):
        print("GCD of {} and {} is {}".format(number1,number2,smallest))
        break
    smallest=smallest-1
    
# candidate_gcd       

