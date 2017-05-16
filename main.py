# Unison - Python 3.5 - Johnathon Kwisses (Kwistech)
"""Main program method call for Unison.

Unison is a speech-to-text and text-to-speech program that allows users 
control over their computer via voice command.

The main program's call structure is as follows:
    main()          - Calls Brain().run()
    Brain()         - Handles most of the processing
    Settings()      - Get and sets all settings
    SpeechToText()  - Converts audio to text
    TextToSpeech()  - Converts text to audio
    Switch()        - Handles mod calls
    Login()         - User login (to be added)
    
After the initial setup, the program will make an audible 'beep.' This 'beep'
informs the user that the program is ready for audio input. The user can then
command the program as they want as long as they say the keyword first in their 
command.

For more information, check the project's GitHub repository documents at 
https://github.com/Kwistech/Unison
"""

# Import for adding to Python Path
from os import path
import sys

# Handles main program logic
from brain import Brain


def main():
    """Main program that creates and runs one Brain class instance."""
    # Add "Unison" to Python's path
    sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    # Initialize Brain class object.
    brain = Brain()
    brain.run()

if __name__ == "__main__":
    main()
