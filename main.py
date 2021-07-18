from pynput import keyboard
import google_stt as stt
import mimic_tts as tts
import play_audio as audio

def parseCommands(text):
    print("parsing command: ", text)

def playStop():
    audio.play("sounds/off.mp3")

def playStart():
    audio.play("sounds/on.mp3")

def listenUser():
    command = stt.listen(playStart, playStop)

    if not command:
        print("failed to listen command")

    parseCommands(command)

def main():
    print("Initiated. Press Ctrl+Alt+Q to start listening")
    with keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': listenUser }) as h:
        h.join()

main()
