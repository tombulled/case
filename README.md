# case
Case Styles

## Usage
```python
>>> import case
>>>
>>> string: str = 'MY __mask__ --ofSanityIS.slowly#Slipping'
>>>
>>> case.parse(string)
['my', 'mask', 'of', 'sanity', 'is', 'slowly', 'slipping']
>>>
```

### Lower
```python
>>> case.lower(string)
'my mask of sanity is slowly slipping'
>>>
```

### Upper
```python
>>> case.upper(string)
'MY MASK OF SANITY IS SLOWLY SLIPPING'
>>>
```

### Title
```python
>>> case.title(string)
'My Mask Of Sanity Is Slowly Slipping'
>>>
```

### Sentence
```python
>>> case.sentence(string)
'My mask of sanity is slowly slipping'
```

### Snake
```python
>>> case.snake(string)
'my_mask_of_sanity_is_slowly_slipping'
```

### Helter
```python
>>> case.helter(string)
'My_Mask_Of_Sanity_Is_Slowly_Slipping'
```

### Macro
```python
>>> case.macro(string)
'MY_MASK_OF_SANITY_IS_SLOWLY_SLIPPING'
```

### Flat
```python
>>> case.flat(string)
'mymaskofsanityisslowlyslipping'
```

### Flush
```python
>>> case.flush(string)
'MYMASKOFSANITYISSLOWLYSLIPPING'
```

### Camel
```python
>>> case.camel(string)
'myMaskOfSanityIsSlowlySlipping'
```

### Pascal
```python
>>> case.pascal(string)
'MyMaskOfSanityIsSlowlySlipping'
```

### Kebab
```python
>>> case.kebab(string)
'my-mask-of-sanity-is-slowly-slipping'
```

### Train
```python
>>> case.train(string)
'My-Mask-Of-Sanity-Is-Slowly-Slipping'
```

### Cobol
```python
>>> case.cobol(string)
'My-Mask-Of-Sanity-Is-Slowly-Slipping'
```

### Dot
```python
>>> case.dot(string)
'my.mask.of.sanity.is.slowly.slipping'
```

### Path
```python
>>> case.path(string)
'my/mask/of/sanity/is/slowly/slipping'
```
