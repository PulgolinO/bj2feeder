# -*- coding: utf-8 -*-
#!/usr/bin/python

#Importa as bibliotecas necessárias
import feedparser, urllib2, os, re

#-----------------------------------#
#------CONFIGURACOES DO USUARIO-----#
#-----------------------------------#

#Define o diretório que quer salvar os arquivos
os.chdir( '/home/nome_do_usuario' )
#Ex: os.chdir( '/home/fulano/downloads' )
#Tenha certeza que tem direito para escrever no diretório

#Define os releases que deverão ser baixados
#Não se esqueça de colocar o nome de cada release separado por vírgula e dentro de aspas duplas
RELEASES = "Release1|Release2|Release3"
#Ex: RELEASES = "Game.of.Thrones|Spiderman|Da.Vinci"

#Aqui é preciso definir os cookies necessários para acessar o site
PASS = "5Sua_Passkey_do_BJ2" #Coloque aqui sua pass do cookie. Não se esqueça de colocar entre aspas.
#Ex: PASS = "abcdefg123456789"
UID = "ua_UID_do_BJ2" #Coloque aqui seu UID do BJ2. Não se esqueça de colocar entre aspas.
#Ex: UID = "123456789"


#------------------------------------#
#----NAO EDITE NADA A PARTIR DAQUI---#
#------------------------------------#

#Verifica se algum release definido satisfaz algum download
if (PASS == "Sua_Passkey_do_BJ2" or UID == "Sua_UID_do_BJ2" or RELEASES == "Release1|Release2|Release3"):
        print( 'Modifique as informações antes de utilizar o script.' )
        print( 'Toda informação está aqui: https://github.com/pulgalipe/bj2feeder\nBye!' )
else:
        print('Procurando por torrents para baixar...\n')
        #Define a URL do Tracker que sera acessado pelo feedparser
        #Utilize o metodo "feedparser.parse" sempre que precisar acessar um feed
        bjurl = 'http://bj2.me/rss.php'
        bjurl = feedparser.parse( bjurl )

        for max_feeds in range( 20 ):
                #percorre os feeds e mostra apenas os que tem alguma palavra definida no
                title = bjurl.entries[ max_feeds ].title
                link = bjurl.entries[ max_feeds ].link
                link = link.replace( 'detalhes', 'download' )
                if re.search( RELEASES, title, re.I ):
                        print( 'Baixando Torrent: ' + title )
                        title = title.encode('ascii', 'replace')
                        print( 'Link: ' + link )
                        os.system( "wget -q --header \"Cookie: pass=" + PASS + ";uid=" + UID + "\" -O \"" + title + ".torrent\" " + link )
                        print( 'Download concluido.\n' )
        print( 'Script finalizado com sucesso!' )
