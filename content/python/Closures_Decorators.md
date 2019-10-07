Title: Closure and Decorators
Date: 2019-10-06
Category: Python
Tags: Python Foundation
Summary: Study note from pluralsight


<details>
<summary>Local Functions </summary>

```python
store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)
```

```python
sort_by_last_letter(['a','c','b'])
<function sort_by_last_letter.<locals>.last_letter at 0x102a149e0>
Out[5]: ['a', 'b', 'c']
sort_by_last_letter(['a','c','b'])
<function sort_by_last_letter.<locals>.last_letter at 0x102a14950>
Out[6]: ['a', 'b', 'c']
sort_by_last_letter(['a','c','b'])
<function sort_by_last_letter.<locals>.last_letter at 0x102a14b00>
Out[7]: ['a', 'b', 'c']
```

The main point here is that the def call in **sort_by_last_letter** is no different from any other name binding in the function, and a new function is created each time def is executed.
  

    
</details>

Remember the ***LEGB*** rule for name lookup. First the local scope is checked, then the enclosing scope, next the global scope, and finally the built-in scope.  

* useful for specialized, one-off functions
* Aid in code organization and readability
* Similar to lambdas, but more general
    *   May contain multiple expressions
    *   May contain statements