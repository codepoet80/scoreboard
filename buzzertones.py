from gpiozero.tones import Tone
import threading
from time import sleep

class songs:
	#constructor
	def __init__(self, buzzerPin = 21):
		#speaker range is midi=57 through midi=81
		from gpiozero import TonalBuzzer

		self.buzzerPin = buzzerPin
		self.buzzer = TonalBuzzer(self.buzzerPin)

	#play a given song in the background (thread means background)		
	def play_song(self, songName):
		songTarget=self.play_ballgame
		if (songName == "ballgame"):
			songTarget = self.play_ballgame
		elif (songName == "abisong"):
			songTarget = self.play_abi_song
		elif (songName == "elisong"):
			songTarget = self.play_eli_song
		song_thread = threading.Thread(target=songTarget)
		song_thread.start()

	#take me out to the ball game
	def play_ballgame(self):
		self.buzzer.play(Tone(midi=60))
		sleep(0.7)
		self.buzzer.play(Tone(midi=72))
		sleep(0.3)
		self.buzzer.play(Tone(midi=70))
		sleep(0.2)
		self.buzzer.play(Tone(midi=67))
		sleep(0.2)
		self.buzzer.play(Tone(midi=64))
		sleep(0.2)
		self.buzzer.play(Tone(midi=67))
		sleep(0.7)
		self.buzzer.play(Tone(midi=62))
		sleep(0.3)
		self.buzzer.stop()
		sleep(1)
		self.buzzer.play(Tone(midi=60))
		sleep(0.5)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=60))
		sleep(0.2)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=60))
		sleep(0.2)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=64))
		sleep(0.7)
		self.buzzer.stop()
		
	#song by Abi W, Jan 26, 2020
	def play_abi_song(self):
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=71))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=70))
		sleep(0.5)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=71))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=70))
		sleep(0.2)
		self.buzzer.play(Tone(midi=67))
		sleep(0.2)
		self.buzzer.stop()

	#song by Eli W, Jan 26, 2020	
	def play_eli_song(self):
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=76))
		sleep(0.2)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.7)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=77))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=76))
		sleep(0.7)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=76))
		sleep(0.2)
		self.buzzer.play(Tone(midi=79))
		sleep(0.2)
		self.buzzer.play(Tone(midi=76))
		sleep(0.2)
		self.buzzer.play(Tone(midi=77))
		sleep(0.7)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=79))
		sleep(0.5)
		self.buzzer.play(Tone(midi=77))
		sleep(0.2)
		self.buzzer.play(Tone(midi=76))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.2)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.stop()
		sleep(0.1)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=76))
		sleep(0.2)
		self.buzzer.play(Tone(midi=72))
		sleep(0.2)
		self.buzzer.play(Tone(midi=74))
		sleep(0.7)
		self.buzzer.stop()