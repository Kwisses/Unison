from pocketsphinx import DefaultConfig


def psconfig():
    # Create a decoder with certain model
    config = DefaultConfig()
    config.set_string('-logfn', settings.POCKETSPHINX_LOG)
    #config.set_string('-hmm',   settings.ACOUSTIC_MODEL)
    config.set_string('-hmm', os.path.join(get_model_path(), 'en-us'))
    config.set_string('-dict', os.path.join(get_model_path(), 'cmudict-en-us.dict'))
    #config.set_string('-lm',    settings.LANGUAGE_MODEL)
    config.set_string('-kws',   settings.KEYPHRASES)
    #config.set_string('-dict',  settings.POCKET_DICT)