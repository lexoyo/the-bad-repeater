#!/usr/bin/env python3
#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import json
import sys
import time
import talkey

import speech_recognition as sr


def talk(phrase):
    sys.stderr.write(phrase + "\n")
    text_to_speech = talkey.Talkey()
    text_to_speech.say(phrase)

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        keywords = None
        keywordsWithProba = None
        lang = 'fr-FR'
        engine = 'sphinx'
        if(engine == 'sphinx'):
            sys.stderr.write("Use engine Sphinx\n")
            phrase = r.recognize_sphinx(audio, lang, keywordsWithProba);
        else:
            sys.stderr.write("Use engine Google speech API\n")
            phrase = r.recognize_google_cloud(audio, json.dumps({
              "type": "service_account",
              "project_id": "marcel-123",
              "private_key_id": "c8a4af088474e9e2ea93903726cdcb41087b43cb",
              "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC3CNfxAvHV0PoJ\n5BaCBM2Idqm3nM+qMQNTbvuYIkrOORVA81+sB2MGKMeWpRb8Dxyv9VgwjkaRciuV\nbM1QY5zPBUvi6F2LvKp6cxiImksGfL6c4ZzsqTIUfhYbhBnx1bEtx+sVwjVKxHDM\n9bfC/vaCswlFTix768vOC0hRgsRDa6uQTlBe5Azs8sgmUnN8tRWZ8K41FbYNghVX\nTqW9SSIqYqh38VrIjiojhGbUDfPsudwXg4IefTwO2/N4Q+ZY+NMPMGRBzPvzDHFe\ndmLibi3cMuJsh0NeEuKJW4bHXTXISR8Yg+W8gJD2hKaRQBvMk7kLCSbW76+YQfbU\nKUB8FxhTAgMBAAECggEAJU4uoSdN/hv1Un3EHqT29UjmR4+0/cW2nVNCAVx/7a9R\nxyazib8JrlAyeeBVInO8D5sMaf0dofhorLB72lYrOECmmm1s35XJE2MRDYqRHxXe\nzd/oGY5UsDuQqvQOS62XyrJ0Fj+6l+4Y5ZVxalOID9SI37DSvUEujWTcTQy/jtPy\nNGlp5c184zP2y+1jFr1JsaaWvMoFAL5IEWwEo3QgrJ5WLgADE2y8Gpdu5IPW9k9I\n+HWLroDFb0/32E/sSYlsu7shkUcnkRFejMK2iuux1uzXKSmp1a21Imj+OdkTKN3G\nwvMErXvR8ty/BIPuTuNThXXexTYCT6zebZGMQYGkfQKBgQD/d6CHyz/s0/JStzcH\n/Cio7Ru5e67bUiBN5t2khkXm6ILRmdA0XkSnzU3bUOkEkm8tObs/IS4tpQqF0VBB\nldwjwHGEsjmWCtlH81GEUPvDEkDx/YjbcfaguqcUYBaR57fcejqnvZMJF2GdWzOB\nZzcTzS9XEoqlV+caDu8mNYyXDQKBgQC3aozyjdiHdjvrQSoZp4rpZ2GQZXtTsEBF\nr74dciRWRo9guf/R+WhJudVZQJuMmc9tB2sijSUft82rPnKwL3foAUqyg78d9NS7\ndwV9dIgWi67qp7nwJusNx/TNHZvFqDkHziy7PaL6qwXUln/Y40P40Nm4jnVSDO5b\nNHGFuXyU3wKBgA0h8C2q5CFfj+ByrLCLZOeyMK+rTQTXRvPaP2CaynMhVsBBoPNg\nOTVLF4qDsUbb5D0174tCQGZ2SoEwjmigtI1d8jf5FX7CFgNd3b3oj9iqUo5eEy/8\nvsnqbnZcrixX9hquad9/nlRkUE9PhelMDgfFj35xZJE1YJr1U5PqQsztAoGADaBv\n6lFZhe7l0rubqh5FdsPEftrbR8Nvcv30jPF++53wZwpKlEoIUnno/OGM7Ow8eeg0\nMHP2Dx4zvIY+NRLBwM3fw9V/7HTVHTxhfwmaVrp3+10MtmfdzL9PU7HgcdXmrsrF\njf+tTRxJqZqo0u9HjIPPuSN0We02BDaoPHwkYlcCgYBK88Lp/WZMFNakV/ajugba\nnDedWJIxGUptRo1rNoGhnAGMFwBP8kEM5A/2mF8lpDfTF8zyUareO8rDJPR/maxE\n4PZ6EcpYfv4fy1AyNckHTCcc8IHeKUiz33ef7zG9FBlRig7weudNtKVvU9k+O/3v\noac3QISWlf3Izt93lMoSLQ==\n-----END PRIVATE KEY-----\n",
              "client_email": "marcel-account@marcel-123.iam.gserviceaccount.com",
              "client_id": "101489589357383356375",
              "auth_uri": "https://accounts.google.com/o/oauth2/auth",
              "token_uri": "https://accounts.google.com/o/oauth2/token",
              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
              "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/marcel-account%40marcel-123.iam.gserviceaccount.com"
            }), lang, keywords);

        sys.stdout.write(">>>>>>>>>>>>>>>>>> " + phrase + "\n")

        talk(phrase)

    except sr.UnknownValueError:
        sys.stderr.write("could not understand audio\n")
    except sr.RequestError as e:
        sys.stderr.write("Could not request results from service; {0}\n".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

talk("TALK NOW")

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
#for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
#stop_listening()  # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)

