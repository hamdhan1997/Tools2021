# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

try:
	import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
        
def entertools():
	os.system('sh babi_buat_yang_ngerecode_thanks.sh')

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6285642215238&text=Assalamualaikum')

def menutools():
	os.system ('clear')
	print ' ┏━╮╭━┓            \033[1;37m[\033[1;33m+\033[1;37m] TOOLS HACK ALL IN ONE\n \033[1;31m┃┏┗┛┓┃        \033[1;35m* \033[1;37mAuthor \033[1;31m: \033[1;36mMuhamad Hamdan Sobirin\n \033[1;31m╰┓▋▋┏╯          \033[1;37mEmail  \033[1;31m: \033[1;32mHamdhanpay@gmail.com\n\033[1;31m╭━┻╮╲┗━━━━╮╭╮    \033[1;37mYoutube\033[1;31m: \033[1;32mHamdan Official\n\033[1;31m┃▎▎┃╲╲╲╲╲╲┣━╯  \033[1;35m* \033[1;33mTools Berisi 20 Tools Hacking.\n\033[1;31m╰━┳┻▅╯╲╲╲╲┃      \033[1;33mJauhi Larangan Yang Ada  \033[1;37m^_^\n \033[1;31m ╰━┳┓┏┳┓┏╯    \033[1;35m+ \033[1;33mHargai Author Karena Memakai\n    \033[1;31m┗┻┛┗┻┛    \033[1;33m   Tidak Sesulit Membuat \033[1;37m:-D'
	loding2()
	print ' \033[1;31╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;35m║ \033[1;37m NO\033[1;37m  \033[1;35m║║ \033[1;37m{\033[1;32mDAFTAR TOOLS HACK LENGKAP\033[1;37m} \033[1;35m║║\033[0mSTATUS\033[1;35m║\n\033[1;35m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m01\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mDARK FACEBOOK\033[1;37m}       \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m02\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mMULTI BRUTEFORCE FACEBOOK\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m03\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mHACK INSTAGRAM  \033[1;37m(\033[1;36mNO ROOT\033[1;37m)} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m04\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mHACK MAIL MULTIBRUTEFORCE\033[1;37m} \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m05\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mVIRTEX WHATSAPP\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m06\033[1;37m} \033[1;31m║║    \033[1;37m{\033[1;32mDAFTAR WEBSITE VULN\033[1;37m}    \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m07\033[1;37m} \033[1;31m║║         \033[1;37m{\033[1;32mSPAM  SMS\033[1;37m}         \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m08\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mCHAT  ADMIN\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m09\033[1;37m} \033[1;31m║║     \033[1;37m{\033[1;32mJOIN HAMDAN SOBIRIN\033[1;37m}     \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m}\033[1;31m ║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m10\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mHACK WIFI \033[1;37m(\033[1;36mROOT\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m11\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mHACK INSTAGRAM \033[1;37m(\033[1;36mROOT\033[1;37m)\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m12\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mHACK  PULSA\033[1;37m}        \033[1;31m║║\033[1;37m{\033[1;31mCOID\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m13\033[1;37m} \033[1;31m║║  \033[1;37m{\033[1;32mHACK DIAMOND  FREE FIRE\033[1;37m}  \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m14\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mHACK  UC PUBG\033[1;37m}       \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m15\033[1;37m} \033[1;31m║║       \033[1;37m{\033[1;32mHACK  CP CODM\033[1;37m}       \033[1;31m║║\033[1;37m{\033[1;33mMAIN\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m16\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mBUG HUNTERS\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m17\033[1;37m} \033[1;31m║║           \033[1;37m{\033[1;32mK-DORK\033[1;37m}          \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m18\033[1;37m} \033[1;31m║║        \033[1;37m{\033[1;32mSEND  VIRUS\033[1;37m}        \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m19\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;32mSHORTNER  LINKS\033[1;37m}      \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m20\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mNUYUL APLIKASI CAPING\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m21\033[1;37m} \033[1;31m║║  \033[1;37m{\033[1;32mNUYUL APLIKASI  FLASHGO\033[1;37m}  \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m22\033[1;37m} \033[1;31m║║     \033[1;37m{\033[1;32mHACK DIAMOND MLBB\033[1;37m}     \033[1;31m║║\033[1;37m{\033[1;31mCOID\033[1;37m}\033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m22\033[1;37m} \033[1;31m║║   \033[1;37m{\033[1;32mHACK FACEBOOK  TARGET\033[1;37m}   \033[1;31m║║ \033[1;37m{\033[1;32mON\033[1;37m} \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m00\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;34mKELUAR  PROGRAM\033[1;37m}      \033[1;31m║║ \033[1;31mEXIT \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝\n\033[1;31m╔══════╗╔═════════════════════════════╗╔══════╗\n\033[1;31m║ \033[1;37m{\033[1;32m++\033[1;37m} \033[1;31m║║      \033[1;37m{\033[1;34mSUBCRIBE PAJAOQ\033[1;37m}      \033[1;31m║║ \033[1;37mSUBS \033[1;31m║\n\033[1;31m╚══════╝╚═════════════════════════════╝╚══════╝'


