import os, time, cores as c
from pystyle import Colorate, Colors
banner1="""
__________                 _           
|_   __  |                (_)          
  | |_ \_|.---.   _ .--.  __   _   __  
  |  _|  / /__\\ [ `.-. | [  | [ \ [  ] 
 _| |_   | \__., | | | |  | |  > '  <  
|_____|   '.__.'[___||__][___][__]`\_]
      by: Phant0m The Great | v: 6.0
      
"""
banner2="""
⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶
⢻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡇
⠘⢿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⠿⠃
⢷⣮⣝⣿⣿⣿⣿⣿⣿⣆⠀⠐⠿⣿⣿⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣫⣵⡞⠀
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣰⣿⣿⣦⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
  ⠰⣾⣽⣿⣿⣿⣿⣿⣿⣇⢰⣿⣿⣿⣿⡆⣼⣿⣿⣿⣿⣿⣿⣭⣶⠃⠀⠀
  ⠀⠙⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠃⠀⠀⠀
  ⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀
  ⠀⠀⠀⠈⢛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀  ⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀  ⠀⠀⠀⠈⠻⡿⠟⣹⣿⣿⣿⣿⡝⠻⢿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠹⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

erro_01=f'{c.red}Não foi possível se conectar ao Alvo !\nPossíveis causas ↓\n• Não existe uma / no final da URL\n• A URL não foi escrita corretamente\n• O site está offline'
erro_000=f'{c.red}Ocorreu um erro de coneção inesperado!'

def carregando():
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banner2))
