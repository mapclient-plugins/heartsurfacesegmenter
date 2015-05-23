'''
Created on May 21, 2015

@author: hsorby
'''
from PySide import QtGui, QtCore

from mapclientplugins.heartsurfacestep.view.ui_heartsurfacewidget import Ui_HeartSurfaceWidget
from mapclientplugins.heartsurfacestep.scene.master import HeartSurfaceScene
from mapclientplugins.heartsurfacestep.model.node import EPI, ENDO

class HeartSurfaceWidget(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(HeartSurfaceWidget, self).__init__(parent)
        self._ui = Ui_HeartSurfaceWidget()
        self._ui.setupUi(self)
        self._ui.widgetZinc.setContext(model.getContext())
        self._ui.widgetZinc.setModel(model)
        self._master_model = model
        self._master_scene = HeartSurfaceScene(model)
        self._callback = None
        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.pushButtonHideAll.clicked.connect(self._hideAllButtonClicked)
        self._ui.listWidget.itemChanged.connect(self._itemChanged)
        self._ui.comboBoxHeartSurface.currentIndexChanged.connect(self._heartSurfaceChanged)
        self._ui.spinBoxPointSize.valueChanged.connect(self._pointSizeChanged)
        self._ui.pushButtonLoad.clicked.connect(self._loadButtonClicked)
        self._ui.pushButtonSave.clicked.connect(self._saveButtonClicked)
        
    def _loadButtonClicked(self):
        self._master_model.load()
    
    def _saveButtonClicked(self):
        self._master_model.save()
        
    def _heartSurfaceChanged(self, index):
        if index == 0:
            self._master_model.setActiveSurface(ENDO)
        elif index == 1:
            self._master_model.setActiveSurface(EPI)
        
    def _pointSizeChanged(self, value):
        self._master_scene.setNodeGraphicsSize(value)
        
    def _itemChanged(self, item):
        region = item.text()
        self._master_model.setImageRegionVisibility(region, item.checkState() == QtCore.Qt.Checked)
        
    def setImageData(self, axis, image_data):
#         self._master_scene.clear()
#         self._master_model.clear()
        
        self._master_model.setImageData(axis, image_data)
        
    def initialise(self):
        self._master_model.initialise()
        self._master_scene.initialise()
         
        self._setupUi()
        
    def _setupUi(self):
        self._ui.listWidget.clear()
        region_names = self._master_model.getImageRegionNames()
        
        for region_name in region_names:
            item = QtGui.QListWidgetItem(self._ui.listWidget)
            item.setText(region_name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | item.flags())
            item.setCheckState(QtCore.Qt.Checked)
        
    def getPointCloud(self, surface):
        return self._master_model.getPointCloud(surface)
    
    def registerDoneExecution(self, callback):
        self._callback = callback
        
    def _doneButtonClicked(self):
        self._callback()
        
    def _viewAllButtonClicked(self):
        self._master_model.beginHierarchicalChange()
        self._ui.widgetZinc.viewAll()
        for index in range(self._ui.listWidget.count()):
            item = self._ui.listWidget.item(index)
            item.setCheckState(QtCore.Qt.Checked)
        self._master_model.endHierarchicalChange()
 
    def _hideAllButtonClicked(self):
        self._master_model.beginHierarchicalChange()
        for index in range(self._ui.listWidget.count()):
            item = self._ui.listWidget.item(index)
            item.setCheckState(QtCore.Qt.Unchecked)
        self._master_model.endHierarchicalChange()
