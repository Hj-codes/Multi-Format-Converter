# Multi-Format-Converter
A versatile Python script for converting images, audio files, and videos to different formats. This script leverages the power of popular Python libraries like Pillow and ffmpeg to provide a comprehensive conversion tool.
## Features:

- **Image Conversion:**
    - Supports conversion to popular image formats (PNG, JPG, JPEG, GIF, BMP).
    - Utilizes the Pillow library for efficient image processing.
- **Audio Conversion:**
    - Supports conversion to widely used audio formats (MP3, WAV).
    - Utilizes the Pydub library for audio file manipulation.
- **Video Conversion:**
    - Supports conversion to common video formats (MP4, AVI, MKV, MOV).
    - Utilizes the MoviePy library for video processing.
## Usage:

1. Clone the repository:
    
    ```bash
    git clone https://github.com/your-username/multi-format-converter.git
    ```
    
2. Navigate to the project directory:
    
    ```bash
    cd multi-format-converter
    ```
    
3. Run the script with the following command:
    
    ```bash
    python ImageConverter.py [file_path] [output_format]
    ```
    
    Replace `[file_path]` with the path to the file you want to convert and `[output_format]` with the desired output format.
    
4. Follow the on-screen menu to choose the conversion type.
5. **Optional: Add Registry Entries for Easy Right-Click Conversion**
    
    To enable right-click conversion in Windows Explorer, you can use the provided batch file:
    
    - Open `add_registry_entries.bat` in a text editor.
    - Replace the paths in the script with the actual paths to your Python executable and `convert.py` script.
    - Save the changes.
    - Right-click on the batch file (`add_registry_entries.bat`) and select "Run as administrator." This will add context menu entries for the supported file formats.
    - **Note:** Adding entries to the Windows Registry requires administrative privileges. Ensure that you run the batch file as an administrator.
6. **Customize File Formats:**
    
    If you want to customize the supported file formats, edit the `add_registry_entries.bat` file and update the `FILE_FORMATS` variable with the desired file extensions.

## Dependencies:
- Pillow: [Documentation](https://pillow.readthedocs.io/en/stable/)
- FFmpeg: [Documentation](https://ffmpeg.org/documentation.html)

## Installation:

1. For Pillow

```bash
pip install pillow

```

1. For FFmpeg (make sure you execute this one line at a time)

```bash
pip install ffmpeg-downloader
ffdl install --add-path
pip install ffmpeg-python
```

## Contributions:

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.
