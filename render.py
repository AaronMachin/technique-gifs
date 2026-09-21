#!/usr/bin/env python3
"""Reconstruction of a Claude Code session for a short explainer video.
Not a capture: every line here is scripted."""
import sys, time, textwrap

W = 96

def c(code, s): return f"\x1b[{code}m{s}\x1b[0m"
DIM   = lambda s: c("38;5;243", s)
GREY  = lambda s: c("38;5;250", s)
WHITE = lambda s: c("1;38;5;255", s)
ORANGE= lambda s: c("38;5;209", s)
GREEN = lambda s: c("38;5;114", s)
RED   = lambda s: c("38;5;203", s)
AMBER = lambda s: c("1;38;5;221", s)

def out(s=""):
    sys.stdout.write(s + "\n"); sys.stdout.flush()

def pause(t): time.sleep(t)

def clear():
    sys.stdout.write("\x1b[2J\x1b[H"); sys.stdout.flush()

def type_line(prefix, text, speed=0.016):
    sys.stdout.write(prefix); sys.stdout.flush()
    for ch in text:
        sys.stdout.write(WHITE(ch) if ch != " " else " "); sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n"); sys.stdout.flush()

def prompt_box(lines, speed=0.013):
    """A submitted user message, the way it sits in the scrollback."""
    out()
    for i, ln in enumerate(lines):
        sys.stdout.write(ORANGE(" > ") if i == 0 else "   ")
        sys.stdout.flush()
        for ch in ln:
            sys.stdout.write(WHITE(ch)); sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n"); sys.stdout.flush()
    out()

def bullet(text, colour=GREEN, mark="⏺"):
    out(colour(f" {mark} ") + GREY(text))

def sub(text, colour=DIM):
    out(DIM("   ⎿  ") + colour(text))

def stream(text, indent="   ", speed=0.006, colour=GREY):
    for ln in textwrap.wrap(text, W - 8):
        sys.stdout.write(indent); sys.stdout.flush()
        for ch in ln:
            sys.stdout.write(colour(ch)); sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n"); sys.stdout.flush()

def note(text):
    """Director's commentary. Deliberately not CLI-shaped."""
    out()
    for ln in textwrap.wrap(text, W - 6):
        out(AMBER("▌ ") + c("38;5;223", ln))
    out()

def spinner(label, secs=1.2):
    frames = "✳✢✻✽✢✳"
    end = time.time() + secs
    i = 0
    while time.time() < end:
        sys.stdout.write("\r" + ORANGE(f" {frames[i % len(frames)]} ") + DIM(label))
        sys.stdout.flush(); time.sleep(0.12); i += 1
    sys.stdout.write("\r" + " " * (len(label) + 6) + "\r"); sys.stdout.flush()

def top(n):
    """Vertical breathing room so short scenes are not stranded at the ceiling."""
    for _ in range(n):
        out()
