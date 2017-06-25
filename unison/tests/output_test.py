"""OutputTest tests your computer's audio output through tts.

If the test fails, there may be a problem with the user's computer
speakers/headphones. Please make sure that the volume on your speakers 
and/or headphones is turned both on and up. If the test continues to fail,
go into your computers' audio settings and ensure that the right output
is selected as the default output to use. 

If the above instructions do not solve the output issue, please notify the
project's author(s) and contributors of the issue. For more information, check 
out the project's GitHub repository at https://github.com/Kwistech/Unison
"""

from unison.apis.text_to_speech import TextToSpeech

# Used to 'speak' message from console input
from unison.classes.settings import Settings


class OutputTest:

    def __init__(self):
        """Initialize TextToSpeech object."""
        # Set settings
        self.settings_obj = Settings(cd="..")
        self.settings = self.settings_obj.set()

        # Set instance variables
        self.tts = TextToSpeech(self.settings)

    @staticmethod
    def display_attempt():
        """Print test instructions to the console."""
        print("Output Test\n")
        print("Please type something into the console.")
        print("~ Ex. Hello world!\n")

    @staticmethod
    def display_end():
        """Additional console end-of-test messages"""
        print("\n---\n")
        print("If you heard your message through your speakers, the test\n"
              "was successful! If you did not, please run the test again.\n"
              "If the problem persists, there may be a problem with the\n"
              "audio output.\n")
        print("End of Output Test")

    def run(self):
        """Run OutputTest."""
        while True:
            # Display attempt and wait for user keyboard input
            self.display_attempt()
            msg = input("> ")

            # Verify msg
            if msg:
                msg = msg.lower()
                self.tts.speak(msg)
                break
            else:
                print("Error: Please type something into the console.")
                print("\n---\n")
                continue

        self.display_end()

if __name__ == "__main__":
    output_test = OutputTest()
    output_test.run()
