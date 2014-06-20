bj2feeder
=========

RSS downloader for BJ2 Torrent Tracker

####Requirements
```feedparser, wget```

####How to install the requirements
Copy & paste this code in your terminal:
```sh
$ sudo apt-get install wget python-pip python-dev build-essential 
$ sudo pip install --upgrade pip
$ sudo pip install feedparser
```

#####Usage of the script
Before run the script you need to change some variables on code, like:
#####os.chdir( '/home/username/some_folder' )
Which you define the folder where your torrents will be downloaded.

#####RELEASES = [ "Release1|Release2|Release3" ]
Where you define filters to downloads your torrents.<br/>
You can define hou much filters as you want, since you keep each one separated by pipe inside the quotes.<br/>
Use of Wildcars are allowed to make more complicated search strings.<br/>
Make use of ```.``` instead space to not break the search.<br/>
Make use of ```.*``` to search for an unindefined number os characters.<br/>
Make use of ```*``` to search for anything after your search string.<br/>
Ex: RELEASES = [ "Game.*Thrones|Spider.man.2|Splinter.Cell*" ]

#####PASS = "Sua_Passkey_do_BJ2"
Is your cookie variable.

#####UID = "Sua_UID_do_BJ2"
Another cookie variable from your BJ2 account.

And then you can just run the script using the command:
```sh
$ python bj2feeder.py
```

**Yay! It's so easy that I can't believe! \o/**

---

bj2feeder
=========

RSS Downloader para BJ2 Torrent Tracker

####Requirementos
```feedparser, wget```

####Como instalar os requerimentos
Copie e cole no seu terminal:
```sh
$ sudo apt-get install wget python-pip python-dev build-essential 
$ sudo pip install --upgrade pip
$ sudo pip install feedparser
```

####Usando o script
Antes de executar o script é preciso mudar algumas variáveis no código do script, como:
#####os.chdir( '/home/nome_usuario/algum_diretorio' )
Onde você define o diretório onde seus torrents serão baixados.

#####RELEASES = [ "Release1|Release2|Release3" ]
Onde você define os filtros para baixar seus torrents.<br/>
Pode definir quantos quiser separado cada um por vígula e colocando entre aspas.<br/>
Você pode usar Wildcards para fazer buscas mais complexas.<br/>
Utilize ```.``` em vez de espaço para não quebrar a busca.<br/>
Utilize ```.*``` para buscar por uma quantidade indefinida de caracteres.<br/>
Utilize ```*``` para buscar por qualquer coisa até o final da string.<br/>
Ex: RELEASES = [ "Game.*Thrones|Spider.man.2|Splinter.Cell*" ]

#####PASS = "Sua_Passkey_do_BJ2"
É a variável do cookie do site.

#####UID = "Sua_UID_do_BJ2"
Uoutra variável do cookie da sua conta do BJ2.

E agora você poderá executar o script utilizando o comando:
```sh
$ python bj2feeder.py
```

**Aha! É tão fácil que parece mentira! \o/**
