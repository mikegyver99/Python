# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:25:48 2016

@author: Michael Garcia garciamj@eou.edu
"""
import sys

d={'/dev/mapper/centos-home': '/home', '/dev/mapper/centos-opt': '/opt', '/dev/mapper/centos-var': '/var', '/dev/sda1': '/boot', '/dev/mapper/centos-root': '/'}
e={'/dev/mapper/centos-opt': '/opt', 'UUID=df510f9c-5d9e-4c08-8815-7e7abd2105c6': '/boot', '//fs/smb': '/mnt/smb', '/dev/mapper/centos-swap': 'swap', '/dev/mapper/centos-home': '/home', '/dev/mapper/centos-var': '/var', '/dev/mapper/centos-root': '/'}

#e['/dev/sda1'] = e.pop('UUID=df510f9c-5d9e-4c08-8815-7e7abd2105c6')
print(e)
    
for key in e:
    if key.startswith('UUID'):
        var1=key
        print(var1)
        