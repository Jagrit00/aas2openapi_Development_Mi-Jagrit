from enum import Enum


class SubmodelElementListTypeValueListElement(str, Enum):
    ANNOTATED_RELATIONSHIP_ELEMENT = "ANNOTATED_RELATIONSHIP_ELEMENT"
    BASIC_EVENT_ELEMENT = "BASIC_EVENT_ELEMENT"
    BLOB = "BLOB"
    CAPABILITY = "CAPABILITY"
    DATA_ELEMENT = "DATA_ELEMENT"
    ENTITY = "ENTITY"
    EVENT_ELEMENT = "EVENT_ELEMENT"
    FILE = "FILE"
    MULTI_LANGUAGE_PROPERTY = "MULTI_LANGUAGE_PROPERTY"
    OPERATION = "OPERATION"
    PROPERTY = "PROPERTY"
    RANGE = "RANGE"
    REFERENCE_ELEMENT = "REFERENCE_ELEMENT"
    RELATIONSHIP_ELEMENT = "RELATIONSHIP_ELEMENT"
    SUBMODEL_ELEMENT = "SUBMODEL_ELEMENT"
    SUBMODEL_ELEMENT_COLLECTION = "SUBMODEL_ELEMENT_COLLECTION"
    SUBMODEL_ELEMENT_LIST = "SUBMODEL_ELEMENT_LIST"

    def __str__(self) -> str:
        return str(self.value)
