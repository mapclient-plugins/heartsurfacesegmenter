'''
Created on May 22, 2015

@author: hsorby
'''
from PySide import QtCore

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

from mapclientplugins.heartsurfacesegmenterstep.maths.algorithms import calculateLinePlaneIntersection

class SegmentationWidget(SceneviewerWidget):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(SegmentationWidget, self).__init__(parent)
        self._model = None
        self._active_button = QtCore.Qt.NoButton
        
    def setModel(self, model):
        self._model = model
        
    def mousePressEvent(self, event):
        if self._active_button != QtCore.Qt.NoButton:
            return

        self._active_button = event.button()
        
        self._handle_mouse_events = False
        self._active_plane = None
        self._active_node = None
        if (event.modifiers() & QtCore.Qt.CTRL) and event.button() == QtCore.Qt.LeftButton:
            point_on_plane = self._calculatePointOnPlane(event.x(), event.y())
            if point_on_plane is not None:
                self._model.beginHierarchicalChange()
                node_model = self._model.getNodeModel()
                node = node_model.createNode()
                node_model.setNodeLocation(node, point_on_plane)
                self._active_node = node
                self._model.endHierarchicalChange()
            else:
                node_graphic = self.getNearestGraphicsNode(event.x(), event.y())
                nearest_graphics = self.getNearestGraphics()
                if node_graphic == nearest_graphics:
                    node = self.getNearestNode(event.x(), event.y())
                    node_model = self._model.getNodeModel()
                    node_model.setSelected(node)
                    self._active_node = node
                    self._active_plane = 'pending'
        else:
            super(SegmentationWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._active_plane is not None and self._active_node is not None:
            point_on_plane = self._calculatePointOnPlane(event.x(), event.y(), plane_description=self._active_plane)
            if point_on_plane is not None:
                node_model = self._model.getNodeModel()
                node_model.setNodeLocation(self._active_node, point_on_plane)
        else:
            super(SegmentationWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._active_button != event.button():
            return

        if self._active_plane is not None and self._active_node is not None:
            node_model = self._model.getNodeModel()
            node_model.assignToActiveSurface(self._active_node)
            self._active_plane = None
            self._active_node = None
        else:
            super(SegmentationWidget, self).mouseReleaseEvent(event)

        self._active_button = QtCore.Qt.NoButton

    def _calculatePointOnPlane(self, x, y, plane_description=None):
        if plane_description is not None and not plane_description == 'pending':
            plane_point = plane_description[0]
            plane_normal = plane_description[1]
        else:
            plane_graphic = self.getNearestGraphicsMesh2D(x, y)
            if plane_graphic:
                scene = plane_graphic.getScene()
                region = scene.getRegion()
                plane_point, plane_normal = self._model.getImagePlane(region)
                self._active_plane = [plane_point, plane_normal]
            else:
                return None

        far_plane_point = self.unproject(x, -y, -1.0)
        near_plane_point = self.unproject(x, -y, 1.0)
        point_on_plane = calculateLinePlaneIntersection(near_plane_point, far_plane_point, plane_point, plane_normal)
        
        return point_on_plane
    
