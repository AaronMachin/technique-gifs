Build me a short silent looping GIF that teaches one technique for using Claude Code,
reconstructed from my real session transcripts.

Audience: a software engineer here who has never used Claude Code and assumes it is a
thing that writes code for you. Mildly sceptical. Will watch it self-serve in a
Confluence page or a Slack post, half-attending, with no sound.

## Start from the renderer that exists

    git clone https://github.com/AaronMachin/technique-gifs
    brew install vhs ffmpeg

`render.py` already holds the drawing primitives: the prompt line, tool bullets,
streamed text, the annotation bar, the spinner. Copy `demo.py` and change the beats,
point `session.tape` at your copy, then `make gif`. Do not rewrite the styling.

## Find the technique first

My transcripts are one .jsonl per session, one folder per working directory, under
~/.claude/projects (or $CLAUDE_CONFIG_DIR if set). Read them from disk. Extract my
turns and your text replies, skip tool output. Do not ask me to resume anything.

Do not work from a written-up guide if one exists. A guide is the procedure with the
evidence taken out, and the evidence is the whole point. Go to the transcripts and
work out what actually happened, including the bit where the first output was wrong.

The technique is the reusable mechanism underneath, not the ticket. Write it as one
sentence before you go any further, and make that sentence say what it saves me or
stops going wrong. If you cannot write it, you have not found it yet.

## Write the script, show me, wait

One technique per GIF. Structure it as beats with a stated duration each, and for each
beat give me the literal text that will be on screen. Include:

- the prompt I actually sent, or a tightened version of it
- a real sample of what came back, enough to show the mechanism working
- the moment it was wrong, or the moment I corrected it, if there was one
- annotations that say what just happened
- a closing frame that is the literal line someone can paste into their own prompt

End the script with a short list of the judgement calls you made that I might overrule.

Show me the script and stop. Do not build anything yet.

## Then get an independent review

Once I have signed off, send the script to a subagent that has not seen our
conversation. Tell it to be adversarial and specific, and ask it these:

1. What does a viewer take away, in one sentence? If that sentence is not the
   technique, the script has failed.
2. Which terms, filenames or references would a newcomer be unable to parse? Which
   need explaining, which need replacing, which are fine as texture?
3. Beat by beat: is there enough time to read what is on screen, assuming the viewer
   is not concentrating? Name what is over-stuffed.
4. Anything that reads as marketing, as corporate training, or as something that would
   embarrass me if a manager watched it.
5. Does the last frame give the viewer something to do?

Bring back what it says, tell me which findings you disagree with and why, and confirm
with me only if something is major.

## Then build it

Reconstruct the session, do not capture one. Running the real Claude CLI inside the
recorder takes real minutes, gives you whatever it says that day, and puts live repo
content in every frame for you to vet. Say in your handover that it is staged and
which details you invented.

Output a .gif and an .mp4. Keep the .gif under about 1MB and the whole thing under
about 70 seconds.

## Traps, all of which cost me time

- Only one idea per GIF, and cut anything more novel than the technique itself. My
  first cut opened on a roster of eight specialist review agents, and a reviewer said
  the takeaway was "it can fire off eight agents", not the technique. Whatever is
  loudest on screen is what people leave with.
- Every beat is too fast on the first pass. Roughly double what feels right. A GIF has
  no scrubber, so anything unreadable is only recoverable by waiting for the whole loop.
- Never write an annotation that tells the viewer something is significant. I cut
  '"todo.md please" is a real answer' for being both AI-sounding and useless. Say what
  happened. If it is not obviously significant once said plainly, the beat is wrong,
  not the caption.
- The payoff has to be the working benefit, in plain words. I had "twenty-two findings
  became three", which sounds good and is not the point. The point was that answering
  the whole list in one message stops things drifting or getting quietly dropped.
  Compressed numbers are a substitute for saying what actually improves.
- After any recut, re-check that every number on screen still follows from what is
  shown. "Five of the eight agents found these independently" survived a cut that had
  already removed the eight agents, so it referred to nothing.
- Anything shorthand on screen must be set up before it is used. "todo.md please" only
  reads as a decision because the prompt shown earlier said what todo.md is for.
- Colour exactly one thing: whatever carries the idea. Everything else stays neutral.
- Do not draw the input box progressively. It renders broken mid-typing. Use the
  scrollback form, "> " and the text.
- Size the terminal to the tallest beat and hand-pad the short ones with leading blank
  lines, or short beats sit stranded at the top of a mostly empty frame.
- Pad the end of the Python script past the end of the vhs recording window, or the
  shell prompt reappears on the final frame.
- Verify by extracting frames with ffmpeg and actually looking at them. Twice the code
  was fine and the picture was wrong.
- Real detail from the transcripts is what stops it looking like a demo. Strip URLs,
  file paths outside the repo, and any customer named in the source.

## Voice

Read my CLAUDE.md and write everything, including the on-screen text, the way I write.
UK English. Plain. No em-dashes. Nothing that sounds like it was written to be
motivating. Sentences of different lengths, not a run of matched pairs.
