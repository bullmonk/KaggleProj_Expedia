# -*- coding: utf-8 -*-
"""
Created on Sat May 07 22:53:31 2016

@author: Xun
"""

####input moduler######################################
import numpy as np
import csv as csv

####input data#########################################  Only notification: change dirctory path here!!!!!!!!!!!!!
#train0 = np.genfromtxt('C:/WinPython/python-2.7.9.amd64/Scripts/expedia/example.csv',delimiter=',',dtype=None)
def read_csv(filename,nline=None):
    table=[]
    with open(filename,'rb') as f:
        sheet = csv.reader(f)
        if nline:
            for row in xrange(nline):
                table.append(sheet.next())
        else:
            for row in sheet:
                table.append(row)
    return table
train0 = np.array(read_csv('C:/WinPython/python-2.7.9.amd64/Scripts/expedia/train.csv',nline = 80000))    

####temporarily remove variables  origin_distance################
train1 = np.delete(train0,6,axis=1)

####check null values##################################
domain = np.core.defchararray.equal(train1,'').astype('int')
danger = np.sum(np.sum(domain,axis=0))
if danger:
    ind = np.nonzero(domain)
    badind = np.unique(ind[0])
    train1 = np.delete(train1,badind,0)
    train0 = np.delete(train0,badind,0)

####build final train data#############################
name = train1[0,:].squeeze()
trainname = []
traindata = []
length = np.shape(train1[:,0].squeeze())[0] - 1

####create variable: book_year#########################
bky = []
for i in xrange(length):
    bky.append((np.datetime64(train1[i+1,0]).astype('M8[Y]')-np.datetime64('0000')).astype('int'))

trainname.append('Book_Year')
traindata = bky

####put back variable: orig_destination_distance#######
trainname.append(train0[0,6])
odd = train0[1::,6].squeeze()
del domain
del ind
domain = np.core.defchararray.equal(odd,'')
ind = np.nonzero(domain)
odd[ind] = 0
traindata = np.column_stack((traindata,odd))

####examine variable: site_name#########################
#trainname.append(name[1])
#SiteName = train1[1::,1].squeeze().astype('int')
#traindata = np.column_stack((traindata,SiteName))

####examine variable: posa_continent####################
#trainname.append(name[2])
#PosaCont = train1[1::,2].squeeze().astype('int')
#traindata = np.column_stack((traindata,PosaCont))

####examine variable: user_location_country##############
trainname.append(name[3])
LocCoun = train1[1::,3].squeeze().astype('int')
traindata = np.column_stack((traindata,LocCoun))

####examine variable: user_location_region###############
trainname.append(name[4])
LocReg = train1[1::,4].squeeze().astype('int')
traindata = np.column_stack((traindata,LocReg))

####examine variable: user_location_city#################
trainname.append(name[5])
LocCit = train1[1::,5].squeeze().astype('int')
traindata = np.column_stack((traindata,LocCit))

####examine variable: is_mobile##########################
trainname.append(name[7])
UserMob = train1[1::,7].squeeze().astype('int')
traindata = np.column_stack((traindata,UserMob))

####examine variable: is_package#########################
trainname.append(name[8])
UserPac = train1[1::,8].squeeze().astype('int')
traindata = np.column_stack((traindata,UserPac))

####examine variable: channel############################
trainname.append(name[9])
Channel = train1[1::,9].squeeze().astype('int')
traindata = np.column_stack((traindata,Channel))

####examine variable: srch_adults_cnt####################
#trainname.append(name[12])
#AduCnt = train1[1::,12].squeeze().astype('int')
#traindata = np.column_stack((traindata,AduCnt))

####examine variable: srch_children_cnt##################
#trainname.append(name[13])
#ChdCnt = train1[1::,13].squeeze().astype('int')
#traindata = np.column_stack((traindata,ChdCnt))

####examine variable: srch_rm_cnt#########################
trainname.append(name[14])
SrchRm = train1[1::,14].squeeze().astype('int')
traindata = np.column_stack((traindata,SrchRm))

####examine variable: srch_destination_id#################
trainname.append(name[15])
SrchDes = train1[1::,15].squeeze().astype('int')
traindata = np.column_stack((traindata,SrchDes))

####examine variable: srch_destination_type_id############
trainname.append(name[16])
SrchDT = train1[1::,16].squeeze().astype('int')
traindata = np.column_stack((traindata,SrchDT))

####examine variable: hotel_continent#####################
#trainname.append(name[19])
#HotCon = train1[1::,19].squeeze().astype('int')
#traindata = np.column_stack((traindata,HotCon))

####examine variable: hotel_country#######################
trainname.append(name[20])
HotCoun = train1[1::,20].squeeze().astype('int')
traindata = np.column_stack((traindata,HotCoun))

####examine variable: hotel_market########################
trainname.append(name[21])
HotMkt = train1[1::,21].squeeze().astype('int')
traindata = np.column_stack((traindata,HotMkt))

####examine variable: user_id############################
#trainname.append(name[6])
#Userid = train1[1::,6].squeeze().astype('int')
#traindata = np.column_stack((traindata,Userid))

####examine variable: cnt#################################
#trainname.append(name[18])
#Cnt = train1[1::,18].squeeze().astype('int')
#traindata = np.column_stack((traindata,Cnt))

####examine variable: hotel_cluster#######################
trainname.append(name[22])
HotClst = train1[1::,22].squeeze().astype('int')
traindata = np.column_stack((traindata,HotClst))

####examine variable: is_booking##########################
trainname.append(name[17])
IsBk = train1[1::,17].squeeze().astype('int')
traindata = np.column_stack((traindata,IsBk))
###############################################################################


####return value of this function#########################
clstunk = np.unique(HotClst) #all unique hotel clusters
clstnum =  np.shape(clstunk)[0] #number of hotel clusters














