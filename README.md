# Python Colorful Print

[![✅Build And Test](https://github.com/sanggi-wjg/color_print/actions/workflows/build-test.yml/badge.svg?branch=main)](https://github.com/sanggi-wjg/color_print/actions/workflows/build-test.yml)
[![PyPI version](https://badge.fury.io/py/colorful_print.svg)](https://badge.fury.io/py/colorful_print)
[![PyPI](https://img.shields.io/pypi/pyversions/colorful_print.svg)](https://pypi.python.org/pypi/colorful_print)
<br/>
[![CodeFactor](https://www.codefactor.io/repository/github/sanggi-wjg/color_print/badge)](https://www.codefactor.io/repository/github/sanggi-wjg/color_print)
[![PyPI](https://img.shields.io/pypi/dm/colorful-print.svg)](https://pypi.org/project/colorful-print/)

![](.images/s2da8d9.png)

## Install

```shell
pip install colorful_print
```

## Usage

```python
import sys
from colorful_print import cp

a = [1, "a", 2.345]
b = (4, "b", 5.678)
c = {"John": "Doe", "age": 20}

cp.black("This is Black", a, b, c)
cp.bright_black("This is Bright Black", a, b, c)
cp.red("This is Red", a, b, c)
cp.bright_red("This is Bright Red", a, b, c)
cp.green("This is Green", a, b, c)
cp.bright_green("This is Bright Green", a, b, c)
cp.yellow("This is Yellow", a, b, c)
cp.yellow("This is Bright Yellow", a, b, c)
cp.blue("This is Blue", a, b, c)
cp.bright_blue("This is Bright Blue", a, b, c)
cp.magenta("This is Magenta", a, b, c)
cp.bright_magenta("This is Bright Magenta", a, b, c)
cp.cyan("This is Cyan", a, b, c)
cp.bright_cyan("This is Bright Cyan", a, b, c)
cp.white("This is White", a, b, c)
cp.bright_white("This is Bright White", a, b, c)
sys.stdout.write("\n")

cp.red("This is Red", a, b, c)
cp.green("This is Bold Green", a, b, c, bold=True)
cp.yellow("This is Bold Italic Yellow", a, b, c, bold=True, italic=True)
cp.blue("This is Bold Italic Underline Blue", a, b, c, bold=True, italic=True, underline=True)
cp.magenta(
    "This is Bold Italic Underline StrikeOut Magenta",
    a,
    b,
    c,
    bold=True,
    italic=True,
    underline=True,
    strike_out=True,
)
cp.cyan(
    "This is Bold Italic Underline Reverse Cyan", a, b, c, bold=True, italic=True, underline=True, reverse=True
)
cp.white(
    "This is Bold Italic Underline StrikeOut Reverse White",
    a,
    b,
    c,
    bold=True,
    italic=True,
    underline=True,
    strike_out=True,
    reverse=True,
)
sys.stdout.write("\n")

cp.black("This is Black", a, b, c, sep="\t\t", end="@@ \n\n", flush=True)
cp.red("This is Red", a, b, c, sep="\t\t", end="@@ \n\n", flush=True)
cp.green("This is Green", a, b, c, sep="\t\t", end="@@ \n\n", flush=True)
```
