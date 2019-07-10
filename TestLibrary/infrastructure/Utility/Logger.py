# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-03-04
@Author      : jet
@Filename : Logger.py
@Software : eclipse + RED
"""

'''    
       useage:
       1.    logger.info("Input >>> pdict : {0} , rdict : {1}".format(pdict,rdict)) 
       2.    logger.info("\n".join(remainTextList))   
'''
import os
import logging


def get_logger():
    bashPath = os.path.join(os.path.dirname(__file__), '../../../')
    #bashPath = os.path.join(os.path.dirname(__file__), 'log')
    if not os.path.exists(bashPath):
        os.mkdir(bashPath)
    logFile = os.path.join(bashPath, 'DemoTestLibrary.log')

    my_logger = logging.getLogger("DemoTestLibrary")
    my_logger.setLevel(level = logging.DEBUG)
    handler = logging.FileHandler(logFile)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    
    my_logger.addHandler(handler)
    my_logger.addHandler(console)
    return my_logger

logger = get_logger()