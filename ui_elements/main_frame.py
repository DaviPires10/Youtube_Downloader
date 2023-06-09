from customtkinter import *
from CTkMessagebox import CTkMessagebox
import requests
from io import BytesIO
from threading import Thread
from youtubesearchpython import VideosSearch


from video_card import VideoCard
from video_options import VideoOptions
from image_manager import ImageManager, Image


class MainFrame(CTkFrame):
    def __init__(self, master, width= 560, height= 800, fg_color= 'transparent'):
        super().__init__(master, width, height, fg_color= fg_color)
        
        master.protocol('WM_DELETE_WINDOW', sys.exit)
        
        
        self.search_frame = CTkFrame(self, 560, 50, fg_color= fg_color)
        self.search_frame.pack(fill=X, padx=6)
        
        self.search_entry = CTkEntry(self.search_frame, 480, 35, 26, placeholder_text= 'Search')
        self.search_entry.bind('<Return>', self.search_videos)
        self.search_entry.grid_configure(column=0,row=0, pady= 3, padx=5)
        
        self.search_button = CTkButton(self.search_frame,
                                       32, 32,
                                       text= None,
                                       image= CTkImage(
                                            ImageManager.LIGHT_SEARCH_IMAGE,
                                            ImageManager.DARK_SEARCH_IMAGE,
                                           size=(40, 40)),
                                       fg_color='transparent',
                                       hover= False, 
                                       cursor= 'hand2',
                                       command= self.search_videos)
        self.search_button.grid(column=1, row=0, sticky=E, pady=3, padx=2)
        
        self.videos_frame = CTkScrollableFrame(self, 550, 750, fg_color= fg_color)
        self.videos_frame.pack(fill=BOTH)

    def run_in_thread(func):
        def wrapper(*args, **kwargs):
            thread = Thread(target=func, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return wrapper

    def try_connection(self):
        try:
            requests.get('https://www.google.com/')
            return True
        except:
            CTkMessagebox(self.master, title='Warning',  message='No Internet Connection!')
            return False
        
    @run_in_thread
    def search_videos(self, event=None):
       
        if not self.try_connection():
            return

        [widget.pack_forget() for widget in self.videos_frame.winfo_children()]
        self.videos_frame._parent_canvas.yview_moveto(0)

        self.search_button.configure(command=None)
        self.search_entry.unbind('<Return>')

        query = self.search_entry.get()
        results = VideosSearch(query).result()['result']
        print(results)
        
        for result in results:
            try:
                if result['publishedTime'] is not None and result['duration'] is not None:
                    
                    title = result['title']
                    video_id = result['id']
                    channel_name = result['channel']['name']
                    published_time = result['publishedTime']
                    duration = result['duration']
                    views = result['viewCount']['short']
                    thumbnail = Image.open(BytesIO(requests.get(result['thumbnails'][0]['url']).content))
                    channel_icon = Image.open(BytesIO(requests.get(result['channel']['thumbnails'][0]['url']).content))

                    VideoCard(self.videos_frame, 525, 120,
                            title, video_id, channel_name,
                            channel_icon, thumbnail, duration,
                            views, published_time).pack(pady=6, fill=X)
                    self.update_idletasks()
                else:
                    print('sim')
            except:
                print("NÃO")

        self.search_button.configure(command= self.search_videos)
        self.search_entry.bind('<Return>', self.search_videos)


app= CTk()
app.geometry('560x640')
MainFrame(app).pack(padx=5)
app.mainloop()