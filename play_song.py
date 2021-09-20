import mido
import time
import random

num_files = 16723

# 60 = Middle C
# programs change the voice select
# https://en.wikipedia.org/wiki/General_MIDI#Piano
# 0 - Piano
# 1 - Piano(Bright)
# 2 - Synth
# 3 - Electric Piano?
# 6 - Harpsichord
# 7 - Clavi
# 11 - Vibraphone
# 33 - Acoustic Bass
# 48 - Strings (Timpani)

while (True):
    alesis = mido.get_output_names()[1]
    port = mido.open_output(alesis)
    num = random.randint(0,num_files)
    try:
        song = mido.MidiFile("data/%d.mid" % num)
        piano = mido.Message("program_change", program=0)
        port.send(piano)
        print(num)
        for msg in song:
            time.sleep(msg.time)
            if msg.type == "program_change":
                print(msg)
            if not msg.is_meta and msg.type != "program_change":
                if msg.type in ["note_on", "note_off", "control_change"]:
                    # print(msg)
                    msg.channel = 0
                # print(msg)
                port.send(msg)
    except:
        print("file not found!")
