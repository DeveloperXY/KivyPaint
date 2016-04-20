from kivy.app import App
from kivy.base import EventLoop
from kivy.config import Config
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from utils.cursor import *


class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        # Check if any of the children components reacted to the click event
        if Widget.on_touch_down(self, touch):
            # A component has reacted to the click, so don't
            # draw the circle
            return

        with self.canvas:
            # Specify the color of the shape to draw
            Color(*get_color_from_hex('#0080FF80'))
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def clear_canvas(self):
        # Save the children widgets (AKA, the 'DELETE' button)
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        # Restore the saved widgets (AKA, the 'DELETE' button)
        for widget in saved:
            self.add_widget(widget)


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
