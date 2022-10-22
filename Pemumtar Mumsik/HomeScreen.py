from PlayMusic import Musik, daftarJudul #import file PlayMusic
from ListMusic import judul, Artist, Lagu #import file ListMusic
from MusicBox import MusicBox #import File MusicBox
from NextMusic import NextMusic #Import file NextMusic
from random import randint #import module random untuk merandom bilangan bertipe integer dengan randint
import os #import module os

def HomeScreen(nama): #fungsi homescreen dengan paramaeter 'nama'
    try: #error handling
        print("Selamat Datang", nama)    
        daftarJudul() #memanggil fungsi daftarjudul pada file PlayMusic
        pilih = int(input("Pilih Musik: "))
        os.system('cls')

        if pilih > 0 and pilih < len(Lagu): #statement jika input lebih dari 0 dan juga kurang dari panjang list lagu
            Musik(pilih) #memanggil file Musik dengan 'pilih' sebagai paramater pada file PlayMusic
            MusicBox(judul[pilih], Artist[pilih]) #memanggil fungsi MusicBox dengan parameter list 'judul[pilih]' dan 'Artist[pili]' pada file MusicBox
            NextMusic(pilih) #memanggil fungsi NextMusic dengan paramater 'pilih' pada file NextMusic
        else: #statement jika inputan melebihi salah
            counter = randint(1, len(Lagu)) # merandom nilai counter yang akan dimasukkan ke fungsi dibawahnya
            Musik(counter)
            os.system('cls')
            MusicBox(judul[counter], Artist[counter])
            NextMusic(counter)
    except: #error handling jika input tidak sesuai
        os.system('cls')
        SecondScreen() #memanggil fungsi SecondScreen

def SecondScreen(): #fungsi SecondScreen
    try:#error handling
        print("Silahkan Pilih Ulang Lagu!")    
        daftarJudul()
        pilih = int(input("Pilih Musik: "))
        os.system('cls')

        if pilih > 0 and pilih < len(Lagu): #statement jika input lebih dari 0 dan juga kurang dari panjang list lagu
            Musik(pilih)
            MusicBox(judul[pilih], Artist[pilih])
            NextMusic(pilih)
        else: #statement jika input tidak sesuai
            counter = randint(1, len(Lagu)) # merandom nilai counter yang akan dimasukkan ke fungsi dibawahnya
            Musik(counter)
            os.system('cls')
            MusicBox(judul[counter], Artist[counter])
            NextMusic(counter)
    except: #error handling jika input salah
        os.system('cls')
        SecondScreen()