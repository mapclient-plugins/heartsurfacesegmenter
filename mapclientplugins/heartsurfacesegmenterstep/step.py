
'''
MAP Client Plugin Step
'''
import os
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.heartsurfacesegmenterstep.configuredialog import ConfigureDialog
from mapclientplugins.heartsurfacesegmenterstep.view.heartsurfacewidget import HeartSurfaceWidget
from mapclientplugins.heartsurfacesegmenterstep.model.master import HeartSurfaceModel
from mapclientplugins.heartsurfacesegmenterstep.model.node import ENDO, EPI
from mapclientplugins.heartsurfacesegmenterstep.model.image import LONG_AXIS, SHORT_AXIS


class HeartSurfaceSegmenterStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(HeartSurfaceSegmenterStep, self).__init__('Heart Surface Segmenter', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Segmentation'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self._config = {}
        self._config['identifier'] = ''
        self._image_data_long_axis = None
        self._image_data_short_axis = None
        self._view = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        if self._view is None:
            model = HeartSurfaceModel()
            model.setLocation(os.path.join(self._location, self._config['identifier']))
            self._view = HeartSurfaceWidget(model)
            self._view.registerDoneExecution(self._doneExecution)
        else:
            self._view.clear()

        if self._image_data_long_axis is not None:
            self._view.setImageData(LONG_AXIS, self._image_data_long_axis)
        if self._image_data_short_axis is not None:
            self._view.setImageData(SHORT_AXIS, self._image_data_short_axis)

        self._view.initialise()
        
        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 2:
            self._image_data_long_axis = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#images
        else:
            self._image_data_short_axis = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#images

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 0:
            # http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud
            return self._view.getPointCloud(ENDO)
        else:
            # http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud
            return self._view.getPointCloud(EPI)

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


