import vlc
import keyboard


keyPressed = False
loop = True
# Create the VLC instance and media player
vlc_instance = vlc.Instance('--no-xlib')
player = vlc_instance.media_player_new()

# Variable to store the path of the current video
current_video_path = ""
initial_video_path = "/data/1.mp4"

def check_stop():
    global loop
    if keyboard.is_pressed('z'):
        player.stop()
        loop = False
    

def setVideoKey(player: vlc.MediaPlayer, key: str, videoPath: str):
    try: 
        global keyPressed
        global current_video_path
        if keyboard.is_pressed(key):
            if not keyPressed:
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
            # If the video has ended, loop the current video
            video = vlc_instance.media_new(current_video_path)
            player.set_media(video)
            player.play()

  # Specify the path to the initial video



current_video_path = initial_video_path
initial_video = vlc_instance.media_new(initial_video_path)
player.set_media(initial_video)
player.set_fullscreen(True)
player.play()


while loop:
    check_stop()
    setVideoKey(player, 'w', '/data/2.mp4')
    setVideoKey(player, 'u', '/data/7.mp4')
    setVideoKey(player, 't', '/data/5.mp4')
    setVideoKey(player, 'y', '/data/6.mp4')
    setVideoKey(player, 'e', '/data/3.mp4')
    setVideoKey(player, 'r', '/data/4.mp4')
    setVideoKey(player, 'i', '/data/8.mp4')

    check_end(player)