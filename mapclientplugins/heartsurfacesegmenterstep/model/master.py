'''
Created on May 21, 2015

@author: hsorby
'''
from cmlibs.zinc.context import Context

from mapclientplugins.heartsurfacesegmenterstep.model.image import ImageModel
from mapclientplugins.heartsurfacesegmenterstep.model.node import NodeModel
import os


class HeartSurfaceModel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._context = Context('heartsurface')
        self.defineStandardMaterials()
        self.defineStandardGlyphs()
        self._region = None
        self._image_model = ImageModel(self._context)
        self._node_model = NodeModel(self._context)
        self._location = None

    def setLocation(self, location):
        self._location = location

    def save(self):
        if not os.path.exists(self._location):
            os.mkdir(self._location)

        string = self._node_model.serialise()
        with open(os.path.join(self._location, 'nodes.json'), 'w') as f:
            f.write(string)

    def load(self):
        if os.path.exists(os.path.join(self._location, 'nodes.json')):
            with open(os.path.join(self._location, 'nodes.json')) as f:
                string = f.read()
                self._node_model.deserialise(string)

    def getPointCloud(self, surface):
        return self._node_model.getPointCloud(surface)

    def getContext(self):
        return self._context

    def setImageData(self, axis, image_data):
        self._image_model.setImageData(axis, image_data)

    def initialise(self):
        self._region = self._context.createRegion()
        self._image_model.initialise(self._region)
        self._node_model.initialise(self._region)

    def clear(self):
        self._image_model.clear()
        self._node_model.clear()
        self._region = None

    def getRegion(self):
        return self._region

    def getImageModel(self):
        return self._image_model

    def getNodeModel(self):
        return self._node_model

    def getImagePlane(self, region):
        return self._image_model.getPlane(region)

    def getImageRegionNames(self):
        return self._image_model.getRegionNames()

    def setImageRegionVisibility(self, region_name, state):
        self._image_model.setRegionVisibility(region_name, state)

    def setActiveSurface(self, surface):
        self._node_model.setActiveSurface(surface)

    def beginHierarchicalChange(self):
        region = self._context.getDefaultRegion()
        region.beginHierarchicalChange()

    def endHierarchicalChange(self):
        region = self._context.getDefaultRegion()
        region.endHierarchicalChange()

    def defineStandardGlyphs(self):
        '''
        Helper method to define the standard glyphs
        '''
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def defineStandardMaterials(self):
        '''
        Helper method to define the standard materials.
        '''
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()
