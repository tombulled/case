# case
Case Styles

## Usage
```python
import case

string: str = 'MY __mask__ --ofSanityIS.slowly#Slipping'
```

### Parsers

#### `parse`
```python
>>> case.parse(string)
['MY', 'mask', 'of', 'Sanity', 'IS', 'slowly', 'Slipping']
```

### Translators

#### `lower`
```python
>>> case.translators.lower(['FoO', 'BAr'])
['foo', 'bar']
```

#### `upper`
```python
>>> case.translators.upper(['FoO', 'BAr'])
['FOO', 'BAR']
```

#### `title`
```python
>>> case.translators.title(['FoO', 'BAr'])
['Foo', 'Bar']
```

#### `swapcase`
```python
>>> case.translators.swapcase(['FoO', 'BAr'])
['fOo', 'baR']
```

#### `capitalize`
```python
>>> case.translators.capitalize(['FoO', 'BAr'])
['Foo', 'bar']
```

#### `dromedary`
```python
>>> case.translators.dromedary(['FoO', 'BAr'])
['foo', 'Bar']
```

#### `alternating`
```python
>>> case.translators.alternating(['FoO', 'BAr'])
['fOo', 'BaR']
```

#### `sponge`
```python
>>> case.translators.sponge(['FoO', 'BAr'])
['FOo', 'bAR']
```

### Renderers

#### `space`
```python
>>> case.renderers.space(['foo', 'bar'])
'foo bar'
```

#### `concatenate`
```python
>>> case.renderers.concatenate(['foo', 'bar'])
'foobar'
```

#### `underscore`
```python
>>> case.renderers.underscore(['foo', 'bar'])
'foo_bar'
```

#### `hyphen`
```python
>>> case.renderers.hyphen(['foo', 'bar'])
'foo-bar'
```

#### `period`
```python
>>> case.renderers.period(['foo', 'bar'])
'foo.bar'
```

#### `slash`
```python
>>> case.renderers.slash(['foo', 'bar'])
'foo/bar'
```

### Styles

#### `lower`
```python
>>> case.lower(string)
'my mask of sanity is slowly slipping'
>>>
```

#### `upper`
```python
>>> case.upper(string)
'MY MASK OF SANITY IS SLOWLY SLIPPING'
>>>
```

#### `title`
```python
>>> case.title(string)
'My Mask Of Sanity Is Slowly Slipping'
>>>
```

#### `sentence`
```python
>>> case.sentence(string)
'My mask of sanity is slowly slipping'
```

#### `snake`
```python
>>> case.snake(string)
'my_mask_of_sanity_is_slowly_slipping'
```

#### `helter`
```python
>>> case.helter(string)
'My_Mask_Of_Sanity_Is_Slowly_Slipping'
```

#### `macro`
```python
>>> case.macro(string)
'MY_MASK_OF_SANITY_IS_SLOWLY_SLIPPING'
```

#### `flat`
```python
>>> case.flat(string)
'mymaskofsanityisslowlyslipping'
```

#### `flush`
```python
>>> case.flush(string)
'MYMASKOFSANITYISSLOWLYSLIPPING'
```

#### `camel`
```python
>>> case.camel(string)
'myMaskOfSanityIsSlowlySlipping'
```

#### `pascal`
```python
>>> case.pascal(string)
'MyMaskOfSanityIsSlowlySlipping'
```

#### `kebab`
```python
>>> case.kebab(string)
'my-mask-of-sanity-is-slowly-slipping'
```

#### `train`
```python
>>> case.train(string)
'My-Mask-Of-Sanity-Is-Slowly-Slipping'
```

#### `cobol`
```python
>>> case.cobol(string)
'MY-MASK-OF-SANITY-IS-SLOWLY-SLIPPING'
```

#### `dot`
```python
>>> case.dot(string)
'my.mask.of.sanity.is.slowly.slipping'
```

#### `path`
```python
>>> case.path(string)
'my/mask/of/sanity/is/slowly/slipping'
```
