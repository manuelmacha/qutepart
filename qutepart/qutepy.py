'''
Created on Aug 16, 2014

@author: manuel
'''

from qutepart import Qutepart

class QutePy(Qutepart):
    '''
    Variation of the qutepart editor to be used solely as a python text editor.
    '''


    def __init__(self, *args):
        '''
        Constructor
        '''
        super(QutePy, self).__init__(*args)
        
        
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    qp = QutePy(None)
    qp.show()
    qp.raise_()
    sys.exit(app.exec_())    
        