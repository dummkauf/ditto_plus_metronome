from pydub import AudioSegment
from pydub.playback import play
import sys


def metronome(
        beatwav:str, # WAV file to be used for the beat. Full path if file isn't in same directory as script
        emphasiswav:str = "poop", # If an emphasis beat is needed, specify the wav file for that.
        outwav:str = "metronomeout.wav", # WAV file name to output
        bpm:int = 120, # Beats per minute
        beatcount:int = 1, # How many beats
        beatemphasis:int = 4, # Which beat to put emphasis on.  Default to 4
        dbIncrease:int = 0, # Number of DB's to increase volume by.
        playwav = False
    ):
    delay = (60/bpm)*1000 # Need delay in milliseconds

    # Lets avoid an infinite loop that will consume all our memory.
    if emphasiswav == outwav or beatwav == outwav:
        sys.exit("Output file set to one of the input files which will cause all kinds of silly problems.  Existing script.")

    # Read the beat wav file and figure out its lenght in ms
    daBeat = AudioSegment.from_wav(beatwav)
    daBeat_ms = len(daBeat)
    daBeat = daBeat + dbIncrease
    if daBeat_ms > delay :
        sys.exit("Beat audio file duration is longer than the specified BPM duration.  Exiting script.")

    # If there's an emphasis file specified...
    if emphasiswav != 'poop':
        # read the file and figure out it's length in ms
        daEmphasis = AudioSegment.from_wav(emphasiswav)
        daEmphasis_ms = len(daEmphasis)
        daEmphasis = daEmphasis + dbIncrease
        if daEmphasis_ms > delay :
            sys.exit("Emphasis audio file duration is longer than the specified BPM duration.  Exiting script.")

    final_song =  AudioSegment.empty()
    daCount = 1
    for counter in range(beatcount):
        if daCount == 1 and emphasiswav != "poop":
            SilenceDuration = delay - daEmphasis_ms
            final_song += daEmphasis
        else:
            SilenceDuration = delay - daBeat_ms
            final_song += daBeat

        final_song += AudioSegment.silent(duration=SilenceDuration)

        daCount = daCount + 1
        if daCount > beatemphasis:
            daCount = 1

    final_song.export(outwav, format="wav")
    if playwav == True:
        play(final_song)
