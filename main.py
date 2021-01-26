from gtts import gTTS
from pdfminer.high_level import extract_text
import gradio as gr
import os


def pdf_to_text(file_obj):
    text = extract_text(file_obj.name)
    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save("test.wav") 
    return 'test.wav'


examples = [
    [os.path.abspath("short-pdf.pdf")],
    [os.path.abspath("long-pdf.pdf")]
]


iface = gr.Interface(fn = pdf_to_text,
                     inputs = 'file',
                     outputs = 'audio', 
                     verbose = True,
                     title = 'PDF to Audio Application',
                     description = 'A simple application to convert PDF files in audio speech. Upload your own file, or click one of the examples to load them.',
                     article = 
                        '''<div>
                            <p style="text-align: center"> All you need to do is to upload the pdf file and hit submit, then wait for compiling. After that click on Play/Pause for listing to the audio. The audio is saved in a wav format.</p>
                        </div>''',
                     examples=examples
                    )

iface.launch()
