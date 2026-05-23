from RealtimeTTS import TextToAudioStream, SystemEngine

engine = SystemEngine()
stream = TextToAudioStream(engine)

stream.feed("Hello. I sound surprisingly human.")
stream.play()
