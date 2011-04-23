from Globals import InitializeClass
from persistent.list import PersistentList

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class Framework(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'CloudFoundryFramework'

    cfName = ''
    cfDetection = PersistentList()

    _properties = ManagedEntity._properties + (
        {'id': 'cfName', 'type': 'string', 'mode': ''},
        {'id': 'cfDetection', 'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('cfEndpoint', ToOne(ToManyCont,
            'ZenPacks.zenoss.CloudFoundry.Endpoint.Endpoint',
            'cfFrameworks'
            )
        ),
        ('cfRuntimes', ToManyCont(ToOne,
            'ZenPacks.zenoss.CloudFoundry.Runtime.Runtime',
            'cfFramework'
            )
        ),
        ('cfAppServers', ToManyCont(ToOne,
            'ZenPacks.zenoss.CloudFoundry.AppServer.AppServer',
            'cfFramework'
            )
        ),
    )

    def device(self):
        return self.cfEndpoint()

    def getCFDetection(self):
        return self.cfDetection

    def setCFDetection(self, detection):
        self.cfDetection = PersistentList(detection)

InitializeClass(Framework)

