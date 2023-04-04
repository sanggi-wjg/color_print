from colorful_print import color


def colorful_dispatcher(c: str, msg: str, *args, **kwargs):
    dispatch = getattr(color, c)
    dispatch(msg, *args, **kwargs)


def red(msg: str, *args, **kwargs):
    colorful_dispatcher('red', msg, *args, **kwargs)


def yellow(msg: str, *args, **kwargs):
    colorful_dispatcher('yellow', msg, *args, **kwargs)


red('123', 456, italic=True)
yellow('789', 123.456, italic=True, bold=True)
