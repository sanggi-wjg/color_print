class Style:
    """
    https://github.com/lambdaisland/ansi/blob/master/src/lambdaisland/ansi.cljc
    https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#rgb-colors

    Color 	Foreground Color Code	Background Color Code
    Black	        30	                    40
    Red	            31	                    41
    Green	        32	                    42
    Yellow	        33	                    43
    Blue	        34	                    44
    Magenta	        35	                    45
    Cyan	        36	                    46
    White	        37	                    47
    Bright Black    90                      100
    Bright Red      91                      101
    Bright Green    92                      102
    Bright Yellow   93                      103
    Bright Blue     94                      104
    Bright Magenta  95                      105
    Bright Cyan     96                      106
    Bright White    97                      107

    Bold                       1
    Italic                     3
    Underline                  4
    Reverse(Font/Background)   7
    Strike Out                 9
    Remove Bold                22
    Remove Italic              23
    Remove Underline           24
    Remove Reverse             27
    Remove Strike-Out          29
    """

    END = "\033[0m"

    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"
    STRIKE_OUT = "\033[9m"

    # Standard colors (30-37)
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors (90-97)
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
