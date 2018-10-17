#coding=utf-8

from  hashlib import md5

song_list={}
song_index = 0

def song_load(filename):
    global song_index
    with open(filename,"r") as fo:
        for line in fo:
            try:
                song_info=line.strip().split(',')
                song={}
                song["id"] = song_info[0]
                song["name"]=song_info[1]
                song["album"]=song_info[2]
                song["musician_sex"]=song_info[3]
                song["release_time"]=song_info[4]
                song["playback"]=song_info[5]   
                key = song_info[6]
                song_list[key] = song
                if song_index < int(song["id"]):
                    song_index = int(song["id"])
            except Exception as e:
                print e
 
            
def song_add(filename):
    global song_index
    song={}
    try:
        song["name"]=raw_input("输入歌曲名：")
        song["album"]=raw_input("输入专辑名：")
        song["musician_sex"]=raw_input("输入艺术家性别：")
        song["release_time"]=int(raw_input("输入发行时间："))
        song["playback"]=int(raw_input("输入播放量："))
        song_index += 1
        song["id"] = song_index
        key  = get_song_id("%s%s%s%s" %(song["name"], song["album"], song["musician_sex"], song["release_time"]))
        if key in song_list:
            print "已经存在"
            return
        song_list[key] = song
        with open(filename,"a") as fi:
            fi.write("%s,%s,%s,%s,%s,%s,%s\n" %(song["id"], song["name"],song["album"],song["musician_sex"],song["release_time"],song["playback"], key))
    except Exception as e:
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


def song_show():
    for sid in song_list:
        print sid, song_list[sid] 


def get_song_id(song_feature):
    return md5(song_feature).hexdigest()

if __name__ == "__main__":
        
    #song_load("songs.txt")
    #for i in range(2):
    #    song_add("songs.txt")
    #for song in song_list:
     #   print song
    song_load("songs.txt")
    while 1:
        order = raw_input("请输入操作需求：删除请输入d，查看请输入l，追加请输入a。")
        if order == "d":
            song_delete("songs.txt")
        elif order== "l":
            song_show()
        elif order== "a":
            song_add("songs.txt")
