import os
import json
import argparse
import whisper
from pathlib import Path
import warnings

warnings.simplefilter("ignore", category=FutureWarning)

def find_media_files(directory):
    """Recursively find audio and video files in a directory."""
    media_extensions = {'.mp3', '.wav', '.m4a', '.mp4', '.mov', '.avi', '.mkv'}
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in media_extensions:
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_media(file_path, model):
    """Transcribe a media file using Whisper."""
    print(f"Processing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(file_path, text, output_dir):
    """Save the transcription to a text file."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{Path(file_path).stem}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"file": file_path, "transcription": text}, f, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Transcribe media files in a folder.")
    parser.add_argument("input_folder", type=str, help="Path to the input folder containing media files")
    parser.add_argument("--output_folder", type=str, default="transcriptions", help="Path to the output folder for transcriptions")
    args = parser.parse_args()

    if not Path(args.input_folder).exists():
        print(f"Error: The specified input folder '{args.input_folder}' does not exist.")
        return

    model = whisper.load_model("tiny", download_root="./models", device='cpu')
    media_files = find_media_files(args.input_folder)

    if not media_files:
        print(f"No media files found in '{args.input_folder}'.")
        return

    print(f"Found {len(media_files)} media files. Processing...")
    
    processed_files = set()  # Prevent duplicates
    for file in media_files:
        if file in processed_files:
            print(f"Skipping duplicate: {file}")
            continue  # Skip already processed files
        
        text = transcribe_media(file, model)
        save_transcription(file, text, args.output_folder)
        print(f"✅ Transcription saved: {file}")

        processed_files.add(file)  # Mark as processed


if __name__ == "__main__":
    main()


    
# import os
# import json
# import argparse
# import whisper
# from pathlib import Path

# def find_media_files(directory):
#     """Recursively find audio and video files in a directory."""
#     media_extensions = {'.mp3', '.wav', '.m4a', '.mp4', '.mov', '.avi', '.mkv'}
#     media_files = []
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if Path(file).suffix.lower() in media_extensions:
#                 media_files.append(os.path.join(root, file))
#     return media_files

# def transcribe_media(file_path, model):
#     """Transcribe a media file using Whisper."""
#     print(f"Processing: {file_path}")
#     result = model.transcribe(file_path)
#     return result["text"]

# def save_transcription(file_path, text, output_dir):
#     """Save the transcription to a text file."""
#     output_dir = Path(output_dir)
#     output_dir.mkdir(parents=True, exist_ok=True)
#     output_file = output_dir / f"{Path(file_path).stem}.json"
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump({"file": file_path, "transcription": text}, f, ensure_ascii=False, indent=4)

# def main():
#     parser = argparse.ArgumentParser(description="Transcribe media files in a folder.")
#     parser.add_argument("input_folder", type=str, help="Path to the input folder.")
#     parser.add_argument("--output_folder", type=str, default="transcriptions", help="Path to the output folder.")
#     args = parser.parse_args()

#     model = whisper.load_model("tiny")  # Load the smallest Whisper model
#     media_files = find_media_files(args.input_folder)
    
#     for file in media_files:
#         text = transcribe_media(file, model)
#         save_transcription(file, text, args.output_folder)
#         print(f"Transcription saved: {file}")

# if __name__ == "__main__":
#     main()
