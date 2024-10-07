import subprocess
import os
import glob
import speech_recognition as sr


def extract_audio_from_mp4(mp4_file, audio_file):
    """
    Extracts audio from an MP4 file and saves it as a WAV file.
    :param mp4_file: Path to the input MP4 file
    :param audio_file: Path to the output WAV file
    """
    command = f'ffmpeg -i "{mp4_file}" -q:a 0 -map a "{audio_file}" -y'
    subprocess.run(command, shell=True, check=True)


def transcribe_audio(audio_file):
    """
    Transcribes speech from an audio file to text.
    :param audio_file: Path to the audio file
    :return: Transcribed text
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Correct method to capture the audio data
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio"


if __name__ == "__main__":
    # Get a list of all MP4 files in the current directory
    mp4_files = glob.glob("*.mp4")

    for mp4_file in mp4_files:
        # Define the corresponding audio and transcript file names
        base_name = os.path.splitext(mp4_file)[0]
        audio_file = f"{base_name}.wav"
        transcript_file = f"{base_name}.txt"

        # Extract audio from MP4
        print(f"Extracting audio from {mp4_file}...")
        extract_audio_from_mp4(mp4_file, audio_file)

        # Transcribe audio to text
        print(f"Transcribing audio from {audio_file}...")
        transcript = transcribe_audio(audio_file)

        # Save the transcript to a text file
        with open(transcript_file, "w") as file:
            file.write(transcript)

        # Optionally, delete the audio file to save space
        os.remove(audio_file)

        print(f"Transcription complete for {mp4_file}. Check {transcript_file} for the output.")
