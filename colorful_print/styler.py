import sys

from .constants import Style


class TextStyler:

    def __init__(self, style: str):
        self.style = style

    def __call__(self, *args, **kwargs):
        try:
            sys.stdout.write(self.format(*args, **kwargs))
            if kwargs.get("flush", False):
                sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"[ColorfulPrint] Failed to print: {e}.")

    def format(self, *args, **kwargs):
        separator = kwargs.get("sep", " ")
        end = kwargs.get("end", "\n")
        content = separator.join(map(str, args))

        styles = []
        if kwargs.get("bold", False):
            styles.append(Style.BOLD)

        if kwargs.get("italic", False):
            styles.append(Style.ITALIC)

        if kwargs.get("underline", False):
            styles.append(Style.UNDERLINE)

        if kwargs.get("strike_out", False):
            styles.append(Style.STRIKE_OUT)

        if kwargs.get("reverse", False):
            styles.append(Style.REVERSE)

        styles.append(getattr(Style, self.style.upper()))
        return f"{''.join(styles)}{content}{Style.END}{end}"
