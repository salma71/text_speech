from gtts import gTTS
from pdfminer.high_level import extract_text
import gradio as gr

def pdf_to_text(file_obj):
    text = extract_text(file_obj.name)
    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save("test.wav") 
    return 'test.wav'

iface = gr.Interface(fn = pdf_to_text, 
                     inputs = 'file', 
                     outputs = 'audio', 
                     title = 'PDF into speech Application',
                     description = 'Simple application in python to try the Gradio package components',
                     article = 
                        '''<div>
                            <p> All you need to do is to upload the pdf file and hit submit, then wait for compiling. After that click on Play/Pause for listing to the audio. The audio is saved in a wav format.</p>
                        </div>'''
                    )
iface.launch()
