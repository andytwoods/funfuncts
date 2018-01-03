# FunFuncts

Experimenting with chainable functional coding in Python. For lists and dicts.
## Getting Started


Install locally

```
pip install git+git://github.com/andytwoods/funfuncts
```

Lets import
```
from funfuncts.funfuncts import fdict, flist

```


Then start using
```
l = [1,2,3]
flist(l)
    .filter(lambda v: v>1) /
    .map(lambda v: v+1)
# [3,4]

```

With a dict input:
```
d = {'a': 1, 'b': 2}
fdict(d).map(lambda val, key: str(val)+key, {})
# {'a': '1a', 'b': '2b'}
```
All 3 functional tools:
```
fd = fdist({'a': 1, 'b': 2, 'c': 3})
result = fd \
    .filter(lambda val, key: val > 1) \
    .map(lambda val, key: key+str(val)) \
    .reduce(lambda accumulating, val, key: accumulating + val)
# 'b2c3'
 ```


