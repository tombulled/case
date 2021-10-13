# case
String case conversion, identification, parsing and creation

## Usage
```python
>>> import case
```

### Parsing
```python
>>> string = 'MY __mask__ --ofSanityIS.slowly#Slipping'
>>>
>>> case.parse(string)
['MY', 'mask', 'of', 'Sanity', 'IS', 'slowly', 'Slipping']
>>>
>>> case.parse(string, case_sensitive = False)
['my', 'mask', 'of', 'sanity', 'is', 'slowly', 'slipping']
```

### Identification
```python
>>> case.identify('FooBar')
[Case(style='pascal')]
```

### Conversion
```python
>>> case.camel('alphaBRAVOCharlie')
'alphaBravoCharlie'
```

### Translation
```python
>>> case.translators.alternating(['foo', 'bar'])
['fOo', 'BaR']
```

### Rendering
```python
>>> case.renderers.underscore(['foo', 'bar'])
'foo_bar'
```
