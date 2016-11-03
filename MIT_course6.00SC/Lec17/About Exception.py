# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 10:48:09 2016

@author: 07
"""

class NoChildException(Exception):
    pass
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


def test():
    raise NoChildException('holy shit')
    

if __name__ == '__main__':
    print 222
    try:
        test()
    except Exception,e:
        print e