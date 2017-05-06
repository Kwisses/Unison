"""Switch class defines how the program selects the correct module.

The class sets all of the main project data to its own variables. This is how 
the program can be used to include future modules without updating core code.

The classes execute_mods() method searches each mods verbs list to see if the 
passed verb is in it. If a match is found, the module is run. Even though this
is generic, there will be a problem as this program scales as there might be
an overlap of verb usage in future modules.
"""


class Switch:

    def __init__(self, settings, stt, tts, apis, mods):
        """Used to select the correct module to run.
        
        Args:
            settings (dict): All program settings.
            stt (speech_to_text.SpeechToText): Handles Speech-To-Text.
            tts (text_to_speech.TextToSpeech): Handles Text-To-Speech.
            apis (list): All API's.
            mods (list): All modules.
        """
        # Set all main project data
        self.settings = settings
        self.stt = stt
        self.tts = tts
        self.apis = apis
        self.mods = mods

    def execute_mods(self, verb, noun):
        """Match verb with appropriate module.
        
        Every module has a .verbs list. This method searches the mod.verbs 
        list for a match. If a match is found, the matching module is run.
        
        Args:
            verb (str): Action word to match with module.
            noun (str): Item to be acted upon.
        """
        for mod in self.mods:
            if verb in mod.verbs:
                # Sends all main project data as **kwargs
                mod.run(settings=self.settings,
                        stt=self.stt, tts=self.tts,
                        apis=self.apis,
                        verb=verb, noun=noun)

    def run(self, msg):
        """Run Switch class functionality.
        
        Args:
            msg (str): Text to be parsed and used for execute_mods().
        """
        for verb in self.settings["verbs"]:
            if verb in msg:
                noun = msg.split(verb + " ")[-1]
                self.execute_mods(verb, noun)
