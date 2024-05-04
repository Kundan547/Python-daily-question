import moviepy.editor
import tkinter as tk
from tkinter.filedialog import askopenfilename

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    vid = askopenfilename()

    if vid:
        video = moviepy.editor.VideoFileClip(vid)
        aud = video.audio
        aud.write_audiofile("demo.mp3")
        print("__end__")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
