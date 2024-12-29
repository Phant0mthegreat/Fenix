import URIs, os, cores as c, banners, sys, time
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
console = Console()
try:
 banners.carregando()
 print(f"{'© Phant0m The Great' : ^30}")
 time.sleep(2)
 while True:
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  console.print(Panel.fit("""[01] [red]Escanear[white]  [02] [red]Informações[white]
  
[03] [red]Criador[white]   [00] [red]Sair[white]""", padding=(2,3), title="[bold yellow]FENIX"))
  ech=input(f'\nDigite sua escolha [{c.bred}>{c.white}] ')
  os.system('clear')
  if ech=='01' or ech=='1':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print('''[ 🗃️ ] Qual Wordlist você vai ultizar ?''')
    console.print(Panel.fit('''[1] apache.txt [red]([white]Contém [red]13232[white] combinações[red])[white]
[2] big.txt [red]([white]Contém[red] 20468[white] combinações[red])[white]
[3] common.txt [red]([white]Contém[red] 4613[white] combinações[red])[white]
[4] Fenixpdr.txt [red]([white]Contém[red] 100[white] combinações[red])[white]
[5] joomla.txt [red]([white]Contém[red] 1544[white] combinações [red])[white]
[6] robots.txt [red]([white]Contém[red] 990[white] combinações [red])[white]
[7] sensitive_files_unix.txt [red]([white]Contém[red] 16[white] combinações[red])[white]
[8] wp_themes.txt [red]([white]Contém[red] 21149[white] combinações[red])[white]'''))
    asc=input(f'\n[{c.bred}>{c.white}] ')
    if asc=='1':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_apache1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_apache2()
    elif asc=='2':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_big1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_big2()
    elif asc=='3':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_common1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_common2()
    elif asc=='4':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_Fenixpdr1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_Fenixpdr2()
    elif asc=='7':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_SFU1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_SFU2()
    elif asc=='5':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_jom1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_jom2()
    elif asc=='8':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_wp1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_wp2()
    elif asc=='6':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
      escoh=input(f'\n[{c.bred}>{c.white}] ')
      if escoh=='s' or escoh=='S':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_rob1()
      elif escoh=='n' or escoh=='N':
        os.system('clear')
        print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
        URIs.URI_rob2()
  elif ech=='02' or ech=='2':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print(f'\n[ {c.yellow}∆{c.white} ] O Fenix, é uma ferramenta de pentester, ele tem a capacidade de encontrar diretórios em sites, e páginas que podem haver alguma vulnerabilidade.\n\n[ {c.yellow}V{c.white} ] Versão: 6.5\n\n[ {c.yellow}×{c.white} ] Bugs: Caso tenha encontrado algum bug no Fenix, faça um Bug-Report entrando em contato com o criador.')
    print(f'\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
    input()
  elif ech=='03' or ech=='3':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print(f'\n[ © ] Criador: Phant0m The Great\n[ {c.bblue}D{c.white} ] {c.bblue}Discord{c.white}: phant0mthegreat.\n')
    print(f'\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
    input('')
  elif ech=='00' or ech=='0':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print('\nAté a próxima !')
    sys.exit()
except KeyboardInterrupt:
  print(f'\n[#] O programa foi interrompido.')
