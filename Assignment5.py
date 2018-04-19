
# coding: utf-8

# In[1]:


#Question1
s=input("Enter the string:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)


# In[21]:


#Question2
s1=input("Enter first string:")
s2=input("Enter second string:")
update=list(set(s1)&set(s2))
print("The common letters are:")
for i in update:
    print(i)


# In[2]:


#Question3
str1=input("Enter first string:")
str2=input("Enter second string:")
update=list(set(str1)-set(str2))
print("The letters are:")
for i in update:
    print(i)


# In[22]:


#Question4
s1=input("Enter first string:")
s2=input("Enter second string:")
update=list(set(s1)&set(s2))
print("The common letters are:")
for i in update:
    print(i)


# In[3]:


#Question5
f=open("D:/data.txt",'r')
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()


# In[23]:


#Question6
f=open("D:/data.txt",'r')
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()


# In[24]:


#Question7
f=open('D:/data.txt', 'r')
num=0
for line in f:
    words = line.split()
    num += len(words)
print("Number of words:")
print(num)
f.close()


# In[4]:


#Question8
lines= 0
f= open("D:/data.txt", 'r')
for line in f:
     lines += 1
print("Number of lines:")
print(lines)
f.close()


# In[5]:


#Question9
f=open("D:/data1.txt","w")
c=input("will meet you tomorrow: \n");
f.write("\n")
f.write(c)
f.close()
print("Contents of appended file:");
f1=open("D:/data1.txt",'r')
line=f1.readline()
while(line!=""):
    print(line)
    line=f1.readline()    
f1.close()


# In[25]:


#Question10
word=input("Enter word to be searched:")
k = 0
 
f=open('D:/data.txt', 'r')
for line in f:
    words = line.split()
    for i in words:
        if(i==word):
            k=k+1
print("Occurrences of the word:")
print(k)


# In[26]:


#Question11
f = open("D:/data.txt",'r')
f1 =open("D:/data1.txt", "w")
for line in f:
    f1.write(line)
f.close()
f1.close()


# In[27]:


#Question12
l=input("Enter letter to be searched:")
k = 0
 
f=open('D:/data.txt', 'r')
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter==l):
                k=k+1
print("Occurrences of the letter:")
print(k)


# In[18]:


#Question13
f= open("D:/data.txt", 'r')
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
             if(letter.isdigit()):
                 print(letter)
f.close()                


# In[32]:


#Question14
f = open('D:/data.txt', "r")
data = f.read()
f.close()
f1 = open('D:/data1.txt', "a")
f1.write(data)
f1.close()


# In[29]:


#Question15
k = 0
 
f =open('D:/data.txt', 'r')
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter.isspace):
                 k=k+1
print("Occurrences of blank spaces:")
print(k)


# In[30]:


#Question16
f=open('D:/data.txt', 'r')
for line in f:
    l=line.title()
    print(l)


# In[20]:


#Question17
f=open("D:/data.txt", 'r')
for line in reversed(list(open("D:/data.txt"))):
    print(line.rstrip())

