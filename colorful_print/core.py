from .exceptions import ColorPrintException
from .style import Style


class ColorString(object):

    def __init__(self, style: str):
        self.style = style

    def __call__(self, *args, **kwargs):
        try:
            print('{}{}{}'.format(
                getattr(Style, self.style.upper()),
                ' '.join(args),
                Style.END
            ))
        except AttributeError:
            raise ColorPrintException('{} not exist'.format(self.style))


class ColorPrint(object):

    def __getattribute__(self, style: str):
        return ColorString(style)
