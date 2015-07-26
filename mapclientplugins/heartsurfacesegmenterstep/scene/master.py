'''
Created on May 22, 2015

@author: hsorby
'''
from mapclientplugins.heartsurfacesegmenterstep.scene.image import ImageScene
from mapclientplugins.heartsurfacesegmenterstep.scene.node import NodeScene

class HeartSurfaceScene(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        self._master_model = model
        self._image = ImageScene(model.getImageModel())
        self._node = NodeScene(model.getNodeModel())
        
    def initialise(self):
        self._image.initialise()
        self._node.initialise()
        
    def clear(self):
        self._image.clear()
        self._node.clear()
        
    def setNodeGraphicsSize(self, size):
        self._node.setGraphicsSize(size)
        
    def getScene(self):
        return self._master_model.getRegion().getScene()
        
