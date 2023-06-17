from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ["col1", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17", "col18", "col19", "col2", "col20", "col3", "col4", "col5", "col6", "col7", "col8", "col9"]
    COL10_FIELD_NUMBER: _ClassVar[int]
    COL11_FIELD_NUMBER: _ClassVar[int]
    COL12_FIELD_NUMBER: _ClassVar[int]
    COL13_FIELD_NUMBER: _ClassVar[int]
    COL14_FIELD_NUMBER: _ClassVar[int]
    COL15_FIELD_NUMBER: _ClassVar[int]
    COL16_FIELD_NUMBER: _ClassVar[int]
    COL17_FIELD_NUMBER: _ClassVar[int]
    COL18_FIELD_NUMBER: _ClassVar[int]
    COL19_FIELD_NUMBER: _ClassVar[int]
    COL1_FIELD_NUMBER: _ClassVar[int]
    COL20_FIELD_NUMBER: _ClassVar[int]
    COL2_FIELD_NUMBER: _ClassVar[int]
    COL3_FIELD_NUMBER: _ClassVar[int]
    COL4_FIELD_NUMBER: _ClassVar[int]
    COL5_FIELD_NUMBER: _ClassVar[int]
    COL6_FIELD_NUMBER: _ClassVar[int]
    COL7_FIELD_NUMBER: _ClassVar[int]
    COL8_FIELD_NUMBER: _ClassVar[int]
    COL9_FIELD_NUMBER: _ClassVar[int]
    col1: float
    col10: float
    col11: float
    col12: float
    col13: float
    col14: float
    col15: float
    col16: float
    col17: float
    col18: float
    col19: float
    col2: float
    col20: float
    col3: float
    col4: float
    col5: float
    col6: float
    col7: float
    col8: float
    col9: float
    def __init__(self, col1: _Optional[float] = ..., col2: _Optional[float] = ..., col3: _Optional[float] = ..., col4: _Optional[float] = ..., col5: _Optional[float] = ..., col6: _Optional[float] = ..., col7: _Optional[float] = ..., col8: _Optional[float] = ..., col9: _Optional[float] = ..., col10: _Optional[float] = ..., col11: _Optional[float] = ..., col12: _Optional[float] = ..., col13: _Optional[float] = ..., col14: _Optional[float] = ..., col15: _Optional[float] = ..., col16: _Optional[float] = ..., col17: _Optional[float] = ..., col18: _Optional[float] = ..., col19: _Optional[float] = ..., col20: _Optional[float] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OrderResponse(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...
