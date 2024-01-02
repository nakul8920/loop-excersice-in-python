#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q.1)To display the Factorial of a number.
n = int(input("enter the number="))
sum = 0
while(n!=0):
    sum = sum+n
    n = n-1
print("factorial of your number is=",sum)


# In[9]:


#Q.2)To reverse a word.
word = input("enter the word=")
reversed_word = word[::-1]
print(reversed_word)


# In[11]:


#Q.3) To reverse a number.
number = int(input("enter a number="))
reversed_number = int(str(number)[::-1])
print(reversed_number)


# In[12]:


#Q.4)To print n natural number in descending order using a while loop.
n = int(input("enter the number="))
while(n>=0):
    print(n)
    n = n-1


# In[16]:


#Q.5)To display the first 7 multiples of 7.
for x in range(1,8):
    result = x*7
    print(result)


# In[19]:


#Q.6) That appends the square of each number to a new list.
my_list = []
while True:
    number = int(input("Enter a number (or enter 0 to stop): "))
    if number == 0:
        break
    squared_number = number * number
    my_list.append(squared_number)
print("Updated list:", my_list)


# In[23]:


#Q.7) To separate positive and negative number from a list.
list1 = [5,8,-1,7,-2,-7]
positive_numbers = []
negetive_numbers = []
for x in list1:
    if x>0:
        positive_numbers.append(x)
    else:
        negetive_numbers.append(x)
print(positive_numbers)
print(negetive_numbers)


# In[26]:


#Q.8) That appends the type of elements from a list.
list2 = [3,-6,'hello',True,3.14]
type_list = []
for x in list2:
    type_list.append(type(x))
print(type_list)


# In[28]:


#Q.9) To filter even and odd number from a list.
list3 = [12,53,76,32,65,78]
even_number = []
odd_number = []
for x in list3:
    if x%2==0:
        even_number.append(x)
    else:
        odd_number.append(x)
print(even_number)
print(odd_number)


# In[30]:


#Q.10) Fetch even values from a dictionary
my_dict = {'a': 10, 'b': 15, 'c': 24, 'd': 31, 'e': 42}
even_values_dict = {}
for key, value in my_dict.items():
    if value % 2 == 0:
        even_values_dict[key] = value
print("Dictionary with even values:", even_values_dict)


# In[ ]:




