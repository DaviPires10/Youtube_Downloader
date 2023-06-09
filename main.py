from customtkinter import *

from  ui_elements import VideoOptions

class Tabs(CTkTabview):
    def __init__(self, master: any, width: int = 300, height: int = 250):
        super().__init__(master, width, height)
        
        self.settings_tab = self.add('SettingsTab')
        self.search_tab = self.add('SearchTab')
        self.video_tab = VideoOptions(self.add('VideoTab'))
        
        self._segmented_button.destroy()