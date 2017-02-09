# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:24:09 2016

@author: Xun
"""

####input moduler######################################
import numpy as np
import csv as csv

####input data#########################################  Only notification: change dirctory path here!!!!!!!!!!!!!
#test0 = np.genfromtxt('C:/WinPython/python-2.7.9.amd64/Scripts/expedia/examptest.csv',delimiter=',',dtype=None)
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
test0 = np.array(read_csv('C:/WinPython/python-2.7.9.amd64/Scripts/expedia/test.csv',nline = None))

####deleting variables  origin_distance################
test1 = np.delete(test0,[0,7],axis=1)

####one special error value############################
bad = np.nonzero(np.core.defchararray.equal(test1,'2161-10-00'))
test1[bad[0],bad[1]] = '2014'

####check null values##################################
domain = np.core.defchararray.equal(test1,'').astype('int')
danger = np.sum(np.sum(domain,axis=0))
if danger:
    ind = np.nonzero(domain)
    test1[ind[0],ind[1]] = '2014'
  
    
####build final train data#############################
name = test1[0,:].squeeze()
testname = []
testdata = []
length = np.shape(test1[:,0].squeeze())[0] - 1

####create variable: book_year#########################
bky = []
for i in xrange(length):
    bky.append((np.datetime64(test1[i+1,0]).astype('M8[Y]')-np.datetime64('0000')).astype('int'))

testname.append('Book_Year')
testdata = bky

####put back variable: orig_destination_distance#######
testname.append(test0[0,7])
odd = test0[1::,7].squeeze()
domain = np.core.defchararray.equal(odd,'')
ind = np.nonzero(domain)
odd[ind] = 0
testdata = np.column_stack((testdata,odd))

####examine variable: site_name#########################
#testname.append(name[1])
#SiteName = test1[1::,1].squeeze().astype('int')
#testdata = np.column_stack((testdata,SiteName))

####examine variable: posa_continent####################
#testname.append(name[2])
#PosaCont = test1[1::,2].squeeze().astype('int')
#testdata = np.column_stack((testdata,PosaCont))

####examine variable: user_location_country##############
testname.append(name[3])
LocCoun = test1[1::,3].squeeze().astype('int')
testdata = np.column_stack((testdata,LocCoun))

####examine variable: user_location_region###############
testname.append(name[4])
LocReg = test1[1::,4].squeeze().astype('int')
testdata = np.column_stack((testdata,LocReg))

####examine variable: user_location_city#################
testname.append(name[5])
LocCit = test1[1::,5].squeeze().astype('int')
testdata = np.column_stack((testdata,LocCit))

####examine variable: is_mobile##########################
testname.append(name[7])
UserMob = test1[1::,7].squeeze().astype('int')
testdata = np.column_stack((testdata,UserMob))

####examine variable: is_package#########################
testname.append(name[8])
UserPac = test1[1::,8].squeeze().astype('int')
testdata = np.column_stack((testdata,UserPac))

####examine variable: channel############################
testname.append(name[9])
Channel = test1[1::,9].squeeze().astype('int')
testdata = np.column_stack((testdata,Channel))

####examine variable: srch_adults_cnt####################
#testname.append(name[12])
#AduCnt = test1[1::,12].squeeze().astype('int')
#testdata = np.column_stack((testdata,AduCnt))

####examine variable: srch_children_cnt##################
#testname.append(name[13])
#ChdCnt = test1[1::,13].squeeze().astype('int')
#testdata = np.column_stack((testdata,ChdCnt))

####examine variable: srch_rm_cnt#########################
testname.append(name[14])
SrchRm = test1[1::,14].squeeze().astype('int')
testdata = np.column_stack((testdata,SrchRm))

####examine variable: srch_destination_id#################
testname.append(name[15])
SrchDes = test1[1::,15].squeeze().astype('int')
testdata = np.column_stack((testdata,SrchDes))

####examine variable: srch_destination_type_id############
testname.append(name[16])
SrchDT = test1[1::,16].squeeze().astype('int')
testdata = np.column_stack((testdata,SrchDT))

####examine variable: hotel_continent#####################
#testname.append(name[17])
#HotCon = test1[1::,17].squeeze().astype('int')
#testdata = np.column_stack((testdata,HotCon))

####examine variable: hotel_country#######################
testname.append(name[18])
HotCoun = test1[1::,18].squeeze().astype('int')
testdata = np.column_stack((testdata,HotCoun))

####examine variable: hotel_market########################
testname.append(name[19])
HotMkt = test1[1::,19].squeeze().astype('int')
testdata = np.column_stack((testdata,HotMkt))

####examine variable: user_id############################
#testname.append(name[6])
#Userid = test1[1::,6].squeeze().astype('int')
#testdata = np.column_stack((testdata,Userid))

###############################################################################






















