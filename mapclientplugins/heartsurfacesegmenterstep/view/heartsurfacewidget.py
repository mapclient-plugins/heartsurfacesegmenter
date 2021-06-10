'''
Created on May 21, 2015

@author: hsorby
'''
from PySide2 import QtCore, QtWidgets

from mapclientplugins.heartsurfacesegmenterstep.view.ui_heartsurfacewidget import Ui_HeartSurfaceWidget
from mapclientplugins.heartsurfacesegmenterstep.scene.master import HeartSurfaceScene
from mapclientplugins.heartsurfacesegmenterstep.model.node import EPI, ENDO

class HeartSurfaceWidget(QtWidgets.QWidget):
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
        self._ui.pushButtonContinue.clicked.connect(self._continueButtonClicked)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.pushButtonHideAll.clicked.connect(self._hideAllButtonClicked)
        self._ui.listWidget.itemChanged.connect(self._itemChanged)
        self._ui.comboBoxHeartSurface.currentIndexChanged.connect(self._heartSurfaceChanged)
        self._ui.spinBoxPointSize.valueChanged.connect(self._pointSizeChanged)
        self._ui.pushButtonLoad.clicked.connect(self._loadButtonClicked)
        self._ui.pushButtonSave.clicked.connect(self._saveButtonClicked)
        
        self._ui.widgetZinc.graphicsInitialized.connect(self._graphicsInitialized)
        
    def _graphicsInitialized(self):
        sceneviewer = self._ui.widgetZinc.getSceneviewer()
        scenepicker = self._ui.widgetZinc.getScenepicker()
        if sceneviewer is not None and scenepicker is not None:
            scene = self._master_scene.getScene()
            sceneviewer.setScene(scene)
            scenepicker.setScene(scene)
            sceneviewer.viewAll()
            
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
        self._graphicsInitialized()
        
    def clear(self):
        self._master_model.clear()
        self._master_scene.clear()
        
    def _setupUi(self):
        self._ui.listWidget.clear()
        region_names = self._master_model.getImageRegionNames()
        
        for region_name in region_names:
            item = QtWidgets.QListWidgetItem(self._ui.listWidget)
            item.setText(region_name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | item.flags())
            item.setCheckState(QtCore.Qt.Checked)
        
    def getPointCloud(self, surface):
        return self._master_model.getPointCloud(surface)
    
    def registerDoneExecution(self, callback):
        self._callback = callback
        
    def _continueButtonClicked(self):
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
