from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Создаем макет
        layout = BoxLayout(orientation='vertical')

        # Добавляем кнопку
        button = Button(text="Нажми меня!", size_hint=(1, 0.5))
        button.bind(on_press=self.on_button_press)

        # Добавляем текстовую метку
        self.label = Label(text="Привет, мир!", size_hint=(1, 0.5))

        # Добавляем элементы в макет
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Изменяем текст метки при нажатии на кнопку
        self.label.text = "Вы нажали кнопку!"

if __name__ == '__main__':
    MyApp().run()
