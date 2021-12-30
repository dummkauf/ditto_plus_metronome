# ditto_plus_metronome
Generate WAV files that can be used on your TC Electronics Ditto+ as a metronome.

The Ditto+ looper pedal from TC Electronics allows you to play loops and background
tracks through your amp via the Pedal.  It can also be used as a metronome if you
load up WAV files on it with the correct beat and delay.  Most WAV files only require
a single beat and the correct amount of silence after and the pedal will loop the
WAV file to create a metronome effect.  This script will allow you to generate the WAV
files necessary for this with only 1 beat, as well as WAV files with multiple beats
and an emphais, which can be handy if you want a different beat on every 4th beat
for a song in 4/4 time.  It also allows you to provide your own WAV files if you want
a different beat other than the default ones included.

basic usage:

Generate a single WAV file using the provided beat.wav with just 1 beat:

`python3 generate.py --beats=1`

Generate a range of WAV files for every 10th BPM between 40 BPM and 200BPM with 4 beats and an emphasis on the 4th beat:

`python3 generate.py --bpmRange=40-200 --beats=4 --beatEmph=4 --emphWave=emphasis.wav --rangeStep=10`

Display help

```python3 generate.py --help
usage: generate.py [-h] [--bpm BPM] [--bpmRange BPMRANGE] [--rangeStep RANGESTEP] [--beats BEATS] [--beatEmph BEATEMPH] [--beatWave BEATWAVE] [--emphWave EMPHWAVE] [--db DB] [--folder FOLDER]

Create WAV files to use your TC Electronics Ditto+ Looper as a Metronome.

optional arguments:
  -h, --help            show this help message and exit
  --bpm BPM             Beats Per Minute that should be generated.
  --bpmRange BPMRANGE   Generate a range BPM's. eg: 40-140
  --rangeStep RANGESTEP
                        Step to generate BPM files in. eg: 10 will genearte 40, 50, 60, etc...
  --beats BEATS         Number of beats that should be included in the output wav. Anything greater than 140 BPM will be bumped up to at least 4 beats.
  --beatEmph BEATEMPH   Which beat to put the emphais on. If the song is in 4/4 time, you will want to set this to 4. Make sure to specify an emphasis WAV file if you plan to use this.
  --beatWave BEATWAVE   Full path to the WAV file containing the main beat to be used.
  --emphWave EMPHWAVE   Full path to the WAV file containing the empahsis beat to be used.
  --db DB               The volume of the input WAV files will be amplified by the number of decibles specified. eg: It makes the output WAV files louder, bigger numbers = louder output.
  --folder FOLDER       Full path to the folder the WAV file output should be written to.
```

One thing I noticed is that WAV files over about 140BPM with just 1 beat are not
detected by the Ditto+.  I'm not sure if it's due to too small of file or being too short
but anything over 140 BPM with less than 1 beat will be automatically be bumped up
to 4 beats, which works around this limitation of the Ditto+.
