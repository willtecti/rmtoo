'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test class for the Configuration.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

class CfgEx(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
