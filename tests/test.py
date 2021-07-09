from colorful_print import color

color.black('Black')
color.red('Red')
color.green('Green')
color.yellow('Yellow')
color.blue('Blue')
color.magenta('Magenta')
color.cyan('Cyan')
color.white('White')

print()
color.red('Red')
color.green('Green', bold = True)
color.yellow('Yellow', bold = True, italic = True)
color.blue('Blue', bold = True, italic = True, underline = True)
color.magenta('Magenta', bold = True, italic = True, underline = True, strike_out = True)
color.cyan('Cyan', bold = True, italic = True, underline = True, reverse = True)
color.white('White', bold = True, italic = True, underline = True, strike_out = True, reverse = True)
