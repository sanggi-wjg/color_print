from functools import cached_property

from .styler import TextStyler


class ColorfulPrinter(object):

    @cached_property
    def black(self):
        return TextStyler("black")

    @cached_property
    def red(self):
        return TextStyler("red")

    @cached_property
    def green(self):
        return TextStyler("green")

    @cached_property
    def yellow(self):
        return TextStyler("yellow")

    @cached_property
    def blue(self):
        return TextStyler("blue")

    @cached_property
    def magenta(self):
        return TextStyler("magenta")

    @cached_property
    def cyan(self):
        return TextStyler("cyan")

    @cached_property
    def white(self):
        return TextStyler("white")

    @cached_property
    def bright_black(self):
        return TextStyler("bright_black")

    @cached_property
    def bright_red(self):
        return TextStyler("bright_red")

    @cached_property
    def bright_green(self):
        return TextStyler("bright_green")

    @cached_property
    def bright_yellow(self):
        return TextStyler("bright_yellow")

    @cached_property
    def bright_blue(self):
        return TextStyler("bright_blue")

    @cached_property
    def bright_magenta(self):
        return TextStyler("bright_magenta")

    @cached_property
    def bright_cyan(self):
        return TextStyler("bright_cyan")

    @cached_property
    def bright_white(self):
        return TextStyler("bright_white")
