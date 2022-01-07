#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
from resources.config import strUsername, strPassword, strToken, orgURL, query, chromeDriverPath, strdomain
from splinter import Browser
import lib.MakeUserTable
import pandas as pd
from simple_salesforce import Salesforce
import time;


# In[2]:


# connect to Salesforce API
if strdomain == 'test':
	sf = Salesforce(username=strUsername, password=strPassword, security_token=strToken, domain= strdomain)
else:
	sf = Salesforce(username=strUsername, password=strPassword, security_token=strToken)


# In[3]:


# get active users
lstActiveUser = sf.query(query)


# In[4]:


# set up splinter browser
dictPath = {'executable_path': chromeDriverPath}
brsr = Browser('chrome', **dictPath, headless=False)


# In[5]:


# log in to Salesforce
if strdomain == 'test':
    strURLLogin = 'https://test.salesforce.com/'
else:
    strURLLogin = 'https://login.salesforce.com/'
brsr.visit(strURLLogin)
brsr.fill('username', strUsername)
brsr.fill('pw', strPassword)
btnLogin = brsr.find_by_name('Login')
btnLogin.click()
time.sleep(30)


# In[6]:


# set up master dataframe
dfUsers = pd.DataFrame(columns=['Record Type', 'Record Count'])


# In[7]:


# loop through all Active Users
for rec in lstActiveUser['records']:
    # visit User Storage webpage
    strId = rec['Id']
    strURLUser = orgURL + '/setup/user/userstorageusage.jsp?id=' + strId
    brsr.visit(strURLUser)
    html = brsr.html
    dfUser = lib.MakeUserTable.MakeUserTable(html, strId)
    dfUsers = pd.concat([dfUser, dfUsers])


# In[8]:


dfUsers.to_excel('export.xlsx')


# In[9]:


# quit
brsr.quit

