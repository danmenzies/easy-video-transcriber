# Easy Video Transcriber

A Python script that automatically extracts audio from MP4 video files and transcribes the speech to text using Google's Web Speech API. This project is ideal for users who need to convert video content into readable text for documentation, content creation, or other purposes.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Requirements](#requirements)
5. [Contributing](#contributing)
6. [License](#license)

---

## Features

- **Audio Extraction**: Extracts audio from MP4 files using `ffmpeg`.
- **Speech Transcription**: Converts extracted audio into text using the Google Web Speech API.
- **Automated Processing**: Scans for all MP4 files in the current directory and processes them automatically.
- **File Cleanup**: Automatically deletes the intermediate audio file after transcription to save space.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- FFmpeg: Used for audio extraction from videos. You can download and install it from [here](https://ffmpeg.org/download.html).
- Google Web Speech API dependencies via the `speech_recognition` library.

### Steps to install

1. Clone the repository:

   ```bash
   git clone https://github.com/danmenzies/easy-video-transcriber.git
   cd easy-video-transcriber
   ```

2. (Optional) Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Install FFmpeg and ensure it’s available in your system’s PATH.

---

## Usage

1. Place all the MP4 files you want to transcribe in the script's directory.

2. Run the script:

   ```bash
   python main.py
   ```

3. The script will:
   - Extract audio from each MP4 file.
   - Transcribe the audio to text.
   - Save the transcription in a text file with the same base name as the video (e.g., `video.mp4` will generate `video.txt`).

4. After transcription, the temporary WAV file will be deleted to conserve disk space.

Example output:

```
Extracting audio from video.mp4...
Transcribing audio from video.wav...
Transcription complete for video.mp4. Check video.txt for the output.
```

---

## Requirements

- Python 3.x
- `ffmpeg`: Required for audio extraction.
- Python libraries:
  - `speech_recognition`
  - `glob` (standard library)
  - `os` (standard library)
  - `subprocess` (standard library)

You can install the Python dependencies using the `requirements.txt` file.

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/feature_name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/feature_name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` can serve as the documentation for your **Easy Video Transcriber** project. If you'd like to add more details or customization, feel free to let me know!