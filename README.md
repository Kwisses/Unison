# Unison
Unison is a voice command and response program that gives a user the ability to control their computer via voice commands.

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
        else:
            self.feedback = False

In essence, the program provides the user audio and visual feedback as to what the program is doing. It then listens to the audio input and then selects the appropriate action/response to the message (msg) it heard.

## Motivation
Unison was developed as a response to the lack of voice command and response programs available to the visually impaired. This program aims to be an audio equivalent to the keyboard, mouse, and screen combination. In this way, we hope to develop software that improves the computer-using experience for the visually impaired.

## Installation
1. Fork or download this repository to your local drive.
2. From the projects root directory (Unison), run `main.py`.

This can be done in the command prompt with `python main.py` or it can be done in your IDE, or it can be done by double-clicking on `main.py`. If you need help with the installation, please contact one of the projects contributors.

*As of right now, the program can only be installed in the above way. We will implement additional ways to install (ex. Windows Installer) in future versions!*

## Dependencies and API Reference
The core program requires the following:
+ [gTTS](https://pypi.python.org/pypi/gTTS)
+ [pocketsphinx](https://pypi.python.org/pypi/pocketsphinx)
+ [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
+ [pygame](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)
+ [speech_recognition](https://pypi.python.org/pypi/SpeechRecognition/)

Additional dependencies might be required for the programs custom modules and apis!

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

If you would like to contribute to Unison, please contact one of the current contributors (list of current contributors can be found at the top of the repository). We are currently seeking contributors to add additional apis and modules to the program. 

## Licence

TBA
