#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from ftplib import FTP
from datetime import datetime
from datetime import timedelta
import zipfile
import os


# In[3]:


#a python class to scape data from the texas rrc file transfer protocol

class grabtxrrcdata():
    
    def __init__(self, localPath = 'C:/Users/Fahim/Desktop/Gibson Reports/AI/Temp'):
        
        self.url = 'ftpe.rrc.texas.gov'
        self.username = 'anonymous'
        self.password = 'emailemail.com'
        self.date = datetime(2020,8,5)
        
        self.localPath = localPath
        os.chdir(self.localPath)
        
    def login(self):
        global ftp 
        
        ftp = FTP(self.url)
        ftp.login(self.username, self.password)
        return
    
    def makeLabel(self):
        self.dirName = self.date.strftime('%x').replace('/','-') + '20'
        self.fileName = self.dirName + '.zip'
        print(self.dirName)
        
        return
    
    def changeDate(self):
        self.date = self.date  + timedelta(days=1)
        return
    
    def setDir(self):
        ftp.cwd(str('/directional_survey/' + self.dirName + '/'))
        return
    
    def grabFile(self):
        localFile = open(self.fileName, 'wb')
        ftp.retrbinary('RETR ' + self.fileName, localFile.write, 1024)
        ftp.quit()
        localFile.close()
        return
    
    def unzipFile(self):
        zfile = zipfile.ZipFile(self.fileName)
        zfile.extractall()
        zfile.close()
        os.remove(self.fileName)
        return
    
    def main(self,days = 2):
        
        for day in range(days):
            self.login()
            self.makeLabel()
            self.setDir()
            self.grabFile()
            self.unzipFile()
            self.changeDate()
            print(self.dirName + ' done!')
            
        return
    
    
        
        
        
        
        
        
        
        


# In[4]:


# t = grabtxrrcdata()


# In[5]:


# t.main()


# In[ ]:




