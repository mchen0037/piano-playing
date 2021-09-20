from mido.sockets import connect
import mido
import time

message = mido.Message("note_on", note=60)
print(message)
output = connect("0.0.0.0", 8080)

# num = random.randint(0,num_files)

song = mido.MidiFile("test.mid")
piano = mido.Message("program_change", program=0)
output.send(piano)
print("huh")
for msg in song:
    time.sleep(msg.time)
    if msg.type == "program_change":
        print(msg)
    if not msg.is_meta and msg.type != "program_change":
        if msg.type in ["note_on", "note_off", "control_change"]:
            # print(msg)
            msg.channel = 0
        print(msg)
        output.send(msg)
