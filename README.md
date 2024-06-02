# AudioToText
Convert your audio to text

### Se uso el modelo de <a href="https://github.com/openai/whisper">Modelo</a>

# AudioToText Transcription App (Beta v1)

This is a simple application built with Python and the Tkinter GUI library. It allows you to transcribe audio files (MP3) to text using the Whisper speech recognition model from OpenAI.

## Features

- Select the desired model quality for transcription (tiny, base, small, medium, large)
- Browse and select an MP3 audio file
- Choose the output file location to save the transcribed text
- Real-time transcription progress display
- Transcription time reporting

## Requirements

- Python 3.x
- Tkinter (usually included with Python installation)
- Whisper library (`pip install whisper`)

## Usage

1. Run the `audio_to_text.py` script.
2. Select the desired model quality for transcription from the radio buttons.
3. Click the "Select Audio File" button and choose an MP3 audio file.
4. Select the output file location and name for saving the transcribed text.
5. Wait for the transcription process to complete. The application will display the transcription time.
6. The transcribed text will be saved in the specified output file.

## File Structure

```
AudioToText/
├── audio_to_text.py
└── icon.ico
```

- `audio_to_text.py`: The main Python script containing the application code.
- `icon.ico`: Optional icon file for the application window.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This application uses the following open-source libraries:

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Standard Python GUI library
- [Whisper](https://github.com/openai/whisper) - Speech recognition model by OpenAI

We appreciate the developers and communities who have contributed to these tools.
