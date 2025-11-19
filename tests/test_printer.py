import sys
import unittest

from colorful_print import cp
from colorful_print.constants import Style
from colorful_print.styler import TextStyler


class TestPrinter(unittest.TestCase):

    def test_format_basic_colors(self):
        styler = TextStyler("red")
        result = styler.format("Hello")
        self.assertEqual(result, f"{Style.RED}Hello{Style.END}\n")

        styler = TextStyler("green")
        result = styler.format("World")
        self.assertEqual(result, f"{Style.GREEN}World{Style.END}\n")

        styler = TextStyler("blue")
        result = styler.format("Test")
        self.assertEqual(result, f"{Style.BLUE}Test{Style.END}\n")

    def test_format_with_bold(self):
        styler = TextStyler("red")
        result = styler.format("Bold Text", bold=True)
        expected = f"{Style.BOLD}{Style.RED}Bold Text{Style.END}\n"
        self.assertEqual(result, expected)

    def test_format_with_multiple_styles(self):
        styler = TextStyler("cyan")
        result = styler.format("Styled", bold=True, italic=True, underline=True)
        expected = f"{Style.BOLD}{Style.ITALIC}{Style.UNDERLINE}{Style.CYAN}Styled{Style.END}\n"
        self.assertEqual(result, expected)

    def test_format_with_all_styles(self):
        styler = TextStyler("magenta")
        result = styler.format("Full Style", bold=True, italic=True, underline=True, strike_out=True, reverse=True)
        expected = f"{Style.BOLD}{Style.ITALIC}{Style.UNDERLINE}{Style.STRIKE_OUT}{Style.REVERSE}{Style.MAGENTA}Full Style{Style.END}\n"
        self.assertEqual(result, expected)

    def test_format_with_custom_separator(self):
        styler = TextStyler("yellow")
        result = styler.format("A", "B", "C", sep="-")
        expected = f"{Style.YELLOW}A-B-C{Style.END}\n"
        self.assertEqual(result, expected)

    def test_format_with_custom_end(self):
        styler = TextStyler("white")
        result = styler.format("Text", end="@@\n")
        expected = f"{Style.WHITE}Text{Style.END}@@\n"
        self.assertEqual(result, expected)

    def test_format_multiple_arguments(self):
        styler = TextStyler("green")
        result = styler.format("Hello", 123, [1, 2, 3], sep=" | ")
        expected = f"{Style.GREEN}Hello | 123 | [1, 2, 3]{Style.END}\n"
        self.assertEqual(result, expected)

    def test_printer(self):
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
