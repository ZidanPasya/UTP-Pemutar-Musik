import MusicBox #import file MusicBox
import pygame #import module pygame
import NextMusic #import file NextMusic
import os #import module os
import MusicBox #import file MusicBox
from time import sleep #import module time
from ListMusic import Lagu, judul, Artist #import file ListMusic

def daftarJudul(): #fungsi daftar judul
    for i in range (len(judul)): #melooping list dan meng output
        if i > 0:
            print(i,'.', judul[i])

def Musik(pilih): #fungsi Musik
    pygame.mixer.init() #Meng inisialisasi pygame.mixer untuk memberikan beberapa perintah mengenai lagu
    try: #error handling 
        pygame.mixer.music.load(Lagu[pilih]) #me load lagu pada directory path
        pygame.mixer.music.play() #memulai lagu
    except: #error handling jika file lagu tidak ada pada direktori
        pygame.mixer.music.stop() #lagu sebelumnya akan di stop
        os.system('cls')
        MusicBox.MusicBox(judul[pilih], Artist[pilih])
        print("Lagu Tidak ada dalam direktori!")
        sleep(3)
        os.system('cls')
        counter = pilih + 1; #counter akan ditambah 1
        NextMusic.Music(counter) #memanggil fungsi Music pada NextMusic       