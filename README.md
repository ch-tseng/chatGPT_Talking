# ChatGPT_Talking (ChatGPT + Google T2S + Google S2T)

Steps:
1. Prepare a PC that can execute Python programs, or a Raspberry Pi.
2. Prepare a headset (or speaker plus microphone)
3. Enable Google Speech to Text and Text to Speech services on your Google Cloud.
4. Apply for your Google Cloud Credentials json file.
5. Apply for your Open API Key: https://platform.openai.com/account/api-keys
6. Install these Python packages:
    - pip install pygame
    - pip install pyaudio
    - pip install openai
    - pip install google-cloud-speech
    - pip install --upgrade google-cloud-texttospeech

7. Modify the parameters in config.ini file, then you can try to run these 3 files:
  - t2t.py: use text to talk
  - t2s.py: input text, reply with voice
  - s2s.py: chat with voice

