### nose-docstring-plugin

This plugin enables you to modify docstring of tests based on their attributes, for example:
```python
@attr(section='MySection', type='functional+', module='MyModule', id=1)
def test_function(self):
    """
    This is the original docstring
    """
    pass
```

Running this with nosetest with docstring plugin:

```> python main.py --with-docstring-modifier --prefix=id,section --suffix=type --replace=s,S```

will print 

```(1, MySection) ThiS iS the original docString (functional+) ... ok```



