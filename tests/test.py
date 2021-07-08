from colorful_print import color
from colorful_print.style import Style

color.black('Black')
color.red('Red')
color.green('Green')
color.yellow('Yellow')
color.blue('Blue')
color.magenta('Magenta')
color.cyan('Cyan')
color.white('White')

print(' Abc')
print(Style.BOLD, 'Abc', Style.END)
print(Style.ITALIC, 'Abc', Style.END)
