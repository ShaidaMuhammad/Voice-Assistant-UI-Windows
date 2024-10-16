import pyaudio
import wave
import base64
from io import BytesIO

CHUNK = 8096  # Number of frames in each buffer
FORMAT = pyaudio.paInt16  # 16-bit format for better sound quality
CHANNELS = 4  # Mono recording
RATE = 48000  # Sample rate in Hertz
WAVE_OUTPUT_FILENAME = "assets/output.wav"

class AudioHandler:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None  # Will hold the stream
        self.frames = []  # Holds recorded audio frames

    def start_audio_stream(self):
        """Start the audio recording stream."""
        try:
            self.stream = self.audio.open(format=FORMAT,
                                          channels=CHANNELS,
                                          rate=RATE,
                                          input=True,
                                          frames_per_buffer=CHUNK)
            self.frames = []  # Clear any previous audio data
            print("Audio stream opened and recording started...")
        except Exception as e:
            print(f"Error starting audio stream: {e}")

    def record_chunk(self):
        """Read a chunk of audio from the stream and append to the frames."""
        if self.stream:
            try:
                data = self.stream.read(CHUNK, exception_on_overflow=True)  # Capture audio chunk
                self.frames.append(data)  # Append captured data
                print(f"Captured audio chunk of size {len(data)}")
            except Exception as e:
                print(f"Error reading audio chunk: {e}")

    def stop_audio_stream(self):
        """Stop the audio stream and save the audio data to a file."""
        if self.stream:
            # Stop and close the audio stream
            try:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None  # Reset the stream
                print("Audio stream stopped.")
                self._save_to_wav()  # Save to file after stopping
            except Exception as e:
                print(f"Error stopping audio stream: {e}")

    def _save_to_wav(self):
        """Save the recorded audio data to a WAV file."""
        try:
            with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(self.audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(self.frames))  # Write audio frames to WAV file
                print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
        except Exception as e:
            print(f"Error saving audio to WAV: {e}")

    def convert_audio_to_base64(self):
        """Convert recorded WAV audio to base64."""
        try:
            with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
                audio_data = f.read()
            return base64.b64encode(audio_data).decode('utf-8')
        except FileNotFoundError:
            print("WAV file not found, could not convert to base64.")
            return None

    def play_audio_from_base64(self, audio_base64):
        """Play audio from base64 encoded string."""
        try:
            audio_data = base64.b64decode(audio_base64)
            wf = wave.open(BytesIO(audio_data), 'rb')

            stream = self.audio.open(format=self.audio.get_format_from_width(wf.getsampwidth()),
                                     channels=wf.getnchannels(),
                                     rate=wf.getframerate(),
                                     output=True)
            data = wf.readframes(CHUNK)
            while data:
                stream.write(data)
                data = wf.readframes(CHUNK)

            stream.stop_stream()
            stream.close()
            print("Audio played from base64.")
        except Exception as e:
            print(f"Error playing audio from base64: {e}")
