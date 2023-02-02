import google.cloud.texttospeech as tts
import pygame
import os

'''
Google T2S service
------------------------ Voices: 14 ------------------------
cmn-CN   | cmn-CN-Standard-A        | FEMALE   | 24,000 Hz
cmn-CN   | cmn-CN-Standard-B        | MALE     | 24,000 Hz
cmn-CN   | cmn-CN-Standard-C        | MALE     | 24,000 Hz
cmn-CN   | cmn-CN-Standard-D        | FEMALE   | 24,000 Hz
cmn-CN   | cmn-CN-Wavenet-A         | FEMALE   | 24,000 Hz
cmn-CN   | cmn-CN-Wavenet-B         | MALE     | 24,000 Hz
cmn-CN   | cmn-CN-Wavenet-C         | MALE     | 24,000 Hz
cmn-CN   | cmn-CN-Wavenet-D         | FEMALE   | 24,000 Hz
cmn-TW   | cmn-TW-Standard-A        | FEMALE   | 24,000 Hz
cmn-TW   | cmn-TW-Standard-B        | MALE     | 24,000 Hz
cmn-TW   | cmn-TW-Standard-C        | MALE     | 24,000 Hz
cmn-TW   | cmn-TW-Wavenet-A         | FEMALE   | 24,000 Hz
cmn-TW   | cmn-TW-Wavenet-B         | MALE     | 24,000 Hz
cmn-TW   | cmn-TW-Wavenet-C         | MALE     | 24,000 Hz
'''

class T2S:
    def __init__(self):
        print("Google T2S service")

    def text_to_wav(self, voice_name: str, text: str):
        language_code = "-".join(voice_name.split("-")[:2])
        text_input = tts.SynthesisInput(text=text)
        voice_params = tts.VoiceSelectionParams(
            language_code=language_code, name=voice_name
        )
        audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

        client = tts.TextToSpeechClient()
        response = client.synthesize_speech(
            input=text_input, voice=voice_params, audio_config=audio_config
        )

        filename = f"{language_code}.wav"
        with open(filename, "wb") as out:
            out.write(response.audio_content)
            #print(f'Generated speech saved to "{filename}"')

        return filename

    def unique_languages_from_voices(self, voices):
        language_set = set()
        for voice in voices:
            for language_code in voice.language_codes:
                language_set.add(language_code)
        return language_set

    def list_languages(self):
        client = tts.TextToSpeechClient()
        response = client.list_voices()
        languages = unique_languages_from_voices(response.voices)

        print(f" Languages: {len(languages)} ".center(60, "-"))
        for i, language in enumerate(sorted(languages)):
            print(f"{language:>10}", end="\n" if i % 5 == 4 else "")

    def list_voices(self, language_code=None):
        client = tts.TextToSpeechClient()
        response = client.list_voices(language_code=language_code)
        voices = sorted(response.voices, key=lambda voice: voice.name)

        print(f" Voices: {len(voices)} ".center(60, "-"))
        for voice in voices:
            languages = ", ".join(voice.language_codes)
            name = voice.name
            gender = tts.SsmlVoiceGender(voice.ssml_gender).name
            rate = voice.natural_sample_rate_hertz
            print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")

    def make_wav(self, audio_type, txt):
        filename = self.text_to_wav(audio_type, txt)

        return filename

    def play_wav(self, wavfile):
        pygame.mixer.init()
        my_sound = pygame.mixer.Sound(wavfile)
        my_sound.play()
        wait = True
        #print('--> wait speak start', wait)
        while wait:
            #print(pygame.mixer.get_busy())
            wait = pygame.mixer.get_busy()
        #print('<-- wait speak finish', wait)
            
        #pygame.time.wait(int(my_sound.get_length() * 1000))

    def speak(self, text, languane_code):
        file = self.make_wav(languane_code, text)
        self.play_wav(file)
        os.remove(file)
        