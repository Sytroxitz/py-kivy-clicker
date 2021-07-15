from kivy import Config
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class cock(App):

    count = NumericProperty(0)
    amount = NumericProperty(1)
    first_upgrade = NumericProperty(10)
    second_upgrade = NumericProperty(100)
    third_upgrade = NumericProperty(1000)
    fourth_upgrade = NumericProperty(2000)

    def __init__(self, **kwargs):
        super(cock, self).__init__(**kwargs)
        self.called = bool(False)

    def build(self):
        # window configs
        Config.set('graphics', 'fullscreen', 'borderless')
        Config.write()

        # window
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (0.6, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.icon = "images/icon.png"

        # cocked score label widget
        self.label = Label(
            text=f'You cocked {self.count} Times in this session.',
            font_size=18,
            pos_hint="center",
            color="#B8B8B8"
        )

        self.window.add_widget(self.label)

        # info label widget
        self.info = Label(
            text=f'ESC = Quit game',
            font_size=18,
            pos_hint="center",
            color="#2F60B5"
        )

        self.window.add_widget(self.info)

        # cock button
        self.button = Button(
            text="cock",
            bold=True,
            size_hint=(0.1, 0.3),
            background_color="#272A41",
            background_normal=""
        )

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # toggle button
        self.toggle = ToggleButton(
            text="Toggle Upgrades",
            bold=True,
            size_hint=(0.1, 0.1),
            background_color="#2F60B5",
            background_normal=""
        )

        self.toggle.bind(on_press=self.toggle_called)
        self.window.add_widget(self.toggle)

        return self.window

    def toggle_called(self, instance):
        if self.called is True:
            self.called = False
            self.info.text = f'ESC = Quit game\n Upgrades Enabled'
            self.info.color = "#62A56F"
        else:
            self.called = True
            self.info.text = f'ESC = Quit game\n Upgrades Disabled'
            self.info.color = "#9B3533"

    def callback(self, instance):

        if self.called is False:
            if self.count <= 100:
                self.count += self.amount
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +1 per cock"
                self.label.color = "#B8B8B8"
                self.info.text = f'ESC = Quit game\nRewards:\n <100 = +1 cock per cock'
                self.info.color = "#2F60B5"

            if self.count >= 100:
                self.count += self.first_upgrade + self.amount
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +10 per cock"
                self.label.color = "#B8B8B8"
                self.info.text = f'ESC = Quit game\nRewards:\n - 100 = +10 cocks per cock'
                self.info.color = "#2F60B5"

            if self.count >= 1000:
                self.count += self.second_upgrade
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +100 per cock"
                self.label.color = "#B8B8B8"
                self.info.text = f'ESC = Quit game\n Rewards:\n - 100 = +10 cocks per cock\n - 1000 = +100 cocks per cock'
                self.info.color = "#2F60B5"

            if self.count >= 10000:
                self.count += self.third_upgrade
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +1000 per cock"
                self.label.color = "#B8B8B8"
                self.info.text = f'ESC = Quit game\n Rewards:\n - 100 = +10 cocks per cock\n - 1000 = +100 cocks per cock\n - 10000 = +1000 cocks per cock'
                self.info.color = "#2F60B5"

            if self.count >= 200000:
                self.count += self.fourth_upgrade
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +2000 per cock"
                self.label.color = "#B8B8B8"
                self.info.text = f'ESC = Quit game\n Rewards:\n - 100 = +10 cocks per cock\n - 1000 = +100 cocks per cock\n - 10000 = +1000 cocks per cock\n - 200000 = +2000 cocks per cock'
                self.info.color = "#2F60B5"

        else:
            if self.called is True:
                self.count += self.amount
                self.label.text = f"You cocked {self.count:,} Times in this session.\n +1 per cock"
                self.label.color = "#2F60B5"
                self.info.text = f'ESC = Quit game\n Upgrades Disabled'
                self.info.color = "#9B3533"

            else:
                self.label.text = f'ERROR: Failed to add "amount" to your cocked score!'
                self.label.color = "#9B3533"


if __name__ == "__main__":
    cock().run()
