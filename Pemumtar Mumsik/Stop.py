import HomeScreen #import file HomeScreen
import os #import module os
import Menu #import file Menu

def Stop():
    try:
        menu = [ #list pilihan
            "1. Pilih lagu",
            "2. Exit"
        ]
        
        for i in range (2): #loop melooping list menu
            print(menu[i])
        
        pilih = int(input("Masukkan pilihan: ")) #memasukkan inputan

        if pilih == 1: #statement kembali ke HomeScreen
            os.system("cls")
            HomeScreen.SecondScreen()
        elif pilih == 2: #statement kembali ke menu Awal login/SignUp
            os.system("cls")
            Menu.Menu()
    except: #error handling jika input salah
        os.system('cls')
        Stop()
    
