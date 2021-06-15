'''
Created on May 22, 2015

@author: hsorby
'''
import json

from opencmiss.zinc.field import Field
from opencmiss.zinc.status import OK
from opencmiss.utils.zinc.field import createFieldFiniteElement

ENDO = 1
EPI = 2


class NodeModel(object):

    def __init__(self, context):
        self._context = context
        self.clear()

    def clear(self):
        self._active_group = None
        self._coordinate_field = None
        self._selection_group = None
        self._selection_group_field = None
        self._endo_group = None
        self._endo_group_field = None
        self._epi_group = None
        self._epi_group_field = None
        self._region = None

    def initialise(self, region):
        self._setupRegion(region)
        self._active_group = self._endo_group

    def serialise(self):
        data = {'ENDO': [], 'EPI': []}
        fieldmodule = self._region.getFieldmodule()
        nodeset = fieldmodule.findNodesetByName('nodes')
        it = nodeset.createNodeiterator()
        node = it.next()
        while node.isValid():
            pos = self.getNodeLocation(node)
            if self._endo_group.containsNode(node):
                data['ENDO'].append(pos)
            elif self._epi_group.containsNode(node):
                data['EPI'].append(pos)

            node = it.next()
        return json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialise(self, string):
        data = json.loads(string)
        self._region.beginChange()
        active_surface = self._active_group
        self.setActiveSurface(ENDO)
        for pos in data['ENDO']:
            node = self.createNode()
            self.setNodeLocation(node, pos)
            self.assignToActiveSurface(node)
        self.setActiveSurface(EPI)
        for pos in data['EPI']:
            node = self.createNode()
            self.setNodeLocation(node, pos)
            self.assignToActiveSurface(node)

        self._active_group = active_surface
        self._region.endChange()

    def getPointCloud(self, surface):

        def _getLocations(nodeset):
            locations = []
            ni = nodeset.createNodeiterator()
            node = ni.next()
            while node.isValid():
                locations.append(self.getNodeLocation(node))
                node = ni.next()

            return locations

        if surface == ENDO:
            return _getLocations(self._endo_group)
        elif surface == EPI:
            return _getLocations(self._epi_group)

        return []

    def getContext(self):
        return self._context

    def getRegion(self):
        return self._region

    def getCoordinateField(self):
        return self._coordinate_field

    def setActiveSurface(self, surface):
        if surface == ENDO:
            self._active_group = self._endo_group
        elif surface == EPI:
            self._active_group = self._epi_group

    def assignToActiveSurface(self, node):
        if self._selection_group.containsNode(node):
            self._selection_group.removeNode(node)
        self._active_group.addNode(node)

    def setSelected(self, node):
        if self._endo_group.containsNode(node):
            self._endo_group.removeNode(node)
        elif self._epi_group.containsNode(node):
            self._epi_group.removeNode(node)
        self._selection_group.addNode(node)

    def getNodeLocation(self, node):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        result, location = self._coordinate_field.evaluateReal(fieldcache, 3)
        fieldmodule.endChange()

        if result == OK:
            return location

        return None

    def setNodeLocation(self, node, location):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        self._coordinate_field.assignReal(fieldcache, location)
        fieldmodule.endChange()

    def createNode(self):
        '''
        Create a node with the models coordinate field.
        '''
        fieldmodule = self._region.getFieldmodule()
        fieldmodule.beginChange()

        nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        template = nodeset.createNodetemplate()
        template.defineField(self._coordinate_field)

        scene = self._region.getScene()
        selection_field = scene.getSelectionField()
        if not selection_field.isValid():
            scene.setSelectionField(self._selection_group_field)

        self._selection_group_field.clear()

        node = nodeset.createNode(-1, template)
        self._selection_group.addNode(node)

        fieldmodule.endChange()

        return node

    def getSelectionGroupField(self):
        return self._selection_group_field

    def getEndoGroupField(self):
        return self._endo_group_field

    def getEpiGroupField(self):
        return self._epi_group_field

    def _setupRegion(self, region):
        self._region = region.createChild(
            'node_region')  # self._context.createRegion() #  self._context.getDefaultRegion().createChild('surfaces')
        self._coordinate_field = createFieldFiniteElement(self._region)
        fieldmodule = self._region.getFieldmodule()
        nodeset = fieldmodule.findNodesetByName('nodes')

        # Setup the selection fields
        self._selection_group_field = fieldmodule.createFieldGroup()
        node_group = self._selection_group_field.createFieldNodeGroup(nodeset)
        self._selection_group = node_group.getNodesetGroup()

        # Setup the selection fields
        self._endo_group_field = fieldmodule.createFieldGroup()
        node_group = self._endo_group_field.createFieldNodeGroup(nodeset)
        self._endo_group = node_group.getNodesetGroup()

        # Setup the selection fields
        self._epi_group_field = fieldmodule.createFieldGroup()
        node_group = self._epi_group_field.createFieldNodeGroup(nodeset)
        self._epi_group = node_group.getNodesetGroup()
