from customtkinter import *
from PIL import Image
import os

from image_manager import ImageManager
from video_options import VideoOptions

class VideoCard(CTkFrame):
    def __init__(self, 
                 master,
                 width: int = 550,
                 height: int = 120,
                 title: str = '',
                 video_id: str = '',
                 channel_name: str = '',
                 channel_icon: Image.Image = None,
                 thumbnail: Image.Image = None,
                 duration: str = '',         
                 views: str = '',
                 published_time: str = ''):

        super().__init__(master,
                         width=width,
                         height= height,
                         cursor='hand2')        
        
        self.title = title
        self.video_id = video_id
        self.channel_name = channel_name
        self.channel_icon = channel_icon
        self.thumbnail = thumbnail
        self.duration = duration
        self.views = views
        self.published_time = published_time

        
        self.thumbnail_label = CTkLabel(self,
                                  text= None,
                                  image= (CTkImage(thumbnail,
                                  size=(212, 118.96))),
                                  cursor= 'hand2')
        self.thumbnail_label.grid(column= 0, row= 0, sticky= W, pady=3, padx= 3)
        
        
        self.duration_label = CTkLabel(self.thumbnail_label,
                                 0, 10,
                                 text= duration,
                                 text_color='white',
                                 fg_color= 'black',
                                 cursor= 'hand2')
        self.duration_label.grid(column= 0, row= 0, sticky= SE, padx=3, pady=3)
        
        
        self.info_frame = CTkFrame(self,
                                   width - 212, height,
                                   fg_color= 'transparent')
        self.info_frame.grid(column= 1, row= 0, padx=1)
        
        
        self.title_textbox = CTkTextbox(self.info_frame,
                                width-212, 50,
                                font= CTkFont(None, 14),
                                fg_color= 'transparent',
                                wrap='word',
                                cursor= 'hand2',
                                activate_scrollbars=False)
        if len(title) > 91:
            self.title_textbox.insert("0.0", title[:90] + '...')
        else:
            self.title_textbox.insert("0.0", title)
        self.title_textbox.configure(state= DISABLED)
        self.title_textbox.pack(pady=1, anchor= NW)
        

        self.view_label = CTkLabel(self.info_frame,
                                 text= f'{views}  •  {published_time}',
                                 text_color= 'gray50',
                                 cursor= 'hand2')
        self.view_label.pack(pady=2, padx= 6, anchor= W)
        
        
        self.channel_label = CTkLabel(self.info_frame,
                                text= '  ' + channel_name,
                                image= CTkImage(
                                    ImageManager.circle_mask(channel_icon), 
                                    size=(23, 23)),
                                compound= LEFT,
                                cursor= 'hand2')
        self.channel_label.pack(pady=4, padx= 6, anchor= W)

        
        self.bind('<ButtonPress-1>', self.get)
        [widget.bind('<ButtonPress-1>', self.get) for widget in self.winfo_children()]
        [widget.bind('<ButtonPress-1>', self.get) for widget in self.info_frame.winfo_children()]

    def get(self, event):
        return {
            'title': self.title,
            'video_id': self.video_id,
            'channel_name': self.channel_name,
            'channel_icon': self.channel_icon,
            'thumbnail': self.thumbnail,
            'duration': self.duration,
            'views': self.views,
            'published_time': self.published_time
        }
    
        
if __name__ == '__main__':
    import os
    os.system('cls')

    
    
    app = CTk()
    app.geometry('550x650')
    # app.wm_attributes('-transparentcolor', '#242424')

    
    for i in range(1):    
        VideoCard(app, title= 'Pneumonoultramicroscopicsilicovolcanoconiosis is the biggest world in english and i dont know why, this title is crazy and i can prove it somehow by showing it to you',
                  thumbnail= Image.open('images\images.jpg'),
                  channel_icon= Image.open('images\Fortnite.png'), 
                  channel_name= 'Sixty Nineteen', 
                  duration= '12:17:23',
                  views= '45K views',
                  published_time= 'Tomorrow').pack(pady=7, padx= 3)


    app.mainloop()
    
    
    