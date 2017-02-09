# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:36:37 2016

@author: Xun
"""

####import moduler & object###############################
import numpy as np
from expediatrain import trainname  #to be used for modeling
from expediatrain import traindata  #to be used for modeling
from expediatrain import clstunk
from expediatest import length
from expediatrain import clstnum
from expediatest import testname
from expediatest import testdata

####add column hotel_cluster to testdata##################
testname.append('hotel_cluster')
testdata = np.repeat(testdata,clstnum,axis=0)
clstunk = np.tile(clstunk,length)
testdata = np.column_stack((testdata,clstunk))
###########################################################
####data stored in traindata, trainname, testdata, testname
