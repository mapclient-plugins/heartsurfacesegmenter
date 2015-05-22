'''
Created on May 22, 2015

@author: hsorby
'''
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.field import Field

class NodeScene(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        self._model = model
        self.clear()
        
    def clear(self):
        self._selection_graphics = None
        self._endo_graphics = None
        self._epi_graphics = None
    
    def initialise(self):
        self._setupVisualisation()
        
    def setGraphicsSize(self, size):
        region = self._model.getRegion()
        scene = region.getScene()
        scene.beginChange()
        attributes = self._selection_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._endo_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._epi_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        scene.endChange()
        
    def _setupVisualisation(self):
        coordinate_field = self._model.getCoordinateField()
        region = self._model.getRegion()
        scene = region.getScene()
        materialmodule = scene.getMaterialmodule()
        red = materialmodule.findMaterialByName('red')
        yellow = materialmodule.findMaterialByName('yellow')
        green = materialmodule.findMaterialByName('green')
        self._selection_graphics = self._createGraphics(scene, coordinate_field, yellow, self._model.getSelectionGroupField())
        self._endo_graphics = self._createGraphics(scene, coordinate_field, red, self._model.getEndoGroupField())
        self._epi_graphics = self._createGraphics(scene, coordinate_field, green, self._model.getEpiGroupField())

    def _createGraphics(self, scene, finite_element_field, material, subgroup_field):
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setMaterial(material)
        graphic.setSelectedMaterial(material)
        graphic.setSubgroupField(subgroup_field)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        attributes.setBaseSize([1.0])
#         surface = scene.createGraphicsSurfaces()
#         surface.setCoordinateField(finite_element_field)
        scene.endChange()

        return graphic
