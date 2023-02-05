from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["sendcommandflag"]
    SENDCOMMANDFLAG_FIELD_NUMBER: _ClassVar[int]
    sendcommandflag: str
    def __init__(self, sendcommandflag: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["data_array"]
    DATA_ARRAY_FIELD_NUMBER: _ClassVar[int]
    data_array: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, data_array: _Optional[_Iterable[float]] = ...) -> None: ...
