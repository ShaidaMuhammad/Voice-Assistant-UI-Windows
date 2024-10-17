# Voice Based Arabic AI Assistant Interface

This is a PyQt5-based application that allows users to record audio, process it, and submit it to the ML-Backend API. It uses `pyaudio` for recording, `sounddevice` for audio playback, and `base64` encoding to send and receive audio data via the API.

## Features

- Record audio using your microphone
- Submit recorded audio to a custom API endpoint (contact me for further details)
- Receive audio responses from the API, including both playback and textual output
- User-friendly interface built with PyQt5

## Requirements

To run the application, you'll need the following dependencies installed:

- Python (Tested on version 3.11.10)
- PyQt5
- pyaudio
- sounddevice
- numpy

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## File Structure

```
.
├── main.py                # The main file to launch the PyQt5 application
├── modules/
│   ├── audio_handler.py   # Module for handling audio recording, playback, and processing
│   ├── api_handler.py     # Module for sending/receiving audio data to/from an API (not included)
├── ui/
│   ├── main_window.py     # UI setup for the main window (auto-generated from .ui file)
└── assets/
    └── output.wav         # Output file where the recorded audio is saved
```

## How to Use

1. **Record Audio:**
   - Click on the "Record Voice" button to start recording audio.
   - Click on "Stop Recording" to finish the recording.

2. **Submit Audio:**
   - Enter an API endpoint in the designated text box.
   - Click on the "Submit" button to send the audio for processing.

3. **Receive and Play Response:**
   - If the API returns an audio response, the app will automatically play it back and display any textual response in the status box.

## Customization

### API Handler

The `api_handler.py` module is expected to handle the interaction with the API. You'll need to customize this module based on the API specifications you're working with. Ensure that it sends the audio as base64 and processes the response properly.

### Error Handling

Make sure to handle any audio device issues (like access to the microphone), or customize how the app deals with unavailable APIs.

### Contact

Feel free to reach out via any of the following platforms:

- **Email:** [shaidasherpao@gmail.com](mailto:shaidasherpao@gmail.com)
- **WhatsApp:** [+923139190354](https://wa.me/923139190354) (Tap to message)
- **LinkedIn:** [Shaida Muhammad](https://www.linkedin.com/in/shaidamuhammad)
- **Twitter:** [@ShaidaSherpao](https://twitter.com/ShaidaSherpao)
- **GitHub:** [ShaidaMuhammad](https://github.com/ShaidaMuhammad)
- **Facebook:** [Shaida Muhammad](https://facebook.com/shaida.muhd)

