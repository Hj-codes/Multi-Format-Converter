# Updated script (ImageConverter.py)

from PIL import Image
import sys
import os
import ffmpeg

def convert_image(file_path, output_format):
    try:
        image = Image.open(file_path)
        if 'A' in image.getbands():
            image = image.convert('RGB')
        output_path = os.path.splitext(file_path)[0] + output_format
        image.save(output_path)
        print(f"Image conversion successful. Saved as {output_path}")
    except Exception as e:
        print(f"Error during image conversion: {e}")
        input("Press Enter to exit...")

def convert_audio(file_path, output_format):
    try:
        output_path = os.path.splitext(file_path)[0] + "." +  output_format
        ffmpeg.input(file_path).output(output_path).run()
        print(f"Audio conversion successful. Saved as {output_path}")
    except Exception as e:
        print(f"Error during audio conversion: {e}")
        input("Press Enter to exit...")

def convert_video(file_path, output_format):
    try:
        output_path = os.path.splitext(file_path)[0] + output_format
        ffmpeg.input(file_path).output(output_path).run()
        print(f"Video conversion successful. Saved as {output_path}")
    except Exception as e:
        print(f"Error during video conversion: {e}")
        input("Press Enter to Exit....")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        output_format = sys.argv[2].lower()
        image_formats = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
        audio_formats = [".mp3", ".wav"]
        video_formats = [".mp4", ".avi", ".mkv", ".mov"]

        if output_format in image_formats:
            convert_image(file_path, output_format)
        elif output_format in audio_formats:
            convert_audio(file_path, output_format)
        elif output_format in video_formats:
            convert_video(file_path, output_format)
        else:
            print("Unsupported format. Supported image formats:", ", ".join(image_formats), "Supported audio formats:", ", ".join(audio_formats), "Supported video formats:", ", ".join(video_formats))
    else:
        print("Usage: python ImageConverter.py [file_path] [output_format]")

