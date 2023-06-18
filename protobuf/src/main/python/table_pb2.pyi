from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cell(_message.Message):
    __slots__ = ["floatVal", "intVal", "stringVal"]
    FLOATVAL_FIELD_NUMBER: _ClassVar[int]
    INTVAL_FIELD_NUMBER: _ClassVar[int]
    STRINGVAL_FIELD_NUMBER: _ClassVar[int]
    floatVal: float
    intVal: int
    stringVal: str
    def __init__(self, floatVal: _Optional[float] = ..., intVal: _Optional[int] = ..., stringVal: _Optional[str] = ...) -> None: ...

class Column(_message.Message):
    __slots__ = ["floatColumn", "intColumn", "name", "stringColumn"]
    FLOATCOLUMN_FIELD_NUMBER: _ClassVar[int]
    INTCOLUMN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRINGCOLUMN_FIELD_NUMBER: _ClassVar[int]
    floatColumn: FloatColumn
    intColumn: IntColumn
    name: str
    stringColumn: StringColumn
    def __init__(self, name: _Optional[str] = ..., floatColumn: _Optional[_Union[FloatColumn, _Mapping]] = ..., intColumn: _Optional[_Union[IntColumn, _Mapping]] = ..., stringColumn: _Optional[_Union[StringColumn, _Mapping]] = ...) -> None: ...

class ColumnBasedTable(_message.Message):
    __slots__ = ["cols"]
    COLS_FIELD_NUMBER: _ClassVar[int]
    cols: _containers.RepeatedCompositeFieldContainer[Column]
    def __init__(self, cols: _Optional[_Iterable[_Union[Column, _Mapping]]] = ...) -> None: ...

class FloatColumn(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class IntColumn(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Cell]
    def __init__(self, values: _Optional[_Iterable[_Union[Cell, _Mapping]]] = ...) -> None: ...

class RowBasedTable(_message.Message):
    __slots__ = ["columnNames", "rows"]
    COLUMNNAMES_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columnNames: _containers.RepeatedScalarFieldContainer[str]
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, columnNames: _Optional[_Iterable[str]] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...

class StringColumn(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class TableRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
