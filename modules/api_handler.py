import requests

class APIHandler:
    def send_audio(self, endpoint, audio_base64):
        """Send the base64 audio to the specified endpoint."""
        payload = {'input': audio_base64}
        try:
            response = requests.post(endpoint, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.RequestException as e:
            print(f"API Request failed: {e}")
            return None
