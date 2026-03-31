''' Імпортування бібліотек'''

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.button        import Button
from kivy.uix.label         import Label
from kivy.uix.textinput     import TextInput
from kivy.uix.checkbox      import CheckBox
from kivy.metrics           import dp
from kivy.utils             import get_color_from_hex as hex

'''Кінець блоку імпортування бібліотек'''





class Questionnaire(Screen):
  def __init__(self, **kw): 
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

    self.button_container = BoxLayout(orientation='horizontal', spacing=dp(10), padding=dp(10))
    

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
    self.commit_button = Button(text='Підтвердити дані', size_hint_y=None, height=dp(48))
    self.reset_button = Button(text='Очистити дані', size_hint_y=None, height=dp(48))

    # підключаємо обробники
    self.commit_button.bind(on_press=self.commit)
    self.reset_button.bind(on_press=self.input_reset)

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

      self.button_container.add_widget(self.commit_button)
      self.button_container.add_widget(self.reset_button)
      self.container.add_widget(self.button_container)

    elif self.stage == 2:
      # Етап 2: Вивід результатів 
      self.container.add_widget(Label(text='Результат: ', font_size='18sp', color=(0,0,0,1)))
      self.container.add_widget(Label(text=' ', font_size='18sp', color=(0,0,0,1)))

  def input_check(self): # Перевірка для полів вводу
    # Створення змінних для перевірки
    temperature = self.temperature_input.text.strip()
    humidity = self.humidity_input.text.strip()
    wind = self.wind_speed_input.text.strip()
    precipitation = self.precipitation_input.text.strip()
    pressure = self.atmoshperic_pressure_input.text.strip()
            
    if not temperature and not humidity and not wind and not precipitation and not pressure: # Перевірка на наявність даних
      if not temperature:
        self.temperature_input.hint_text_color = hex('#ff0008')
        self.temperature_input.hint_text = "Будь ласка, введіть температуру"
      if not humidity:
        self.humidity_input.hint_text_color = hex('#ff0008')
        self.humidity_input.hint_text = "Будь ласка, введіть вологість"
      if not wind:
        self.wind_speed_input.hint_text_color = hex('#ff0008')
        self.wind_speed_input.hint_text = "Будь ласка, введіть швидкість руху вітру"
      if not precipitation:
        self.precipitation_input.hint_text_color = hex('#ff0008')
        self.precipitation_input.hint_text = "Будь ласка, введіть кількість опадів"
      if not pressure:
        self.atmoshperic_pressure_input.hint_text_color = hex('#ff0008')
        self.atmoshperic_pressure_input.hint_text = "Будь ласка, введіть тиск"
      return False



    # Перевірка чи дані записані правильно
    try:
      int(temperature)
    except ValueError:
      self.temperature_input.text = ''
      self.temperature_input.hint_text_color = hex('#ff0008')
      self.temperature_input.hint_text = "Температура повинна бути числом"
      return False
    
    try:
      int(humidity)
    except ValueError:
      self.humidity_input.text = ''
      self.humidity_input.hint_text_color = hex('#ff0008')
      self.humidity_input.hint_text = "Вологість повинна бути числом"
      return False
    
    try:
      int(wind)
    except ValueError:
      self.wind_speed_input.text = ''
      self.wind_speed_input.hint_text_color = hex('#ff0008')
      self.wind_speed_input.hint_text = "Швидкість повітря повинна бути числом"
      return False
    
    try:
      int(precipitation)
    except ValueError:
      self.precipitation_input.text = ''
      self.precipitation_input.hint_text_color = hex('#ff0008')
      self.precipitation_input.hint_text = "Кількість опадів повинна бути числом"
      return False
    
    try:
      int(pressure)
    except ValueError:
      self.atmoshperic_pressure_input.text = ''
      self.atmoshperic_pressure_input.hint_text_color = hex('#ff0008')
      self.atmoshperic_pressure_input.hint_text = "Атмосферний тиск повинен бути числом"
      return False
    
  def commit(self, inst):
    # Йдемо на наступний етап
    if self.stage < 2:
      if self.input_check():
        self.stage += 1
        self.build_stage()

  def input_reset(self):
    # Очищення даних
    self.temperature_input.text = ''
    self.temperature_input.hint_text_color = hex('#000000')
    self.temperature_input.hint_text = "Температура"

    self.humidity_input.text = ''
    self.humidity_input.hint_text_color = hex('#000000')
    self.humidity_input.hint_text = "Вологість"

    self.wind_speed_input.text = ''
    self.wind_speed_input.hint_text_color = hex('#000000')
    self.wind_speed_input.hint_text = "Швидкість руху вітру"

    self.precipitation_input.text = ''
    self.precipitation_input.hint_text_color = hex('#000000')
    self.precipitation_input.hint_text = "Кількість опадів"

    self.atmoshperic_pressure_input.text = ''
    self.atmoshperic_pressure_input.hint_text_color = hex('#000000')
    self.atmoshperic_pressure_input.hint_text = "Атмосферний тиск"