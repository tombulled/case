# case
String case conversion, identification, parsing and creation

## Styles
| Style    | Example |
| -------- | ------- |
| lower    | foo bar |
| upper    | FOO BAR |
| title    | Foo Bar |
| sentence | Foo bar |
| snake    | foo_bar |
| helter   | Foo_Bar |
| macro    | FOO_BAR |
| kebab    | foo-bar |
| train    | Foo-Bar |
| cobol    | FOO-BAR |
| flat     | foobar  |
| flush    | FOOBAR  |
| pascal   | FooBar  |
| camel    | fooBar  |
| dot      | foo.bar |
| path     | foo/bar |

## Usage
```python
>>> import case
```

### Conversion
```python
>>> case.snake('alphaBRAVOCharlie')
'alpha_bravo_charlie'
```

### Identification
```python
>>> case.identify('FooBar')
[Case(style='pascal')]
```
