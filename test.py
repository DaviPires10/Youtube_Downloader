import tkinter as tk
from tkinter import ttk
import threading
import yt_dlp


def check_video():
    video_url = entry_url.get()
    try:
        with yt_dlp.YoutubeDL() as ydl:
            
            formats = ydl.extract_info(video_url, download=False).get('formats', [])
            available_options = [f"{fmt['ext']} - {fmt['format_note']}" for fmt in formats]
            options_var.set(available_options)
            
    except yt_dlp.DownloadError:
        options_var.set(["Vídeo não encontrado."])

def download_progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes')
        downloaded_bytes = d.get('downloaded_bytes')
        if total_bytes and downloaded_bytes:
            progress = downloaded_bytes / total_bytes
            progress_bar['value'] = progress * 100
    elif d['status'] == 'finished':
        progress_bar['value'] = 100

def download_video():
    video_url = entry_url.get()
    selected_option = options_listbox.get(options_listbox.curselection())
    format_code = selected_option.split(' - ')[0]
    ydl_opts = {
        'format': format_code,
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [download_progress_hook],
        'embedthumbnail': True
    }

    def download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    # Criar uma nova thread para o download
    download_thread = threading.Thread(target=download)
    download_thread.start()

# Criar janela principal
root = tk.Tk()
root.title("Download de Vídeo")

# Criar widget Label para o URL
label_url = tk.Label(root, text="URL do Vídeo:")
label_url.pack()

# Criar widget Entry para o URL
entry_url = tk.Entry(root)
entry_url.pack()

# Criar widget Button para verificar o vídeo
button_check = tk.Button(root, text="Verificar Vídeo", command=check_video)
button_check.pack()

# Criar widget Options para as opções de download
options_var = tk.StringVar()
options_listbox = tk.Listbox(root, listvariable=options_var, selectmode=tk.SINGLE)
options_listbox.pack()

# Criar widget Button para baixar o vídeo
button_download = tk.Button(root, text="Baixar Vídeo", command=download_video)
button_download.pack()

# Criar widget Progressbar para mostrar o progresso do download
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate')
progress_bar.pack()

# Iniciar loop da interface gráfica
root.mainloop()
