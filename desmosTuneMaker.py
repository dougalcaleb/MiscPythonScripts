# TO USE: set Desmos bounds to y-axis: 1 < y < 13 and x-axis: 0 < x < 10
# Note that "scale" and "speed" settings MUST be the same on Desmos or the speed will be off

# Settings
mode = "drone" # "sine" uses compressed sine waves to give a different sound
bpm = 113      # the acual BPM of the original song
scale = 10     # the width of the x-axis bounds in Desmos. Stick with 10.
speed = 0.25    # the playback speed of the Hear Graph menu in Desmos. At 0.5, you get 10sec of playback
noteMode = "short"  # Determines if notes have space between them. "short" or "smooth"
outputMode = "file" # Sets output mode. "console" or "file"




sineCompression = 500000000 # 500000000 or 1e9
sineFunc = f"sin({sineCompression}x) + "


notes = {
    "e": 1.01,
    "f": 2,
    "f#": 3,
    "g": 4,
    "g#": 5,
    "a": 6,
    "a#": 7,
    "b": 8,
    "c": 9,
    "c#": 10,
    "d": 11,
    "d#": 12,
    "e5": 13,

    "gb": 3,
    "ab": 5,
    "bb": 7,
    "db": 10,
    "eb": 12,

    "rest": 15,

    "whole": float('%.3f'%(60000 / bpm / 1000 / (100 / scale) * 20 * speed * 2)),
    "half": float('%.3f'%(60000 / bpm / 2 / 1000 / (100 / scale) * 20 * speed * 2)),
    "dothalf": float('%.3f'%(60000 / bpm / 2 / 1000 / (100 / scale) * 20 * speed * 2)) + float('%.3f'%(60000 / bpm / 4 / 1000 / (100 / scale) * 20 * speed * 2)),
    "quarter": float('%.3f'%(60000 / bpm / 4 / 1000 / (100 / scale) * 20 * speed * 2)),
    "8th": float('%.3f'%(60000 / bpm / 8 / 1000 / (100 / scale) * 20 * speed * 2)),
    "16th": float('%.3f'%(60000 / bpm / 16 / 1000 / (100 / scale) * 20 * speed * 2)),
    "32nd": float('%.3f'%(60000 / bpm / 32 / 1000 / (100 / scale) * 20 * speed * 2)),

    "notePause": float('%.3f'%(60000 / bpm / 64 / 1000 / scale * 10))
}

n = notes

# [ n["note"], n["note length"], number of times]

sandstorm = [
    [ n["b"], n["8th"], 5 ],
    [ n["rest"], n["8th"], 1 ],
    [ n["b"], n["8th"], 7 ],
    [ n["rest"], n["8th"], 1],
    [ n["e5"], n["8th"], 7 ],
    [ n["rest"], n["8th"], 1],
    [ n["d"], n["8th"], 7 ],
    [ n["rest"], n["8th"], 1 ],
    [ n["a"], n["8th"], 2],
    [ n["b"], n["8th"], 5 ],
    [ n["rest"], n["8th"], 1],
    [ n["b"], n["8th"], 7 ],
    [ n["rest"], n["8th"], 1],
    [ n["e5"], n["8th"], 2 ],
    [ n["b"], n["8th"], 5 ],
    [ n["rest"], n["8th"], 1],
    [ n["b"], n["8th"], 7 ],
]
 # bpm: 113
