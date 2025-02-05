# Create a Python script that processes a directory of media files by:

Folder Parsing: Recursively scanning the provided folder (including subfolders) to locate any audio or video files.
Transcription: Using the Whisper package with the smallest available model to transcribe each media file.
Saving Results: Storing each transcription in a structured format (e.g., text or JSON) alongside the original files or in a designated output folder.

# Key points to remember 
1. To install whisper, you must have older version of python like python3.8, 3.10, or 3.11 as the latest python version doesn't support openai-whisper
2. make sure to create virtual environment to run the script.
3. whisper required ffmpeg for transcribing. So download it from ffmpeg from official website according to your os, open itin winrar and extract it anywhere. Now Copy all he files of bin folder inside the ffmpeg folder and paste it to the folder ffmpeg(create a folder in local disk C with name ffmpeg). After that copy the path(C:\ffmpeg) and add it to the environment variables. Check if it is installed using command "ffmpeg" in cmd

# some commands you need 

# to install whisper
1. to install: pip install openai-whisper
2. to show if it is installed or not : pip show openai-whisper

# to create virtual environment
1. to create : pip -m venv env_name or python -m venv env_name
2. To activate: .\env_name\Scripts\activate

# to run any python file
python .\script.py

# to run my python scripts we need input and output path because of argparse which is a command-line argument
python .\script .\input --output_folder .\output
*Here input is the input folder where inputs are stored which is provided by the user from which os scans for directory media files, output is the output folder where output is stored after transcribing the input as json file and output_folder is the argument in the code for output folder*
