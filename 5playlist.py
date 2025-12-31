import random
playlist=[]
while True :
    print("\n--- PLAYLIST MENU ---")
    print("1. Add Song")
    print("2. Play Particular Song")
    print("3. Remove Song")
    print("4. Shuffle Playlist")
    print("5. Play Songs Sequentially")
    print("0. Exit")
    
    ch = input("enter choice : ")
    if ch=='1':
        song= input("enter song name ")
        playlist.append(song)
        print("song added.")
    
    elif ch=='2':
        song= input("enter song to play : ")
        if song in playlist :
            print("Now playing : ",song)
        else:
            print("song not found in playlist")
    elif ch=='3':
        song=input("enter song to remove :")
        if song in playlist :
            playlist.remove(song)
            print("song removed .")
        else:
            print("song not found")
    elif ch=='4':
        random.shuffle(playlist)
        print("playlist shuffled")
        print("Current Playlist:", playlist)
    elif ch=='5':
        if len(playlist)==0:
            print("empty playlist")
        else :
            print("playing songs sequentially :")
            for s in playlist :
                print (" now playing  : ",s)
    elif ch=='0':
        print("playlist closed")
        break

    else:
        print("invalid choice")