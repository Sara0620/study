#coding=utf-8

song_list=[]
def song_load(filename):
    with open(filename,"r") as fo:
        for line in fo:
            try:
                song_info=line.strip().split()
                song={}
                song["name"]=song_info[0]
                song["album"]=song_info[1]
                song["musician_sex"]=song_info[2]
                song["release_time"]=song_info[3]
                song["playback"]=song_info[4]   
                song_list.append(song)
                return song_list
            except Exception as e:
                print e
            
def song_add(filename):
    song={}        
    try:
        song["name"]=raw_input("输入歌曲名：")
        song["album"]=raw_input("输入专辑名：")
        song["musician_sex"]=raw_input("输入艺术家性别：")
        song["release_time"]=int(raw_input("输入发行时间："))
        song["playback"]=int(raw_input("输入播放量："))
        song_list.append(song)
        with open(filename,"a") as fi:
            fi.write("%s,%s,%s,%s,%s\n" %(song["name"],song["album"],song["musician_sex"],song["release_time"],song["playback"]))
    except exception as e:
        print e            
def song_delete(filename):
    try:
        song_load("songs.txt")
        delete_name = raw_input("请输入要删除的歌名：")
        for name in song_list:
            song.pop["delete_name"]
            fi.write("%s,%s,%s,%s,%s\n" %(song["name"],song["album"],song["musician_sex"],song["release_time"],song["playback"]))
    except Exception as e:
        print e
if __name__ == "__main__":
        
    #song_load("songs.txt")
    #for i in range(2):
    #    song_add("songs.txt")
    #for song in song_list:
     #   print song
    order = raw_input("请输入操作需求：删除请输入d，查看请输入l，追加请输入a。")
        if order == "d":
            song_delete("songs.txt")
        elif order== "l":
            song_load("songs.txt")
        elif order== "a":
            song_add("songs.txt")
