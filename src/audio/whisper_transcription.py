import whisper

def initialize_whisper_model(model_name: str): 
    return whisper.load_model(model_name)