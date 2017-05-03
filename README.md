# Unison
Unison is a speech-to-text and text-to-speech program that allows users control over their computer via voice command.
Unison aims to be a valuable tool for people with visual impairments.

## Installation

1. Fork this repository and clone it to your local drive.
2. From the projects root directory (Unison), run `main.py`.


This can be done in the command prompt with `python main.py` or it can also be done in your IDE.

## Dependencies
pyaudio,
pocketsphinx,
speech_recognition,
gTTS,
pygame,

## Usage

To use Unison, run the program (see Installation) and wait until you hear a sound. This sound notifies the user that the program is ready for audio input. Once the sound has been played, a user can command the program with the following phrasing:

+ "Keyword verb noun"
+ E.g. "Unison open default"

The keyword is the word that the program uses to verify the audio. The verb is the action which the user wants to do. The noun is the object that is going to be acted upon. 


Once a phrase has been received and verified, Unison will start to process what it has been commanded to do. 

* As of right now, Unison only has one module. More modules will come in the future!

## Contributing

Right now, we are not looking for contributors as Unsion is still in its very early stage. Once the project has been developed more, we will need people to create modules for it.

## Credits

Johnathon Kwisses (Kwistech)
