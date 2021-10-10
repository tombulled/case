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

#### Lower
```python
>>> case.lower(string)
'my mask of sanity is slowly slipping'
>>>
```

#### Upper
```python
>>> case.upper(string)
'MY MASK OF SANITY IS SLOWLY SLIPPING'
>>>
```

#### Title
```python
>>> case.title(string)
'My Mask Of Sanity Is Slowly Slipping'
>>>
```

#### Sentence
```python
>>> case.sentence(string)
'My mask of sanity is slowly slipping'
```

#### Snake
```python
>>> case.snake(string)
'my_mask_of_sanity_is_slowly_slipping'
```

#### Helter
```python
>>> case.helter(string)
'My_Mask_Of_Sanity_Is_Slowly_Slipping'
```

#### Macro
```python
>>> case.macro(string)
'MY_MASK_OF_SANITY_IS_SLOWLY_SLIPPING'
```

#### Flat
```python
>>> case.flat(string)
'mymaskofsanityisslowlyslipping'
```

#### Flush
```python
>>> case.flush(string)
'MYMASKOFSANITYISSLOWLYSLIPPING'
```

#### Camel
```python
>>> case.camel(string)
'myMaskOfSanityIsSlowlySlipping'
```

#### Pascal
```python
>>> case.pascal(string)
'MyMaskOfSanityIsSlowlySlipping'
```

#### Kebab
```python
>>> case.kebab(string)
'my-mask-of-sanity-is-slowly-slipping'
```

#### Train
```python
>>> case.train(string)
'My-Mask-Of-Sanity-Is-Slowly-Slipping'
```

#### Cobol
```python
>>> case.cobol(string)
'MY-MASK-OF-SANITY-IS-SLOWLY-SLIPPING'
```

#### Dot
```python
>>> case.dot(string)
'my.mask.of.sanity.is.slowly.slipping'
```

#### Path
```python
>>> case.path(string)
'my/mask/of/sanity/is/slowly/slipping'
```
