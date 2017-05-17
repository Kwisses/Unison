"""InputTest tests your computer's audio input through stt.

If the test fails, there may be a problem with the user's computer
microphone. Ensure that the microphone is working and is receiving input.
If the test continues to fail, check your internet connection as the
project's SpeechToText class object uses a connection to the Google database
to verify and convert the audio message. 

If the above instructions do not solve the input issue, please notify the
project's author(s) and contributors of the issue. For more information, check 
out the project's GitHub repository at https://github.com/Kwistech/Unison
"""

# Used to print audio message to the console
from classes.settings import Settings
from speech_to_text import SpeechToText


class InputTest:

    def __init__(self):
        """Initialize SpeechToText object and instance variables."""
        # Set settings
        self.settings_obj = Settings(cd="..")
        self.settings = self.settings_obj.set()

        # Set instance variables
        self.stt = SpeechToText(self.settings)
        self.count = 1
        self.timer = 3

    def display_attempt(self):
        """Print test instructions to the console."""
        print("Input Test - Attempt {}/{}\n".format(self.count, self.timer))
        print("Please speak into your computer's microphone")
        print("~ Ex. Hello world!\n")
        print("Listening...")

    @staticmethod
    def display_end():
        """Additional console end-of-test messages."""
        print("\n---\n")
        print("If your message was printed to the console, the test\n"
              "was successful! If it was not, please run the test again.\n"
              "If the problem persists, there may be a problem with the\n"
              "audio input.\n")
        print("End of Input Test")

    def run(self):
        """Run InputTest."""
        while True:
            # Display attempt and listen for input
            self.display_attempt()
            msg = self.stt.listen()

            # Verify msg
            if msg:
                print("\nSPOKEN: '{}'".format(msg))
                break
            else:
                print("\nSPOKEN: 'Error: No Input Received'")

                # Handle test attempts
                if self.count >= self.timer:
                    break
                else:
                    print("\n---\n")
                    self.count += 1
                    continue

        self.display_end()

if __name__ == "__main__":
    input_test = InputTest()
    input_test.run()
