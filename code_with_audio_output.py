from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
from playsound import playsound

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("VIT Python Project --Language Translator with Audio")
root.config(bg='ghost white')

# Heading
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='deep sky blue').pack()
Label(root, text="VIT Python Project", font='arial 20 bold', bg='light blue', width='20').pack(side='bottom')

# Input and Output Text Boxes
  
Label(root, text="Enter Text", font='arial 10 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 10 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

# Language options
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')

# Create a dictionary to map full language names to ISO 639-1 codes
lang_code_map = {value: key for key, value in LANGUAGES.items()}

# Translation and audio output
def Translate():
    translator = Translator()
    
    # Get the full text from input and the selected languages
    input_text = Input_text.get(1.0, END)
    src_language = src_lang.get()
    dest_language = dest_lang.get()
    
    # Translate the text
    translated = translator.translate(text=input_text, src=lang_code_map.get(src_language), dest=lang_code_map.get(dest_language))
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

    # Generate audio for the translated text using the ISO 639-1 language code
    tts = gTTS(text=translated.text, lang=lang_code_map.get(dest_language))
    tts.save("translated_audio.mp3")
    
    # Play the audio
    playsound("translated_audio.mp3")
    os.remove("translated_audio.mp3")  # Remove the file after playing


# Translate Button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1', activebackground='sky blue')
trans_btn.place(x=490, y=180)

root.mainloop()