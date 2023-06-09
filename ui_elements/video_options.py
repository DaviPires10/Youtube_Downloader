from customtkinter import *
from PIL import Image
from threading import Thread
from yt_dlp import YoutubeDL
import requests
from CTkMessagebox import CTkMessagebox

class VideoOptions(CTkScrollableFrame):
    def __init__(self,
                 master,
                 width = 560,
                 height = 800,
                 title: str = '',
                 video_id: str = '',
                 channel_name: str = '',
                 channel_icon: Image.Image | None = None,
                 thumbnail: Image.Image | None = None,
                 duration: str = '',         
                 views: str = '',
                 published_time: str = '',):
        super().__init__(master, width, height)
        
        self.id = video_id

        
        self.thumb = CTkLabel(self,
                              text = None, 
                              image= CTkImage(
                                  thumbnail, 
                                  size=(width, width/1.782)))
        self.thumb.grid(column=0, row= 0)
        
        
        self.duration = CTkLabel(self.thumb,
                                 0, 10,
                                 text= duration,
                                 fg_color= 'black')
        self.duration.grid(column= 0, row= 0, sticky= SE, padx=3, pady=3)
        
        
        self.title = CTkTextbox(self,
                                width, 80,
                                font= (None, 16),
                                fg_color= 'transparent',
                                wrap='word')
        self.title.insert("0.0", title)
        self.title.configure(state= DISABLED)
        self.title.grid(column=0, row= 1)
       
        self.info_bar = CTkLabel(self,
                                 font= (None, 12),
                                 text= f'{views}  •  {published_time}',
                                 text_color= 'gray50')

        
    def download(self, format: str):
            
        try:
            requests.get('https://google.com/')
        except:
            CTkMessagebox(message='No internet Connection!', icon='cancel')
            return    

        try:  
    
            if format == 'Video':
            
                output_directory = filedialog.asksaveasfilename(
                    confirmoverwrite=True, defaultextension= '.mp4', filetypes= [('Video files', '*.mp4')],
                    initialdir= os.path.expanduser("~") + "/Downloads/", initialfile= self.title, title= 'Save as')
                
                
                print(output_directory)
                yt_opts = {
                    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]',
                    'embedthumbnail': True
                    }
                                                    
            elif format == 'Audio':

                output_directory = filedialog.asksaveasfilename(
                    confirmoverwrite = True, defaultextension = '.mp3', filetypes = [('Audio files', '*.mp3')],
                    initialdir = os.path.expanduser("~") + "/Downloads/", initialfile = self.title, title= 'Save as')
                
                    
                yt_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
            
            with YoutubeDL(yt_opts) as yt:
                info_dict = yt.extract_info(self.id, download=False)
                file = yt.prepare_filename(info_dict, outtmpl= info_dict['title'])

                if not os.path.isfile(file):
                    yt.download([self.id])

                    print(f"File saved as {file}")
                        
        except:
            CTkMessagebox(message=f"Sorry! Couldn't download your {type} :( ")
            return
        

        CTkMessagebox(message=type + " Downloaded", icon='check',
                    option_text_2="Open File", option_command_2=lambda: os.startfile(file))

    def check_video(self):

        try:
            with YoutubeDL() as ydl:
                info = ydl.extract_info(self.id, download=False)
                formats = info.get('formats', [])
                available_options = []
                for fmt in formats:
                    ext = fmt['ext']
                    format_note = fmt['format_note']
                    option = f"{ext} - {format_note}"
                    available_options.append(option)

        except:
            ...
            
if __name__ == '__main__':
    
    app = CTk()
    
    app.geometry('560x650')
    # app.wm_attributes('-transparentcolor', '#242424')

    VideoOptions(app, title= 'Pneumonoultramicroscopicsilicovolcanoconiosis is the biggest world in english and i dont know why, this title is crazy and i can prove it somehow by showing it to you',
                thumbnail= Image.open('images\images.jpg'),
                channel_icon= Image.open('images\Fortnite.png'), 
                channel_name= 'Sixty Nineteen', 
                duration= '12:17:23',
                views= '45K views',
                published_time= 'Tomorrow').pack()


    app.mainloop()