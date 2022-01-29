wordle-solvre
=============

![](https://byob.yarr.is/jamesalbert/wordle-solvre/wordle)
![](https://byob.yarr.is/jamesalbert/wordle-solvre/sweardle)

^This badge will be generated from each hourly run of the workflow.

This project was originally designed to be a wordle solver using interactive prompts. After the implementing the source that would narrow down possible words given incorrect, correct, and misplaced letters, I wanted to use webdriver (deprecated, but it's what I'm used to) to automated the actual solving of the puzzle in the browser. I ran into some issues because the site uses shadow elements which (I'm not too familiar) seem to hide elements within the dom. Poking around, I ran `Object.getOwnPropertyNames` against the root game-app element. The list of properties it returned included a `solution` string. This property exposes the answer without any tries at all.

In short, the helper script is `src/main.py`, and the cheatin' cheater script is `cheat.py`. Simply run them without arguments.

I'm not sure if this bug is already known, but hopefully gets patched here soon. 