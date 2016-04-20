from kivy.app import App
from kivy.base import EventLoop
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from utils.cursor import *


class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        print touch.x, touch.y


class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        if EventLoop.window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse
                a, b = pygame_compile_cursor()
                mouse.set_cursor((24, 24), (9, 9), a, b)
            except:
                pass

        return CanvasWidget()


if __name__ == '__main__':
    Config.set('graphics', 'width', 960)
    Config.set('graphics', 'height', 540)  # 16:9
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')
    # Config.set('graphics', 'resizable', 0)  # Disable window resizing

    from kivy.core.window import Window

    Window.clearcolor = get_color_from_hex('#FFFFFF')
    PaintApp().run()