rickrolled = [
    [n["e"], n["8th"], 2],
    [n["f#"], n["8th"], 1],
    [n["e"], n["8th"], 1],
    [n["c#"], n["quarter"] * 1.5, 2],
    [n["b"], n["half"] * 1.5, 1],
    [n["e"], n["8th"], 4],
    [n["b"], n["quarter"] * 1.5, 2],
    [n["a"], n["8th"], 1],
    [n["g#"], n["8th"], 1],
    [n["f#"], n["half"], 1],
    [n["f#"], n["8th"], 2],
    [n["a"], n["8th"], 1],
    [n["f#"], n["8th"], 1],
    [n["a"], n["half"], 1],
    [n["b"], n["quarter"], 1],
    [n["g#"], n["quarter"], 1],
    [n["f#"], n["quarter"], 1],
    [n["e"], n["half"], 1],
    [n["e"], n["quarter"], 1],
    [n["b"], n["half"], 1],
    [n["a"], n["half"], 1],

    [n["rest"], n["half"], 1],

    [n["e"], n["8th"], 2],
    [n["f#"], n["8th"], 1],
    [n["e"], n["8th"], 1],
    [n["c#"], n["quarter"] * 1.5, 2],
    [n["b"], n["half"] * 1.5, 1],
    [n["e"], n["8th"], 4],
    [n["e5"], n["half"], 1],
    [n["f"], n["quarter"], 1],
    # [n["c"], n["8th"], 1],
    # [n["a#"], n["8th"], 1],
    # [n["a"], n["quarter"], 1],
]

crabRave = [
    [n["e"], n["8th"], 3],
    [n["g"], n["8th"], 1],
    [n["a"], n["8th"], 3],
    [n["g"], n["8th"], 1],
    [n["f#"], n["8th"], 3],
    [n["e"], n["8th"], 1],
    [n["d"], n["8th"], 3],
    [n["e"], n["8th"], 1],
    [n["g"], n["8th"], 3],
    [n["a"], n["8th"], 1],
    [n["g"], n["8th"], 3],
    [n["f#"], n["8th"], 1],
    [n["e"], n["8th"], 3],
    [n["d"], n["8th"], 1],
    [n["e"], n["8th"], 3],
    [n["g"], n["8th"], 1],
    [n["a"], n["8th"], 3],
    [n["g"], n["8th"], 1],
    [n["f#"], n["8th"], 3],
    [n["e"], n["8th"], 1],
    [n["d"], n["8th"], 3],
    [n["e"], n["8th"], 1],
]

# shootingStars = [
#     [n["d#"], n["quarter"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["quarter"], 1],
#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["quarter"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["a#"], n["8th"], 1],
#     [n["g#"], n["quarter"], 1],
#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["quarter"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["quarter"], 1],
# ]

# ariaMath = [
#     [n["d#"], n["quarter"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["quarter"], 1],

#     [n["d#"], n["8th"], 1],
#     [n["g#"], n["8th"], 1],
#     [n["d#"], n["quarter"], 1],
#     [n["g#"], n["8th"], 1],
# ]

def expand(tuneRaw):
    tuneExpanded = []
    for note in tuneRaw:
        for i in range(note[2]):
            tuneExpanded.append([note[0], note[1]])
    return tuneExpanded

def create(tune, noteJoining):
    tune = expand(tune)

    joiner = None

    if noteJoining == "stacatto" or noteJoining == "short":
        joiner = notes['notePause']
    elif noteJoining == "legato" or noteJoining == "smooth":
        joiner = 0

    tuneStr = "f(x)=\left\{"
    firstPart = True

    if mode == "drone":
        pos = 0
        for note in tune:
            if not firstPart:
                tuneStr += ", "
            firstPart = False
            tuneStr += f"{pos}<x<{pos + note[1] - joiner}: {note[0]}"
            pos += note[1]
            pos = float('%.3f'%(pos))

    elif mode == "sine":
        pos = 0
        for note in tune:
            if not firstPart:
                tuneStr += ", "
            firstPart = False
            tuneStr += f"{pos}<x<{pos + note[1] - joiner}: {sineFunc} + {note[0]}"
            pos += note[1]
            pos = float('%.3f'%(pos))

    tuneStr += "\\right\}"
    return tuneStr

result = create(rickrolled, noteMode)

if outputMode == "console":
    print(result)
else:
    try:
        file = open("tuneMakerOutput.txt", "w")
        file.write(result)
        file.close()
        print("Done")
    except:
        print("Encountered an error")
