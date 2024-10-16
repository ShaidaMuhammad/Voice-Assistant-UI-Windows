import sys
from PyQt5 import QtWidgets, QtCore
from ui.main_window import Ui_MainWindow
from modules.audio_handler import AudioHandler
from modules.api_handler import APIHandler

class AudioAssistantApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudioAssistantApp, self).__init__()
        self.setupUi(self)  # Setup the UI

        # Initialize the audio handler and API handler
        self.audio_handler = AudioHandler()
        self.api_handler = APIHandler()

        # Set up recording state and two timers
        self.is_recording = False  # Track whether recording is in progress
        self.chunk_timer = QtCore.QTimer()  # Timer to capture audio chunks
        self.chunk_timer.timeout.connect(self.capture_audio_chunk)  # Capture audio chunks

        self.time_timer = QtCore.QTimer()  # Timer to update recording time
        self.time_timer.timeout.connect(self.update_recording_time)  # Update recording time
        self.recording_time = 0  # Counter for recording time in seconds

        # Connect buttons to their actions
        self.recordButton.clicked.connect(self.toggle_recording)
        self.submitButton.clicked.connect(self.submit_audio)

    def toggle_recording(self):
        """Start or stop recording audio depending on the current state."""
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        """Start recording and change the button text to 'Stop Recording'."""
        self.audio_handler.start_audio_stream()  # Start recording
        self.recording_time = 0  # Reset the recording time
        self.chunk_timer.start(100)  # Capture audio every 100 milliseconds
        self.time_timer.start(1000)  # Update the recording time every 1 second
        self.recordButton.setText("Stop Recording")  # Change button text
        self.statusBox.setPlainText("Recording in progress...")  # Display recording status
        self.is_recording = True  # Set recording state to True

    def stop_recording(self):
        """Stop recording and change the button text back to 'Record Voice'."""
        self.audio_handler.stop_audio_stream()  # Stop the audio recording
        self.chunk_timer.stop()  # Stop capturing audio chunks
        self.time_timer.stop()  # Stop the timer updating the seconds
        self.recordButton.setText("Record Voice")  # Change button text back
        self.statusBox.setPlainText(f"Recording finished. Duration: {self.recording_time} seconds.")  # Display duration
        self.is_recording = False  # Set recording state to False

    def capture_audio_chunk(self):
        """Capture chunks of audio data while recording is in progress."""
        self.audio_handler.record_chunk()  # Capture a chunk of audio data

    def update_recording_time(self):
        """Update the recording time every second and display it in the status box."""
        self.recording_time += 1
        self.statusBox.setPlainText(f"Recording in progress... {self.recording_time} seconds")

    def submit_audio(self):
        """Submit the recorded audio to the API."""
        if self.is_recording:
            self.stop_recording()  # Automatically stop recording if submit is pressed while recording

        endpoint = self.endpointInput.text()
        if not endpoint:
            self.statusBox.setPlainText("Please provide an API endpoint.")
            return

        audio_base64 = self.audio_handler.convert_audio_to_base64()
        if audio_base64:
            response = self.api_handler.send_audio(endpoint, audio_base64)
            if response:
                output_audio_base64 = response.get('response_audio')
                output_in_text_formate = response.get('response_text')

                if output_audio_base64:
                    self.audio_handler.play_audio_from_base64(output_audio_base64)
                    # self.statusBox.setPlainText("Audio played successfully.")
                    self.statusBox.setPlainText(output_in_text_formate)
                else:
                    self.statusBox.setPlainText("No output received from the API.")
            else:
                self.statusBox.setPlainText("Failed to get a valid response from the API.")
        else:
            self.statusBox.setPlainText("No audio recorded.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AudioAssistantApp()
    window.show()
    sys.exit(app.exec_())
