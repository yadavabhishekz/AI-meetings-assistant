from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://youtu.be/Lg-meK5IU8Q"

chunks = process_input(source= source)

text = transcribe_all(chunks=chunks)

print(text)