def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Sudah punya ID dan Password nya? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN UNTUK MELANJUTKAN║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'Sobirin' and user == 'Hamdhan':
      print '║LOGIN SUKSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login GAGAL, Silahkan hubungi ADMIN'
      wa()
      ressture()
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        
def lodhirt():
    lodhirt = [
     'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN', '      ', 'SOBIRIN', '      ', 'HAMDAN\n']
    for o in lodhirt:
        print '\r\x1b[1;97m╔[\x1b[1;32m+\x1b[1;97m] \x1b[1;92mSUBSCRIBE CHANNEL \x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

os.system('clear')
logoname = '\033[1;91m____________\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\33[31;1m  ╔╗╔╔═╗╔╦╗╔═╗\n\33[33;1m ╔════════════╗\33[0;36m ║║║╠═╣║║║╠═╣\n\33[33;1m ╚════════════╝\33[37;1m ╝╚╝╩ ╩╩ ╩╩ ╩\n\33[0;36m  ║\033[1;36m██████████\033[1;31m╚╗\33[0;36m ╦╔═╔═╗╔╦╗╦ ╦\n\033[1;31m  ║\033[1;36m██\033[1;31m╔══╗\033[1;36m█\033[1;31m╔═╗\033[1;36m█\033[1;31m║\033[1;33m ╠╩╗╠═╣║║║║ ║\n\33[32;1m║\033[1;36m██\33[0;36m║\33[0;36m╬\33[0;36m╔╝\033[1;36m█\33[0;36m╚╗  ║\033[1;36m█\33[0;36m║\33[0;36m ╩ ╩╩ ╩╩ ╩╚═╝\n\33[0;36m  ║\033[1;36m██\33[0;36m╚═╝\033[1;36m█\33[0;36m║\033[1;36m█\33[0;36m╚╝\033[1;36m█\33[0;36m║\ \033[0m Subscribe\n\33[0;36m  ╚╗\033[1;36m█████████\33[0;36m═╝ \033[0mChannel\n\33[0;36m   ╚╗║╠╩╩╩╩╩╝   \033[0mHamdan Official\n\33[0;36m    ║║╚╗\033[1;33m┈\33[33;1m█\33[37;1m▐█████\033[1;31m▒\033[0m.｡oO\n\033[1;31m    ║\033[1;36m██\033[1;31m╠╦╦╦╗\n\033[1;31m    ╚╗\033[1;36m██████ \033[0mAuthor \033[1;31m: \033[1;32mHamdan Sobirin\n\033[1;31m     ╚════╝    \033[0mHACKER \033[1;31m: \033[1;32mCYBER TEAM TEGAL\n \033[1;33m<══════════════════════════════════>\n\033[1;31m'
print logoname
enternamek = raw_input("\033[1;31m[*] \033[1;32mMASUKAN NAMA KAMU: \033[1;36m")
os.system('clear')

print 32 * '\x1b[1;97m\xe2\x95\x90'
print '\33[32;1m █░░░█ █▀▀ █░░ ▄▀ ▄▀▄ █▄░▄█ █▀▀\n █░█░█ █▀▀ █░▄ █░ █░█ █░█░█ █▀▀\n ░▀░▀░ ▀▀▀ ▀▀▀ ░▀ ░▀░ ▀░░░▀ ▀▀▀'
print '                 \033[1;31m[*] \033[1;37mHi \033[1;36m' + enternamek
print 32 * '\x1b[1;97m\xe2\x95\x90'
lodhirt()
print '\033[1;37m║'
print '\033[1;37m╠\033[1;37m[\033[1;31m*\033[1;37m] \033[1;32mPILIH MENUNYA \033[1;37m[\033[1;31m*\033[1;37m]'
print '║\033[1;37m{\033[1;33m1\033[1;37m} \033[1;34mLogin Toolnya\033[1;37m'
print '║\033[1;37m{\033[1;33m2\033[1;37m} \033[1;34mHubungi Author \033[0m(\033[1;32mWhatsApp\033[1;37m)'
print '║\033[1;37m{\033[1;33m3\033[1;37m} \033[1;34mInstall Bahan\033[1;37m'
print '║\033[1;37m{\033[1;33m4\033[1;37m} \033[1;34mDownload User & Pass\033[1;37m'
print '║\033[1;37m{\033[1;31m0\033[1;37m} \033[1;31mExit.'
pilih = input("\033[1;37m╚═\x1b[1;91m▶\x1b[1;97m ")
if pilih == 1:
	tik()
	entertools()
elif pilih == 2:
	tik()
	wa()
	print '\n\033[1;37mTerimakasih Telah Menggunakan Tools Ini ^_^'
elif pilih == 3:
	tik()
	os.system ('bash babi_lu.sh')
elif pilih == 4:
	os.system('xdg-open https://raw.githubusercontent.com/hamdhan1997/locator1/master/PassHamdan.txt')
elif pilih == 0:
	os.system('clear')
	print '\033[1;37mTerimakasih Telah Menggunakan Tools Ini ^_^'
	os.system('exit')
	