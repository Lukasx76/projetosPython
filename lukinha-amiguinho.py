from pytube import YouTube
from colorama import Fore


def on_complete(stream, file_path):
    print('Download Completed')
    print()


def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))


video_link = input('Write the video URL: ')
video_object = YouTube(
    video_link,
    on_complete_callback=on_complete,
    on_progress_callback=on_progress,
                       )

# information
print("------------------")
print(Fore.RED, f"Video title: {video_object.title}")
print(Fore.RED, f"Video title: {round(video_object.length / 60, 2)} minutes")
print("------------------")

download_choice = input("""
Resolution Choice:   
------------------
B: Best  
W: Worst 
A: Audio 

""")
match download_choice:
    case "B" | "b":
        video_object.streams.get_highest_resolution().download()

    case "W" | "w":
        video_object.streams.get_lowest_resolution().download()

    case "A" | "a":
        video_object.streams.get_audio_only().download()