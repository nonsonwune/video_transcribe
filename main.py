# Import necessary libraries.
import whisper
from moviepy.editor import VideoFileClip

# This function extracts the audio from a video file.
def extract_audio_from_video(video_path):
    # Determine the base name of the video file without the .mp4 extension.
    video_name = video_path.split('.mp4')[0]
    # Open the video file.
    with VideoFileClip(video_path) as video:
        # Extract the audio from the video.
        audio = video.audio
        # Define the path to save the extracted audio.
        output_path = f'extracted_audio/{video_name}_audio.mp3'
        # Save the audio to the defined path.
        audio.write_audiofile(output_path)
        # Return the path of the saved audio.
        return output_path

# This function transcribes the extracted audio.
def transcribe_audio(audio_path):
    # Load the whisper model.
    model = whisper.load_model("base")
    # Transcribe the audio using the whisper model.
    result = model.transcribe(audio_path)
    # Return the transcribed text.
    return result["text"]

# This function saves the transcription to a file.
def save_transcription_to_file(transcription, video_path):
    # Determine the base name of the video file without the .mp4 extension.
    video_name = video_path.split('.mp4')[0]
    # Define the path to save the transcription.
    with open(f"transcription/{video_name}_transciption.txt", "w") as f:
        # Write the transcription to the defined file.
        f.write(transcription)

# Main function to perform the entire process.
def main():
    # Specify the video file to be processed.
    video_file = 'youtube_video.mp4' #change the filename to your desired video path
    # Extract audio from the specified video.
    audio_path = extract_audio_from_video(video_file)
    # Transcribe the extracted audio.
    transcription = transcribe_audio(audio_path)
    # Save the transcription to a file.
    save_transcription_to_file(transcription, video_file)
    # Indicate the completion of the process.
    print("Done")

# Execute the main function when the script is run.
if __name__ == "__main__":
    main()
