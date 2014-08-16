'''
Created on Aug 16, 2014

@author: manuelmacha
'''
from PyQt4.QtGui import QWidget

class MiniMapWidget(QWidget):
    '''
    A miniMap widget to compliment the qutepart text editor, similar to the one found in sublime.
    '''


    def __init__(self, qutepart_, parent = None):
        '''
        Constructor
        @param qutepart_: reference to the instance of the qutepart editor which contains the document to be reflected in this minimap 
        '''
        
        super(MiniMapWidget, self).__init__(parent)
        
        self._qutepart = qutepart_
        
        
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    mmw = MiniMapWidget(None)
    mmw.show()
    mmw.raise_()
    sys.exit(app.exec_())

    
        