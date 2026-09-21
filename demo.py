#!/usr/bin/env python3
"""A minimal example beat sheet. Replace with your own."""
from render import *
import re

NUM = lambda s: c("1;38;5;117", s)   # colour exactly one thing: the idea

def user(lines, speed=0.012):
    out()
    for i, ln in enumerate(lines):
        sys.stdout.write(ORANGE(" > ") if i == 0 else "   "); sys.stdout.flush()
        for ch in ln:
            sys.stdout.write(WHITE(ch)); sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n"); sys.stdout.flush()
    out()

def plain(s=""):
    out("   " + s if s else "")

clear()

# ---- beat 1: title --------------------------------------------------
top(9); pause(0.8)
plain(AMBER("The technique, in three or four words"))
pause(0.7); out()
plain(GREY("The job it does, in one line"))
pause(3.4)
clear()

# ---- beat 2: the prompt ---------------------------------------------
top(4)
user(["the prompt you actually sent, tightened but not invented"])
pause(1.4)
note("What this instruction is doing, and why it is the whole trick.")
pause(5.0)
clear()

# ---- beat 3: what came back -----------------------------------------
top(4)
spinner("Working", 1.4)
bullet("a real sample of the output", GREEN)
sub("enough to show the mechanism, not the whole reply")
pause(1.0)
plain(NUM("1 ") + GREY(" the part that carries the idea is the only thing coloured"))
pause(3.0)
note("Say what just happened. Do not assert that it matters.")
pause(5.0)
clear()

# ---- beat 4: the line to steal ---------------------------------------
top(7); pause(0.6)
plain(GREY("Add this to your own prompt:"))
out(); pause(0.8)
plain(AMBER("  the literal line someone can paste"))
pause(4.5)
clear(); pause(0.8)

# Pad past the end of the vhs recording window.
pause(6.0)
