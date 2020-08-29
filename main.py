from kivy.app import App
import gui.windows


class MyApp(App):
    def build(self):
        return gui.windows.kivy_builder


if __name__ == "__main__":
    MyApp().run()
