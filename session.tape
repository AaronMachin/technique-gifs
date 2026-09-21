Output demo.mp4

Set Shell "bash"
Set FontFamily "Menlo"
Set FontSize 20
Set Width 1240
Set Height 860
Set Padding 34
Set Framerate 30
Set TypingSpeed 0ms
Set Theme { "background": "#1a1815", "foreground": "#e8e3db", "cursor": "#1a1815", "black": "#1a1815", "white": "#e8e3db", "brightWhite": "#ffffff" }

# Hidden so the command itself never appears on camera.
Hide
Type "clear && python3 demo.py"
Enter
Sleep 500ms
Show

# Must be SHORTER than the Python script's total runtime, or the shell
# prompt reappears on the final frame.
Sleep 26s
