from _typeshed import Incomplete

__all__ = ["MetaData", "loadarff", "ArffError", "ParseArffError"]

class ArffError(OSError): ...
class ParseArffError(ArffError): ...

class Attribute:
    type_name: Incomplete
    name: Incomplete
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> None: ...
    def parse_data(self, data_str) -> None: ...

class NominalAttribute(Attribute):
    type_name: str
    values: Incomplete
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name, values) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...
    def parse_data(self, data_str): ...

class NumericAttribute(Attribute):
    type_name: str
    dtype: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...
    def parse_data(self, data_str): ...

class StringAttribute(Attribute):
    type_name: str
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...

class DateAttribute(Attribute):
    date_format: Incomplete
    datetime_unit: Incomplete
    type_name: str
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name, date_format, datetime_unit) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...
    def parse_data(self, data_str): ...

class RelationalAttribute(Attribute):
    type_name: str
    dtype: Incomplete
    attributes: Incomplete
    dialect: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string): ...
    def parse_data(self, data_str): ...

class MetaData:
    name: Incomplete
    def __init__(self, rel, attr) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def names(self): ...
    def types(self): ...

def loadarff(f): ...
