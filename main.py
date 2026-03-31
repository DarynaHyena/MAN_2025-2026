''' Імпортування бібліотек'''

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.button        import Button
from kivy.uix.label         import Label
from kivy.uix.textinput     import TextInput
from kivy.uix.checkbox      import CheckBox
from kivy.metrics           import dp

'''Кінець блоку імпортування бібліотек'''





class Screens(Screen):
  def __init__(self,kw): 
    super().__init__(**kw)
    # поточний етап (1-2)
    self.stage = 1

    # загальні віджети
    self.anchor = AnchorLayout()
    self.container = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))

    # контейнери
    self.cloud_container = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
    self.cloud_button_container1 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.cloud_button_container2 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.cloud_button_container3 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.cloud_button_container4 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))

    self.season_container = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
    self.season_button_container1 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.season_button_container2 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.season_button_container3 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.season_button_container4 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))

    self.location_container = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
    self.location_button_container1 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.location_button_container2 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    self.location_button_container3 = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    

    # поля вводу
    self.temperature_input = TextInput(hint_text='Температура', size_hint_y=None, height=dp(44))
    self.humidity_input = TextInput(hint_text='Вологість',   size_hint_y=None, height=dp(44))
    self.wind_speed_input = TextInput(hint_text='', size_hint_y=None, height=dp(44))
    self.precipitation_input = TextInput(hint_text='', size_hint_y=None, height=dp(44))
    self.atmoshperic_pressure_input = TextInput(hint_text='', size_hint_y=None, height=dp(44))

    # кнопки
    self.cloud_cover_button = CheckBox()
    self.season_button = CheckBox()
    self.location_button = CheckBox()
    self.commit_button = Button(text='Підтвердити результат', size_hint_y=None, height=dp(48))

    # підключаємо обробники
    




    # збираємо
    self.anchor.add_widget(self.container)
    self.add_widget(self.anchor)

    # показуємо перший етап
    self.build_stage()

  def build_stage(self):
    self.container.clear_widgets()
    
    if self.stage == 1:
      # Етап 1: анкета
        self.container.add_widget(Label(text='Введіть дані про температуру: ', font_size='18sp', color=(0,0,0,1)))
        self.container.add_widget(self.temperature_input)
        self.container.add_widget(Label(text='Введіть дані про вологість: ', font_size='18sp', color=(0,0,0,1)))
        self.container.add_widget(self.humidity_input)
        self.container.add_widget(Label(text='Введіть дані про швидкість руху повітря (м/с): ', font_size='18sp', color=(0,0,0,1)))
        self.container.add_widget(self.wind_speed_input)
        self.container.add_widget(Label(text='Введіть дані про кількість опадів в рік: ', font_size='18sp', color=(0,0,0,1)))
        self.container.add_widget(self.precipitation_input)
        self.container.add_widget(Label(text='Введіть дані про хмарність: ', font_size='18sp', color=(0,0,0,1)))

        self.cloud_button_container1.add_widget(Label(text='Похмуро', font_size='18sp', color=(0,0,0,1)))
        self.cloud_button_container1.add_widget(self.cloud_cover_button)
        self.cloud_button_container2.add_widget(Label(text='Мінлива хмарність', font_size='18sp', color=(0,0,0,1)))
        self.cloud_button_container2.add_widget(self.cloud_cover_button)
        self.cloud_button_container3.add_widget(Label(text='Безхмарно', font_size='18sp', color=(0,0,0,1)))
        self.cloud_button_container3.add_widget(self.cloud_cover_button)
        self.cloud_button_container4.add_widget(Label(text='Хмарно', font_size='18sp', color=(0,0,0,1)))
        self.cloud_button_container4.add_widget(self.cloud_cover_button)
        self.cloud_container.add_widget(self.cloud_button_container1)
        self.cloud_container.add_widget(self.cloud_button_container2)
        self.cloud_container.add_widget(self.cloud_button_container3)
        self.cloud_container.add_widget(self.cloud_button_container4)
        self.container.add_widget(self.cloud_container)

        self.container.add_widget(Label(text='Введіть дані про атмосферний тиск: ', font_size='18sp', color=(0,0,0,1)))
        self.container.add_widget(self.atmoshperic_pressure_input)
        self.container.add_widget(Label(text='Введіть дані про пору року: ', font_size='18sp', color=(0,0,0,1)))


        self.season_button_container1.add_widget(Label(text='Зима', font_size='18sp', color=(0,0,0,1)))
        self.season_button_container1.add_widget(self.season_button)
        self.season_button_container2.add_widget(Label(text='Весна', font_size='18sp', color=(0,0,0,1)))
        self.season_button_container2.add_widget(self.season_button)
        self.season_button_container3.add_widget(Label(text='Осінь', font_size='18sp', color=(0,0,0,1)))
        self.season_button_container3.add_widget(self.season_button)
        self.season_button_container4.add_widget(Label(text='Літо', font_size='18sp', color=(0,0,0,1)))
        self.season_button_container4.add_widget(self.season_button)
        self.season_container.add_widget(self.season_button_container1)
        self.season_container.add_widget(self.season_button_container2)
        self.season_container.add_widget(self.season_button_container3)
        self.season_container.add_widget(self.season_button_container4)
        self.container.add_widget(self.season_container)

        self.container.add_widget(Label(text='Введіть дані про тип рельєфу: ', font_size='18sp', color=(0,0,0,1)))
        self.location_button_container1.add_widget(Label(text='Рівнинний', font_size='18sp', color=(0,0,0,1)))
        self.location_button_container1.add_widget(self.location_button)
        self.location_button_container2.add_widget(Label(text='Гірський', font_size='18sp', color=(0,0,0,1)))
        self.location_button_container2.add_widget(self.location_button)
        self.location_button_container3.add_widget(Label(text='Прибережний', font_size='18sp', color=(0,0,0,1)))
        self.location_button_container3.add_widget(self.location_button)
        self.location_container.add_widget(self.location_button_container1)
        self.location_container.add_widget(self.location_button_container2)
        self.location_container.add_widget(self.location_button_container3)
        self.container.add_widget(self.location_container)

        self.container.add_widget(self.commit_button)
        