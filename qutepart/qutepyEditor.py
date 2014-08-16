'''
Created on Aug 16, 2014

@author: manuel
'''

# Import statements
from qutepart.qutepy import QutePy
from qutepart.miniMap import MiniMapWidget
from PyQt4.QtGui import QWidget, QMainWindow, QVBoxLayout, QDockWidget
from PyQt4.QtCore import Qt

class QutePyEditor(QMainWindow):
    '''
    Arranges an instance of the Qutepart editor and minimap in a widget
    '''


    def __init__(self, parent = None):
        '''
        Constructor. Just setting up member-variables. initQutePyEditor needs to be called to create sub-widgets.
        '''
        super(QutePyEditor, self).__init__(parent)
        
        self._qutePy = None
        self._qutePyDockWidget = None
        self._miniMapWidget = None
        self._miniMapDockWidget = None
        
    def initQutePyEditor(self):
        
        self.setWindowTitle(self.__class__.__name__)
        
        self._qutePyDockWidget = QDockWidget(self)
        self._miniMapDockWidget = QDockWidget(self)
        
        self._qutePy = QutePy(self._qutePyDockWidget)
        self._miniMapWidget = MiniMapWidget(self._qutePy, parent = self._miniMapDockWidget)
        
        self._qutePyDockWidget.setWidget(self._qutePy)
        self._miniMapDockWidget.setWidget(self._miniMapWidget)
        
        self._miniMapDockWidget.setWindowTitle(self._miniMapWidget.__class__.__name__)
        
        self.addDockWidget(Qt.LeftDockWidgetArea, self._qutePyDockWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, self._miniMapDockWidget)
        
        
        

        
        
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    qpe = QutePyEditor(None)
    qpe.initQutePyEditor()
    qpe.show()
    qpe.raise_()
    sys.exit(app.exec_())        
        