from colorama import Fore
from pyfiglet import figlet_format

name = "GirishCodeAlchemy"
formatted_text = figlet_format(name, font="standard", width=100)

# Print the name in a single line
print(Fore.GREEN + formatted_text)

# Reset colorama to avoid color bleeding in the terminal
print(Fore.RESET)