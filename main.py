import tkinter as tk
from tkinter import filedialog
import whisper
import time

def transcribe_audio():
    selected_model = model_var.get()
    audio_file = filedialog.askopenfilename(title="Seleccionar archivo de audio", filetypes=[("Archivos MP3", "*.mp3")])
    
    if not audio_file:
        return
    
    output_file = filedialog.asksaveasfilename(title="Guardar archivo de texto", defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    
    if not output_file:
        return
    
    try:
        model = whisper.load_model(selected_model)
    except Exception as e:
        result_label.config(text="Error al cargar el modelo: " + str(e))
        return

    start_time = time.time()
    result = model.transcribe(audio_file)
    elapsed_time = time.time() - start_time
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result["text"])
    
    result_label.config(text="Transcripción completada en {:.2f} segundos".format(elapsed_time))

app = tk.Tk()
app.title("Audio a Texto Beta v1")
app.iconbitmap("icon.ico")
model_var = tk.StringVar(value="medium")

model_frame = tk.Frame(app)
model_frame.pack()

tk.Label(model_frame, text="Seleccione Calidad de texto (Recomendada: medium):").pack()
model_choices = ["tiny", "base", "small", "medium", "large"]
for model_choice in model_choices:
    tk.Radiobutton(model_frame, text=model_choice, variable=model_var, value=model_choice).pack()

file_button = tk.Button(app, text="Seleccionar archivo de audio", command=transcribe_audio)
file_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
