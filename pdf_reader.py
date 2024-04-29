#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2


# In[3]:


myFile=open('US_Declaration.pdf',mode='rb')


# In[4]:


pdfReader = PyPDF2.PdfReader(myFile)


# In[7]:


#pdfReader.numPages

len(pdfReader.pages)


# In[9]:


#page_one=pdfReader.getPage(0)
page_one=pdfReader.pages[0]


# In[13]:


print(page_one.extract_text())
print (f"Test Build for teamCity")


# In[ ]:




