# vhs records the terminal, ffmpeg encodes. Both via homebrew:
#   brew install vhs ffmpeg
NAME ?= demo

video:
	vhs session.tape

gif: video
	ffmpeg -loglevel error -i $(NAME).mp4 \
	  -vf "fps=11,scale=940:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=48:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
	  -loop 0 -y $(NAME).gif

# Always look at the frames. Twice the code was fine and the picture was not.
frames: video
	for t in 2 8 16 24; do ffmpeg -loglevel error -ss $$t -i $(NAME).mp4 -frames:v 1 -y frame_$$t.png; done

clean:
	rm -f *.mp4 *.gif *.png
