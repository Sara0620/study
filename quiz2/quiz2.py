#coding=utf-8
songlist=[]
def song_load(filename):
    with open(filename,"r") as fo:
        for line in fo:
            try:
                songinfo = line.strip().split(",")
                song={}
                song["name"] = songinfo[0]
                song["album"] = songinfo[1]
                song["musician_sex"] = songinfo[2]
                song["release_time"] = songinfo[3]
                song["playback"] = songinfo[4]
                songlist.append(song)
            except Exception as e:
                print e
def song_add(filename):
    song={}
    try:
        song["name"]=raw_input("请输入歌名：")
        song["album"]=raw_input("请输入专辑名：")
        song["musician_sex"]=raw_input("请输入音乐人性别：")
        song["release_time"]=int(raw_input("请输入发行时间："))
        song["playback"]=int(raw_input("请输入播放量："))
        songlist.append(song)
      
        with open(filename,"a") as fi:
            fi.write("%s,%s,%s,%s,%s\n" %(song["name"],song["album"],song["musician_sex"],song["release_time"],song["playback"]))
    except Exception as e:
        print e 

if __name__ == "__main__":
    song_load("song.txt")    
    for i in range(1):
        song_add("song.txt")
    for song in songlist:
        print song
