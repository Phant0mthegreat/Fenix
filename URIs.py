import requests, banners, sys
import cores as c, os
from urllib.parse import urlparse
from pystyle import Colorate, Colors
'''
1=V 2=X
'''
try:
 def URI_Fenixpdr1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: Fenixpdr.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/Fenixpdr.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}100)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}100)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}100)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}100)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}100)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_Fenixpdr2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: Fenixpdr.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/Fenixpdr.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}100)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}100)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}100)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}100)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_apache1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: apache.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/apache.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}13232)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}13232)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}13232)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}13232)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}13232)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_apache2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com]\n[{c.bred}Incorreto{c.white}: https://www.google.com/]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: apache.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/apache.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}13232)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}13232)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}13232)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}13232)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_common1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: common.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/common.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}4613)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}4613)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}4613)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}4613)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}4613)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_common2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: common.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/common.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}4613)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}4613)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}4613)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}4613)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_big1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: big.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/big.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}- Encontrada ({qgel}{c.green}/{c.white}20469)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}20469)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}20469)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}20469)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}20469)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_big2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: big.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/big.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}20469)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}20469)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}20469)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}20469)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_SFU1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: sensitive_files_unix.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/sensitive_files_unix.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}16)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}16)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}16)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}16)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}16)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_SFU2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: sensitive_files_unix.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/sensitive_files_unix.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}16)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}16)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}16)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}16)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_jom1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: joomla.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/joomla.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}1544)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}1544)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}1544)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}1544)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}1544)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_jom2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: joomla.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/joomla.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}1544)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}1544)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}1544)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}1544)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_wp1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: wp_themes.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/wp_themes.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}21149)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}21149)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}21149)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}21149)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}21149)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_wp2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: wp_themes.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/wp_themes.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}21149)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}21149)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}21149)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}21149)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_rob1():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: robots.txt\n[ 👁️ ] Visualizar não encontrados: {c.green}✔{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/robots.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}990)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}990)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}990)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}990)\n')
     else:
      qgel=qgel+1
      print(f'[ {c.red}÷{c.white} ] Página {palavra} não foi encontrada... ({qgel}{c.red}/{c.white}990)\n')
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
 def URI_rob2():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com/]\n[{c.bred}Incorreto{c.white}: https://www.google.com]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ 💉 ] Alvo: {url}\n[ 🗂️ ] Wordlist: robots.txt\n[ 👁️ ] Visualizar não encontrados: {c.red}✖{c.white}\n')
  qgel=0
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(url, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(banners.erro_01)
    sys.exit()
  elif url[-1]!='/':
    print(banners.erro_01)
    sys.exit()
  with open("wordlist/robots.txt", "r") as arquivo:
   wordlist=arquivo.readlines()
   wordlist=[palavra.strip() for palavra in wordlist]
   for palavra in wordlist:
    uri=urlparse(url+palavra)
    response=requests.get(uri.geturl())
    try:
     if response.status_code==200:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.green}!{c.white} ] {uri.geturl()} [Status:{c.green}200{c.white}] - Encontrada ({qgel}{c.green}/{c.white}990)\n')
     elif response.status_code==301:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.blue}!{c.white} ] {uri.geturl()} [Status:{c.blue}301{c.white}] - Encontrada ({qgel}{c.blue}/{c.white}990)\n')
     elif response.status_code==302:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.cyan}!{c.white} ] {uri.geturl()} [Status:{c.cyan}302{c.white}] - Encontrada ({qgel}{c.cyan}/{c.white}990)\n')
     elif response.status_code==403:
      qgel=qgel+1
      qnut=qnut+1
      print(f'[ {c.yellow}!{c.white} ] {uri.geturl()} [Status:{c.yellow}403{c.white}] - Encontrada ({qgel}{c.yellow}/{c.white}990)\n')
     else:
      qgel=qgel+1
    except:
      print(banners.erro_000)
      sys.exit()
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
except KeyboardInterrupt:
  print(f'\n[#] O programa foi interrompido.')
