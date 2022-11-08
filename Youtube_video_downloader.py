# To download the given Youtube video link
# Package installed: pip install pytube

import pytube

link = input('Enter the Youtube video URL')
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()

print('Downloaded ', link)

# Input
# www.youtube.com/watch?v=UKA31XLzsNA&list=RDUKA31XLzsNA&start_radio=1


# Output
# The video with highest resolution will be downloaded in mp4 format