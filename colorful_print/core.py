import sys

from .exceptions import ColorPrintException
from .style import Style


class ColorString(object):

    def __init__(self, style: str):
        self.style = style

    def __call__(self, *args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        file = kwargs.get('file', sys.stdout)
        flush = kwargs.get('flush', False)

        try:
            string = self.format(*args, **kwargs)
        except AttributeError:
            raise ColorPrintException('{} not exist'.format(self.style))

        print(string, sep = sep, end = end, file = file, flush = flush)

    def format(self, *args, **kwargs):
        string = '{}{}{}'.format(getattr(Style, self.style.upper()), ' '.join(map(str, args)), Style.END)

        if kwargs.get('bold', False):
            string = '{}{}{}'.format(getattr(Style, 'BOLD'), string, Style.END)

        if kwargs.get('italic', False):
            string = '{}{}{}'.format(getattr(Style, 'ITALIC'), string, Style.END)

        if kwargs.get('underline', False):
            string = '{}{}{}'.format(getattr(Style, 'UNDERLINE'), string, Style.END)

        if kwargs.get('strike_out', False):
            string = '{}{}{}'.format(getattr(Style, 'STRIKE_OUT'), string, Style.END)

        if kwargs.get('reverse', False):
            string = '{}{}{}'.format(getattr(Style, 'REVERSE'), string, Style.END)

        return string


class ColorPrint(object):

    def __getattribute__(self, style: str):
        return ColorString(style)
