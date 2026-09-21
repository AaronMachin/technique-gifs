# Technique GIFs

Short silent looping GIFs that teach one Claude Code technique each, built as
reconstructed terminal sessions rather than screen captures.

A capture takes real minutes of real time, gives you whatever the model said that
day, and puts live repo content in every frame for you to vet. A reconstruction
runs in seconds and you choose every line. The trade is honesty, so say in the
handover that it is staged and which details are invented.

## How it works

`render.py` holds the drawing primitives: the prompt line, tool bullets, streamed
text, the annotation bar, the spinner. A beat sheet (`demo.py`) imports those and
prints the session with controlled timing. `vhs` records a real terminal running
that script, `ffmpeg` encodes it.

```
brew install vhs ffmpeg
make gif          # writes demo.gif
make frames       # writes stills so you can check the picture, not the code
```

To make a new one, copy `demo.py`, change the beats, point `session.tape` at it.

## Writing one

`PROMPT.md` is the brief to hand a fresh agent. It covers mining the technique out
of `~/.claude/projects` transcripts, getting the script reviewed before anything is
built, and the traps.

The short version of the traps:

- One idea per GIF. Cut anything more novel than the technique itself, because
  whatever is loudest on screen is what people leave with.
- Every beat is too fast on the first pass. Roughly double what feels right.
- Colour exactly one thing: whatever carries the idea.
- Size the terminal to the tallest beat, pad the short ones with leading blanks.
- End the Python script after the `vhs` recording window closes, or the shell
  prompt turns up on the final frame.
- Last frame should be the line someone can paste, held long enough to read.

## Keeping it readable

There is no scrubber on a GIF, so anything unreadable on the first pass is only
recoverable by waiting out the loop. Around 70 seconds is the ceiling before that
wait gets annoying.
