# cassidy
String case conversion, identification, parsing and creation

## Usage
```python
>>> import cassidy
```

### Parsing
```python
>>> string = 'MY __mask__ --ofSanityIS.slowly#Slipping'
>>>
>>> cassidy.parse(string)
['my', 'mask', 'of', 'sanity', 'is', 'slowly', 'slipping']
>>>
>>> cassidy.parse(string, case_sensitive = True)
['MY', 'mask', 'of', 'Sanity', 'IS', 'slowly', 'Slipping']
```

### Conversion
```python
>>> cassidy.snake('alphaBRAVOCharlie')
'alpha_bravo_charlie'
```

### Identification
```python
>>> cassidy.identify('FooBar')
[Case(style='pascal')]
```
