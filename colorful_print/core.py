import sys

from .exceptions import ColorPrintException
from .style import Style


class ColorString(object):

    def __init__(self, style: str):
        self.style = style

    def __call__(self, *args, **kwargs):
        try:
            string = self.format(*args, **kwargs)
        except AttributeError:
            raise ColorPrintException('{} not exist'.format(self.style))
        except Exception as e:
            raise ColorPrintException(e)

        sys.stdout.write(string)

    def format(self, *args, **kwargs):
        seperator = kwargs.get('sep', ' ')
        string = '{}{}{}'.format(getattr(Style, self.style.upper()), seperator.join(map(str, args)), Style.END)

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

        string = '{}{}'.format(string, kwargs.get('end', '\n'))
        if kwargs.get('flush', False):
            sys.stdout.flush()

        return string


class ColorPrint(object):

    def __getattribute__(self, style: str):
        return ColorString(style)
