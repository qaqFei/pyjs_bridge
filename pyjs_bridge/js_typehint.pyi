import typing

globalThis: typing.Any
Infinity = float("inf")
NaN = float("nan")
undefined = object()

def eval(code: str) -> typing.Any: ...
def isFinite(value: typing.Any) -> bool: ...
def isNaN(value: typing.Any) -> bool: ...
def parseFloat(string: str) -> float: ...
def parseInt(string: str, radix: int) -> int: ...
def decodeURI(encodedURI: str) -> str: ...
def decodeURIComponent(encodedURIComponent: str) -> str: ...
def encodeURI(uri: str) -> str: ...
def encodeURIComponent(uriComponent: str) -> str: ...
def escape(string: str) -> str: ...
def unescape(string: str) -> str: ...

Object = object
Function = typing.Callable
Boolean = bool
Symbol = type("Symbol")

Error = type("Error", (object, ), {})
AggregateError = type("AggregateError", (Error, ), {})
EvalError = type("EvalError", (Error, ), {})
RangeError = type("RangeError", (Error, ), {})
ReferenceError = type("ReferenceError", (Error, ), {})
SyntaxError = type("SyntaxError", (Error, ), {})
TypeError = type("TypeError", (Error, ), {})
URIError = type("URIError", (Error, ), {})
InternalError = type("InternalError", (Error, ), {})

Number = float
BigInt = int
Math = object()
Date = object()

String = str
RegExp = object()

Array = list
Int8Array = list
Uint8Array = list
Uint8ClampedArray = list
Int16Array = list
Uint16Array = list
Int32Array = list
Uint32Array = list
BigInt64Array = list
BigUint64Array = list
Float32Array = list
Float64Array = list

Map = dict
Set = set
WeakMap = dict
WeakSet = set

ArrayBuffer = object
SharedArrayBuffer = object
Atomics = object
DataView = object
JSON = object

WeakRef = object
FinalizationRegistry = object

Iterator = typing.Iterator
AsyncIterator = typing.AsyncIterator
Promise = object
GeneratorFunction = typing.Callable
AsyncGeneratorFunction = typing.Callable
Generator = typing.Iterator
AsyncGenerator = typing.AsyncIterator
AsyncFunction = typing.Callable

Reflect = object
Proxy = object

Intl = object

PyPromise = Promise
PyProxy = Proxy

del typing
