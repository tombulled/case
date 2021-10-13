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
['my', 'mask', 'of', 'sanity', 'is', 'slowly', 'slipping']
>>>
>>> case.parse(string, case_sensitive = True)
['MY', 'mask', 'of', 'Sanity', 'IS', 'slowly', 'Slipping']
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
