# mouse-mover

A small Python script that moves the mouse like a person would, so the machine stays awake and you show as active.

Each loop picks one of two moves:

- 80%: glide to a random point on the screen in 0.5 to 2 seconds, make 1 to 3 small corrections, scroll 30% of the time, then pause 1 to 5 seconds.
- 20%: drift into the top-left quarter of the screen, make 2 to 4 small moves there, then pause 1 to 3 seconds.

## Install

```sh
pip install -r requirements.txt
```

It uses [pyautogui](https://pypi.org/project/PyAutoGUI/) to move the mouse and [keyboard](https://pypi.org/project/keyboard/) to watch for the exit key.

## Run

```sh
python move-mouse.py
```

Press `Esc` to stop. The script stops after the current move finishes.

On Linux the `keyboard` package reads `/dev/input` directly and needs root, so run it with `sudo`. Its macOS support is experimental.

## License

MIT
