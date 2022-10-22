import HomeScreen #import file HomeScreen
import PlayMusic #import file PlayMusic
import os #import file os
import time #import file time
import pygame #import module pygame
import Stop #import file Stop
from ListMusic import judul, Artist, Lagu #import list judul dan artis pada file listMusic
from MusicBox import MusicBox, BoxPause #import fungsi MusicBox dan BoxPause pada file listMusic

def NextMusic(counter): #fungsi NextMusic dengan paramaeter counter
    while(True):
        pilihan = str(input("Masukkan Pilihan: "))
        if pilihan == '▶': #statement untuk lagu berikutnya
            counter += 1 # counter akan di tambah 1, misal counter = 10, maka 10 + 1 = 1 -> counter == 11
            if counter >= len(Lagu): #statement jika melebihi panjang list, counter == 1
                counter = 1
                PlayMusic.Musik(counter)
                os.system('cls')
                MusicBox(judul[counter], Artist[counter])
            else: #statement jika belum melebihi list
                PlayMusic.Musik(counter)
                os.system('cls')
                MusicBox(judul[counter], Artist[counter])
        elif pilihan == '◀': #statement untuk lagu sebelumnya
            counter-=1 #counter di kurang 1
            if counter <= 0: #jika kurang dari 0, maka counter akan menjadi panjang list dikurang 1
                counter = len(Lagu)-1 #misal counter = 0, misal len(lagu) == 14, maka 14-1 -> counter == 13 bisa disebut juga indeks ke-13 dari list
                PlayMusic.Musik(counter)
                os.system('cls')
                MusicBox(judul[counter], Artist[counter])
            else:#statement jika belum kurang list
                PlayMusic.Musik(counter)
                os.system('cls')
                MusicBox(judul[counter], Artist[counter])
        elif pilihan == '❚❚': #statement untuk pause lagu
            counter = counter #nilai counter akan tetap
            pygame.mixer.music.pause()
            os.system('cls')
            BoxPause(judul[counter], Artist[counter]) #memanggil fungsi BoxPause
        elif pilihan == '▷': #statement untuk unpause lagu
            counter = counter #counter tetap sama
            pygame.mixer.music.unpause()
            os.system('cls')
            MusicBox(judul[counter], Artist[counter])
        elif pilihan == '↺': #statement untuk me reload atau mengulang lagu
            counter = counter
            try: #error handling
                pygame.mixer.music.load(Lagu[counter]) #untuk me load lagu
                pygame.mixer.music.play() #untuk memulai lagu
                os.system('cls')
                MusicBox(judul[counter], Artist[counter])
            except: #error handling jika file lagu tidak ada pada Path
                pygame.mixer.music.stop()
                os.system('cls')
                MusicBox.MusicBox(judul[counter], Artist[counter])
                print("Lagu Tidak ada dalam direktori!")
                time.sleep(3)
                os.system('cls')
                counter = counter + 1; #counter ditambah 1
                NextMusic.Music(counter)
        elif pilihan == '◼': #statement untuk stop lagu
            os.system('cls')
            pygame.mixer.music.stop() #untuk stop lagu
            Stop.Stop() #memanggil fungsi stop
        elif pilihan == '↩': #statement untuk kembali ke menu HomeScreen 
            os.system('cls') 
            HomeScreen.SecondScreen()
        else: #statement jika perintah tidak sesuai
            counter = counter
            os.system('cls')
            MusicBox(judul[counter], Artist[counter])

def Music(count): #fungsi Music
    if count >= len(Lagu): #statement jika lebih dari list lagu dan kurang dari 0
        count = 1 #counter akan jadi 1
        pygame.mixer.music.stop() #untuk stop lagu
        os.system('cls')
        BoxPause(judul[count], Artist[count])
        NextMusic(count)
    else: #statement jika diantara panjang list lagu dan 0
        count = count
        pygame.mixer.stop() #untuk stop lagu
        os.system('cls')
        BoxPause(judul[count], Artist[count])
        NextMusic(count)
