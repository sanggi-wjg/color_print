# color_print

[![PyPI version](https://badge.fury.io/py/colorful_print.svg)](https://badge.fury.io/py/colorful_print)
[![PyPI](https://img.shields.io/pypi/pyversions/colorful_print.svg)](https://pypi.python.org/pypi/colorful_print)

Example

![colorful example](tests/example.png)

```python
from colorful_print import color

color.black('Print Black')
color.red('Print Red')
color.green('Print Green')
color.yellow('Print Yellow')
color.blue('Print Blue')
color.magenta('Print Magenta')
color.cyan('Print Cyan')
color.white('Print White')

print()
color.red('Print Red')
color.green('Print Bold Green', bold = True)
color.yellow('Print Bold Italic Yellow', bold = True, italic = True)
color.blue('Print Bold Italic Underline Blue', bold = True, italic = True, underline = True)
color.magenta('Print Bold Italic Underline StrikeOut Magenta', bold = True, italic = True, underline = True, strike_out = True)
color.cyan('Print Bold Italic Underline Reverse Cyan', bold = True, italic = True, underline = True, reverse = True)
color.white('Print Bold Italic Underline StrikeOut Reverse White', bold = True, italic = True, underline = True, strike_out = True, reverse = True)
```

```python
from colorful_print import color

def colorful_dispatcher(c: str, msg: str, *args, **kwargs):
    dispatch = getattr(color, c)
    dispatch(msg, *args, **kwargs)

def _red(msg: str, *args, **kwargs):
    colorful_dispatcher('red', msg, *args, **kwargs)

def _yellow(msg: str, *args, **kwargs):
    colorful_dispatcher('yellow', msg, *args, **kwargs)

_red('123', 456, italic = True)
_yellow('789', 123.456, italic = True, bold = True)
```


Usage
```shell script
pip install colorful_print
```

