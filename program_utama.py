def menu(akses):
    print("MAIN MENU")

    if(akses == "admin"):
        print("------")
        print("=> LOGIN")
        print("=> TAMBAH-GAME")
        print("=> INFO-GAME")
        print("=> STOK-GAME")
        print("=> LISTING-GAME")
        print("=> FIND-GAME")
        print("=> TOP-UP")
        print("=> HELP")
        print("=> SAVE")
        print("=> EXIT\n")
        print("=> Tidak punya akun ?")
        print("=> SIGN UP")

    elif(akses == "user"):
        print("------")
        print("=> LOGIN")
        print("=> BUY-GAME")
        print("=> LISTING-GAME")
        print("=> FIND-GAME")
        print("=> INVENTORY")
        print("=> SEARCH-MY-GAME")
        print("=> FIND-AT-STORE")
        print("=> HISTORY")
        print("=> HELP")
        print("=> SAVE")
        print("=> EXIT")

    else:
        print("------")
        print("=> LOGIN")
        print("=> EXIT")

def pilihMenu(akses):
    menu(akses)
    return (input("Masukan pilihan: ").lower())

