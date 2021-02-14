# Spectral Crib Synth
### Category: Forensics
### Author: Brandon Arenas (Inga5508)

## Description
So my friend borrowed two of my favourite songs and combined them together to make a synth mix. Unfortunately, it kinda sucks and on top of that, he lost one of the original mp3 files! The **AUDACITY**!!! Can you recover my song please?

## Hints
1. Try looking at the audio files as spectrograms
2. Try to somehow “cancel out” the first part of the flag in synth_mix (suggest to look up inverting maybe)

## Solution

The wolf_raven mp3 file has part of the flag “magpie{5yn” at the 1 minute mark when viewing the audio as a spectrogram. The timecop_1983 file has the second part of the flag “tH_15_80’5k1n6}” at the 3 minute mark when viewing the audio as a spectrogram. The synth_mix file is a mix of both of these files where I purposely obfuscate the flag by moving the audio of wolf_raven which contains “magpie{5yn”, so that it aligns at the 3 minute mark with "tH_15_80'5k1n6}". This makes the flag look like an illegible garble of letters. The challenge consists of reversing this process. 

1. View the audio files as spectrograms.
2. Move the chunk of flag in raven_wolf to the 3 minute mark. Putting the wolf_raven flag to the 3 minute mark will align it with the garbled flag in synth_mix. 
3. After aligning them, raven_wolf needs to be inverted.
4. Finally, a new mix needs to be created by saving the mix as one audio file. 
5. The new mix will have raven_wolf subtracted from synth_mix which will contain the ungarbled timecop_1983 file, revealing the second part of the flag.

## Flag
magpie{5yntH_15_80’sk1n6}
