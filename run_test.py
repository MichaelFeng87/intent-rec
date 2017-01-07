# -*- coding: UTF-8 -*-

'''
Created on 2016年11月22日

@author: super
''' 

'''
1. laod train and test data
2. train network predictor model
3. evaluate network predictor model
*4. run predict by network model
'''
'''
1. train model
2. evaluate the model
'''

import time

from core import layer
from recog.test.testMedQuesRec import testLoadBasicData, testTrainNetPred, \
    testEvalNetPred, testShowNetPred, testLoadAttentionData, testGetNpyData


def one_data(lb_data=2, name_net='BiDirtGRU_Net', encode_type=0):
    # exp_param
      
#     xy_data, input_shape = testLoadBasicData(lb_data=lb_data)
    xy_data, input_shape = testGetNpyData(lb_data=lb_data, encode_type=encode_type)
    print('x_train: {0}'.format(xy_data[0]))
    print(xy_data[0].shape)
    print('y_train: {0}'.format(xy_data[1]))
    print(xy_data[1].shape)
#     print(len(set(xy_data[1]])))
    print('x_test: {0}'.format(xy_data[2]))
    print('y_test: {0}'.format(xy_data[3]))
#     print(len(set(xy_data[3])))
    print('input_shape: {0}'.format(input_shape))
    
    model_path, history_metrices = testTrainNetPred(xy_data, input_shape, name_net=name_net, lb_data=lb_data)
    score = testEvalNetPred(xy_data, model_path)
    # testRunNetPred(xy_data, model_path)
    
    ''' write the exp-res into file '''
    resFileName = 'RES_{0}_mat{1}_data{2}.txt'.format(name_net, encode_type, lb_data)
    resStr = str(history_metrices) + '\n' + str(score)
    fw = open(resFileName, 'w')
    fw.write(resStr)
    fw.close()
    
# one_data()

'''
batch process as above operation from data 0~9
'''
def batch_allData(name_net='BiDirtGRU_Net', encode_type=1):  
    for i in range(10):
        one_data(lb_data=i, name_net=name_net, encode_type=encode_type)
    
# batch_allData()

'''
bacth all model on one data
'''
def batch_allModel_oneData(lb_data=2, encode_type=1):
#     name_nets = ['CNNs_Net', 'GRU_Net', 'BiDirtGRU_Net', 'LSTM_Net', 'BiDirtLSTM_Net', 'StackLSTMs_Net']
    name_nets = ['CNNs_Net', 'GRU_Net', 'LSTM_Net', 'BiDirtLSTM_Net', 'StackLSTMs_Net']
    for name_net in name_nets:
        one_data(lb_data=lb_data, name_net=name_net, encode_type=encode_type)
        
batch_allModel_oneData(encode_type=0)
batch_allModel_oneData(encode_type=1)
        
'''
batch process all model in all data 0~9
'''
def batch_allModel_allData(encode_type=1):
    name_nets = ['CNNs_Net', 'GRU_Net', 'BiDirtGRU_Net', 'LSTM_Net', 'BiDirtLSTM_Net', 'StackLSTMs_Net']
    #===========================================================================
    # '''except CNNs_Net'''
    # name_nets = ['GRU_Net', 'BiDirtGRU_Net', 'LSTM_Net', 'BiDirtLSTM_Net', 'StackLSTMs_Net']
    #===========================================================================
    for name_net in name_nets:
        batch_allData(name_net=name_net, encode_type=encode_type)

# batch_allModel_allData()

'''
1. fig the model framework picture
(inux only)
'''
#===============================================================================
# # exp_param
# lb_data = 0
# name_net = 'CNNs_Net'
# 
# xy_data, input_shape = testLoadBasicData(lb_data=lb_data)
# testShowNetPred(input_shape=input_shape, name_net=name_net)
#===============================================================================

'''
load attention xy_data and store them into npz
'''
def load_store_matData(lb_data=2, encode_type=1):
    '''
    @param @encode_type: 0: basic mat data, 1: attention mat data
    '''
    xy_data = None
    input_shape = None
    if encode_type == 0:
        xy_data, input_shape = testLoadBasicData(lb_data=lb_data)
    else:
        xy_data, input_shape = testLoadAttentionData(lb_data=lb_data)
    
    print('x_train: {0}'.format(xy_data[0]))
    print(xy_data[0].shape)
    print('y_train: {0}'.format(xy_data[1]))
    print(xy_data[1].shape)
#     print(len(set(xy_data[1]])))
    print('x_test: {0}'.format(xy_data[2]))
    print('y_test: {0}'.format(xy_data[3]))
#     print(len(set(xy_data[3])))
    print('input_shape: {0}'.format(input_shape))
    
#load_store_matData()

'''
batch load xy_data and store them into npz
'''
def batchload_store_matData(encode_type=1):
    for i in range(10):
        load_store_matData(lb_data=i, encode_type=encode_type)
        
# batchload_store_matData()
        
