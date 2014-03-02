#!/usr/bin/env python

import os
import sys
from mpd import MPDClient

# connect to mpd
mpc = MPDClient()
mpc.connect('localhost', 6600)

# get song info
song_info = mpc.currentsong()
song_file = song_info['file']

# get cover
image_extensions = (".jpg", ".jpeg", ".png")
music_library = '/mnt/berta/media/music'
song_path = os.path.join(music_library, song_file)
if os.path.exists(song_path):
	song_dir = os.path.dirname(song_path)
	for f in os.listdir(song_dir):
		if f.endswith(image_extensions):
			song_cover = f
			break

# set symlink
try:
	os.unlink('/tmp/mpd.cover')
except:
	pass
if 'song_cover' not in vars():
	os.symlink(os.path.join(os.environ['HOME'], '.conky/scripts/mpd-no-cover.jpg'), '/tmp/mpd.cover')
else:
	os.symlink(os.path.join(song_dir, song_cover), '/tmp/mpd.cover')
