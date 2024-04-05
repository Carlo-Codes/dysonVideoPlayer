import vlc
import keyboard
import os


keyPressed = False
loop = True

vlc_instance = vlc.Instance('--no-xlib')
player = vlc_instance.media_player_new()
username = 'carlo'
usbPath = '/media/'+ username +'/VIDEOS/'

current_video_path = ""
initial_video_path = usbPath + "1.mp4"

def check_stop():
    global loop
    if keyboard.is_pressed('z'):
        player.stop()
        vlc_instance.release()
        loop=False
    
def checkMediaAttached():
    global loop
    for d in os.listdir('/media/'+ username):
        if d == 'VIDEOS':
            loop = True
            return
    print('VIDEOS usb is not found,')
    loop = False
    return

def setVideoKey(player: vlc.MediaPlayer, key: str, videoPath: str):
    try: 
        global keyPressed
        global current_video_path
        if keyboard.is_pressed(key):
            if not keyPressed:
                if current_video_path != videoPath:
                    video = vlc_instance.media_new(videoPath)
                    player.set_media(video)
                    player.play()
                    player.set_fullscreen(True)
                    current_video_path = videoPath
                    keyPressed = True
        else:
            keyPressed = False
    except:
        print("error playing video")

def check_end(player: vlc.MediaPlayer):
    global current_video_path
    if player.get_state() == vlc.State.Ended:
        if current_video_path:
            video = vlc_instance.media_new(current_video_path)
            player.set_media(video)
            player.play()



current_video_path = initial_video_path
initial_video = vlc_instance.media_new(initial_video_path)
player.set_media(initial_video)
player.set_fullscreen(True)
player.play()


while loop:
    checkMediaAttached()
    check_stop()
    
    setVideoKey(player, 'w', usbPath + '2.mp4')
    setVideoKey(player, 'u', usbPath + '7.mp4')
    setVideoKey(player, '+', usbPath + '5.mp4')
    setVideoKey(player, 'y', usbPath + '6.mp4')
    setVideoKey(player, 'e', usbPath + '3.mp4')
    setVideoKey(player, 'r', usbPath + '4.mp4')
    setVideoKey(player, 'i', usbPath + '8.mp4')
    setVideoKey(player, 'o', initial_video_path)
    setVideoKey(player, 'p', initial_video_path)

    check_end(player)
