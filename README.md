# Unison
Unison is a voice command and response program that gives a user the ability to control their computer via voice commands.

## Motivation
Unison was developed as a response to the lack of voice command and response programs available to the visually impaired. This program aims to be an audio equivalent to the keyboard, mouse, and screen combination. In this way, we hope to develop software that improves the computer user experience for the visually impaired.

## Requirements
Unison is designed to work on __Windows 10__ only. Unison requires a __microphone__ (for voice commands) and __speakers__ (for audio feedback and responses). In addition, Unison connects to various API's (Google Text To Speech, Google SpeechRecognition, etc.) and thus requires a __stable connection to the internet__. 

## Dependencies and API Reference
The core program requires the following:
+ [Python 3.5.0](https://www.python.org/downloads/release/python-350/)
+ [gTTS](https://pypi.python.org/pypi/gTTS)
+ [pocketsphinx](https://pypi.python.org/pypi/pocketsphinx)
+ [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
+ [pygame](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)
+ [speech_recognition](https://pypi.python.org/pypi/SpeechRecognition/)

Additional dependencies may be required for the programs custom modules and API's!

## Installation
1. Fork or download this repository to your local drive.
2. From the projects root directory (Unison), run `main.py`.

This can be done in the command prompt with `python main.py` or it can be done in your IDE, or it can be done by double-clicking on `main.py`. If you need help with the installation, please contact one of the projects contributors.

*As of right now, the program can only be installed in the above way. We will implement additional ways to install (ex. Windows Installer) in future versions!*

## Code Example
The core of the program depends on the following main program loop:

    while True:
        # Program feedback
        if self.feedback:
            self.gen_feedback(self.beep, self.beep_v)

        # Listen to audio from mic
        msg = self.stt.listen()

        # Verify and process audio msg
        if msg:
            self.process_msg(msg)
            self.feedback = True
        else:
            self.feedback = False

In essence, the program provides the user audio and visual feedback as to what the program is doing. It then listens to the audio input and then selects the appropriate action/response to the message it heard.

## How to use
To use Unison, run the program (see **Installation**) and wait until you hear a beep. If you do not hear a beep, proceed to the **Tests** section below to test your computers audio input. The beep notifies the user that the program is ready for audio input. Once heard, a user can command the program with their voice using the following phrasing:

    "keyword verb noun"

Examples: 

    "unison open default"
    "unison launch windows media player"

The `keyword` is the word that the program uses to verify the audio. The `verb` is the action which the user wants to do. The `noun` is the object that is going to be acted upon.

Upon keyword recognition, Unison will process what it has been commanded to do. To quit the program, simply say "unison terminate" and the program will terminate.

**In order to launch files and programs, a user must copy said files and programs into the "Unison Desktop" directory (created at runtime and can be found on the user's desktop). Note that to launch programs, a copy of the programs .exe file must be present in this folder. Also, it is a good idea to rename the files and programs in this directory to names that can be said easily.**

    Example:
        
        wmplayer.exe --> windows media player.exe

*Note: A complete list of verb/noun usage is available in the [project's Wiki (under List of Verbs and Nouns)](https://github.com/Kwistech/Unison/wiki/List-of-Verbs-and-Nouns).*

## Tests
To run all of the available program tests, run `all_tests.py` located in the projects 'tests' directory. To run one test at a time, simply open the test file you would like to run (Ex. `input_test.py`, `output_test.py`, `dependencies_test.py`), and run that file.

Example code in `all_tests.py`:

    class AllTests:
        def __init__(self):
            # Test objects
            input_test = InputTest()
            output_test = OutputTest()
            dep_test = Dependencies()
            
            # Tests iterator
            self.tests = [input_test, output_test, dep_test]

        def run(self):
            for test in self.tests:
                test.run()

    if __name__ == "__main__":
        all_tests = AllTests()
        all_tests.run()

Example output from `all_tests.py`:

    Input Test - Attempt 1/3

    Please speak into your computer's microphone
    ~ Ex. Hello world!

    Listening...

    SPOKEN: 'hello'  # will print what user says

## Contributors

If you would like to contribute to Unison, feel free to fork the repository, develop API's and modules, and submit pull requests. Instructions on how to develop API's and modules can be found in the project's Wiki. Please note and adhere to the repository's licence as it best reflects the aim of the project. We are currently seeking contributors to add additional API's and modules to the program. 

## Licence

Open Software License 3.0
