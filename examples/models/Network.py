from __future__ import annotations
from enum import Enum
from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

from models.Layer1 import KPI
from models.Layer1 import Product
from models.Layer1 import Order
from models.Layer1 import Process
from models.Layer1 import Resource
from models.Layer1 import Capability


class Sub_KPI(SubmodelElementCollection):
    placeholder: str
    
class Network_KPI(KPI):
    KPI_Type: str
    Sub_KPI: Sub_KPI

#------------------------------------------------------#

class measurements_in_cm(SubmodelElementCollection):
   placeholder_list = list()


class Material(SubmodelElementCollection):
    
    name: str
    cost: str

class subComponent(SubmodelElementCollection):
    #placeholder: str
    pass

class Component(SubmodelElementCollection):
    name:str
    subComponent:subComponent
    cost:str
    transfer_price:str
    measurements_in_cm:measurements_in_cm
    weight:str
    time_stamp_lastprocess:str


class Network_Product(Product):
    name: str
    measurements_in_cm: measurements_in_cm
    Material: Material
    Component: Component
    cost: str
    product_generation: str
#--------------------------------------------------------#
class statusEnum(Enum):
    preparing = 1
    in_progress=2

class orderStatus(SubmodelElementCollection):
    
    # preparing = 1
    # in_progress = 2
    # finished = 3
    # failed = 4
    Status = statusEnum
    neifu = []
   # Status = ["preparing","in_progress","finished","failed"]
    # class status (Enum):
    #     preparing = 1
    #     in_progress = 2
    #     finished = 3
    #     failed = 4
   


class OrderType(SubmodelElementCollection):
    pass
    #SuppliedOrder: str
    #CustomOrder: str
    #ProductionOrder: str
    #TransportOrder: str
    #StoreOrder:str

class Network_Order(Order):
    position:str
    orderStatus:orderStatus
    priority:str
    OrderType:OrderType
#----------------------------------------------------------#
class subProcesses(SubmodelElementCollection):
   pass 


class ProcessStatus(SubmodelElementCollection):
    pass
    #preparing: str
    #in_progress: str
    #finsihed: str
    #failed: str


class ProcessType(SubmodelElementCollection):

    Transport: str
    Production: str

class Network_Process(Process):
    subProcesses:subProcesses
    process_time:str
    process_cost:str
    ProcessStatus:ProcessStatus
    processType:ProcessType
#------------------------------------------------------#
class subResources(SubmodelElementCollection):
    placeholder: str

class OrganisationType(SubmodelElementCollection):
    InternalOrga:str
    ExternalOrga:str

class Organisation(SubmodelElementCollection):
    OrganisationType:List[OrganisationType]

class ResourceType(SubmodelElementCollection):
    Network:str
    TransportUnit:str
    LocationNode:str

class Network_Resource(Resource):
    subResources:subResources
    Organisation:Organisation
    ResourceType:List[ResourceType]
#---------------------------------------------------------#
class subCapabilities(SubmodelElementCollection):
    placeholder: str

class inherentCapability(SubmodelElementCollection):
    TransportCapability:str
    ProductionCapability:str

class CapabilityType(SubmodelElementCollection):
    subCapabilities:subCapabilities
    inherentCapability:List[inherentCapability]

class Network_Capability(Capability):
    CapabilityType:CapabilityType

    
#-------------------------------------------------------#
class Network(AAS):
    KPI: Network_KPI
    Product: Network_Product
    Order: Network_Order
    #Process: Network_Process
    #Resource: Network_Resource
    #Capability: Network_Capability

