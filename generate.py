from my_modules.Metronome import metronome
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Create WAV files to use your TC Electronics Ditto+ Looper as a Metronome.')
    parser.add_argument('--bpm', default=120, type=int, help='Beats Per Minute that should be generated.')
    parser.add_argument('--bpmRange', default=False, type=str, help='Generate a range BPM\'s.  eg: 40-140')
    parser.add_argument('--rangeStep', default=1, type=int, help='Step to generate BPM files in.  eg: 10 will genearte 40, 50, 60, etc...')
    parser.add_argument('--beats', default=1, type=int, help='Number of beats that should be included in the output wav.  Anything greater than 140 BPM will be bumped up to at least 4 beats.')
    parser.add_argument('--beatEmph', default=4, type=int, help='Which beat to put the emphais on.  If the song is in 4/4 time, you will want to set this to 4.  Make sure to specify an emphasis WAV file if you plan to use this.')
    parser.add_argument('--beatWave', default='beat.wav', type=str, help='Full path to the WAV file containing the main beat to be used.')
    parser.add_argument('--emphWave', default=False, type=str, help='Full path to the WAV file containing the empahsis beat to be used.')
    parser.add_argument('--db', default=30, type=int, help='The volume of the input WAV files will be amplified by the number of decibles specified.  eg: It makes the output WAV files louder, bigger numbers = louder output.')
    parser.add_argument('--folder', default='./wav_files/', type=str, help='Full path to the folder the WAV file output should be written to.')
    args = parser.parse_args()
    #print(args.accumulate(args.integers))


    if not os.path.exists(args.folder):
        os.makedirs(args.folder)



    if args.bpmRange == False:
        # No range specified.  Generate 1 wav file at the specified BPM

        # Getting above about 140BPM with just 1 beat and the Ditto doesn't like it.  It's either too short or
        # Too small, either way, bumping it up to be sure it will play on the ditto.
        if args.bpm > 140 and args.beats < 4:
            args.beats = 4

        if args.emphWave == False: # Emphasis beat not specified
            metronome(
                beatwav=args.beatWave,
                beatcount=args.beats,
                bpm=args.bpm,
                outwav=(args.folder + str(args.bpm) + "_BPM-" + str(args.beats) + "_Beats.wav"),
                dbIncrease=args.db
            )
        else: # Emphasis beat specified.
            metronome(
                beatwav=args.beatWave,
                emphasiswav=args.emphWave,
                beatcount=args.beats,
                bpm=args.bpm,
                outwav=(args.folder + str(args.bpm) + "_BPM-" + str(args.beats) + "_Beats-Emphasis_" + str(args.beatEmph) + ".wav"),
                dbIncrease=args.db
            )
    else:
        # Range specified, generate the files for each BPM in the range.
        daRange = (args.bpmRange).split("-")
        daRange[0] = int(daRange[0])
        daRange[1] = int(daRange[1])

        if daRange[0] > daRange[1]:
            sys.exit("Bad BPM range specified.")

        for i in range(int(daRange[0]), int(daRange[1])+1, args.rangeStep):
            # Getting above about 140BPM with just 1 beat and the Ditto doesn't like it.  It's either too short or
            # Too small, either way, bumping it up to be sure it will play on the ditto.
            if i > 140 and args.beats < 4:
                args.beats = 4

            if args.emphWave == False: # Emphasis beat not specified
                metronome(
                    beatwav=args.beatWave,
                    beatcount=args.beats,
                    bpm=i,
                    outwav=(args.folder + str(i) + "_BPM-" + str(args.beats) + "_Beats.wav"),
                    dbIncrease=args.db
                )
            else: # Emphasis beat specified.
                metronome(
                    beatwav=args.beatWave,
                    emphasiswav=args.emphWave,
                    beatcount=args.beats,
                    bpm=i,
                    outwav=(args.folder + str(i) + "_BPM-" + str(args.beats) + "_Beats-Emphasis_" + str(args.beatEmph) + ".wav"),
                    dbIncrease=args.db
                )

if __name__ == "__main__":
    main()
