# case
Case Styles

## Usage
```python
>>> import case
>>>
>>> case.parse('toBe.ORNot  to_ -be')
['to', 'be', 'or', 'not', 'to', 'be']
>>>
>>> case.snake('we CAME&weSaw-we+Conquered')
'we_came_we_saw_we_conquered'
>>>
```
