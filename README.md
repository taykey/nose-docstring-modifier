### nose-docstring-plugin

This plugin enables you to modify docstring of tests based on their attributes, for example:
```
@attr(section='section', type='functional+', module='module', id=1)
def test_function(self):
    """
    This is the original docstring
    """
    pass
```

Running this with nosetest with docstring plugin:

```> python main.py --with-docstring --prefix=id,section --suffix=type```

will print 

```(1, section) This is the original docstring (functional+) ... ok```



