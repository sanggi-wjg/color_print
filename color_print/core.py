from .exceptions import ColorPrintException
from .style import Style


class ColorString(object):

    def __init__(self, style: str):
        self.style = style

        if '_' in style:
            style = style.split('_')
            self.type = style[0]
            self.color = style[1]
        else:
            self.color = style

    def __call__(self, *args, **kwargs):
        try:
            print('{}{}{}'.format(
                getattr(Style, self.color.upper()), *args, Style.END),
            )
        except AttributeError:
            raise ColorPrintException('{} not exist'.format(self.style))


class ColorPrint(object):

    def __init__(self, do_print: bool = True):
        self.do_print = do_print

    def disable(self):
        pass

    def __getattribute__(self, style: str):
        return ColorString(style)
