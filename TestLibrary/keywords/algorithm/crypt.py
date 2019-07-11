# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-11
@Author      : jet
@Filename : crypt.py
@Software : eclipse + RED
"""

from TestLibrary.infrastructure.Utility.AESCipher import AESCipher

class crypt:
    def __init__(self):
        pass

    def kw_aes_cbc_encrypt(self, secureKey, iv, data):
        """加密"""
        e = AESCipher(secureKey, iv)
        return e.encrypt(data)
    
    def kw_aes_cbc_decrypt(self, secureKey, iv, data):
        """解密"""
        e = AESCipher(secureKey, iv)
        return e.decrypt(data)
    

    
    
    
    
    
    
    
    