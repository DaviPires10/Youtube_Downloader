import subprocess

def embed_thumbnail(caminho_video, caminho_capa, caminho_saida):
    command = f'ffmpeg -i "{caminho_video}" -i "{caminho_capa}" -map 0 -map 1 -c copy -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "{caminho_saida}"'
    subprocess.run(command, shell=True)
    
video = r'C:\Users\davip\Área de Trabalho\Python_Projects\Youtube_Downloader\12 VEZES QUE O FORTNITE MOSTROU O FUTURO.mp4'
image = r'C:\Users\davip\Área de Trabalho\Python_Projects\Youtube_Downloader\images\images.jpg'

adicionar_capa_video_ffmpeg(video, image, video)