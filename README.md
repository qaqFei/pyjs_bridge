# pyjs_bridge

A bridge between Python and JavaScript

```bash
pip install python_js_bridge
```

## sample

```python
import ast

from pyjs_bridge import pyast2jsast, tojseval

pycode = """
from time import time, sleep

def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

async def foo():
    i = 0
    st = time()
    while i < 25:
        print(time(), i, fib(i))
        await sleep(0.1)
        i += 1

foo()
"""

jsast = pyast2jsast(ast.parse(pycode))
with open("out.js", "w", encoding="utf-8") as f:
    f.write(tojseval(jsast))
```

```bash
>>> node out.js
1742608916.119 0 0
1742608916.239 1 1
1742608916.347 2 1
1742608916.457 3 2
1742608916.565 4 3
1742608916.674 5 5
1742608916.782 6 8
1742608916.892 7 13
1742608917.001 8 21
1742608917.11 9 34
1742608917.22 10 55
1742608917.33 11 89
1742608917.438 12 144
1742608917.547 13 233
1742608917.655 14 377
1742608917.764 15 610
1742608917.875 16 987
1742608917.985 17 1597
1742608918.093 18 2584
1742608918.203 19 4181
1742608918.311 20 6765
1742608918.421 21 10946
1742608918.53 22 17711
1742608918.64 23 28657
1742608918.75 24 46368
```
