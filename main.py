from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget

Config.set('graphics', 'width', 960)
Config.set('graphics', 'height', 540)  # 16:9
# Config.set('graphics', 'resizable', 0)  # Disable window resizing

from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class CanvasWidget(Widget):
    pass


class PaintApp(App):
    def build(self):
        return CanvasWidget()


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    PaintApp().run()
