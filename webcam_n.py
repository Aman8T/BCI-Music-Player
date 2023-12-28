import simpleaudio as sa
  
# define an object to play
wave_object = sa.WaveObject.from_wave_file('the-rhythm-of-the-africa-wav-8837.wav')
print('playing sound using simpleaudio')
  
# define an object to control the play
play_object = wave_object.play()
play_object.wait_done()