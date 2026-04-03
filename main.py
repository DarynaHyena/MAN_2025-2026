''' Імпортування бібліотек'''

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.button        import Button
from kivy.uix.label         import Label
from kivy.uix.textinput     import TextInput
from kivy.metrics           import dp
from kivy.utils             import get_color_from_hex as hex

from weather_model import train_model

'''Кінець блоку імпортування бібліотек'''

knn_model = train_model()


weather_result_map = {
  0: "rainy",
  1: "cloudy",
  2: "sunny",
  3: "snowy"
}



class Questionnaire(Screen):
  def __init__(self, **kw): 
    super().__init__(**kw)
    # поточний етап (1-2)
    self.stage = 1

    # загальні віджети
    self.anchor = AnchorLayout()
    self.container = BoxLayout(orientation='vertical', spacing=dp(1), padding=dp(1))
    self.button_container = BoxLayout(orientation='horizontal', spacing=dp(1), padding=dp(1))

    # поля вводу
    self.temperature_input = TextInput(hint_text='Температура', size_hint_y=None, height=dp(30))
    self.humidity_input = TextInput(hint_text='Вологість',   size_hint_y=None, height=dp(30))
    self.wind_speed_input = TextInput(hint_text='Швидкість руху повітря', size_hint_y=None, height=dp(30))
    self.precipitation_input = TextInput(hint_text='Кількість опадів', size_hint_y=None, height=dp(30))
    self.cloud_cover_input = TextInput(hint_text='Хмарність', size_hint_y=None, height=dp(30))
    self.atmoshperic_pressure_input = TextInput(hint_text='Атмосферний тиск', size_hint_y=None, height=dp(30))
    self.season_input = TextInput(hint_text='Пора року', size_hint_y=None, height=dp(30))
    self.location_input = TextInput(hint_text='Тип поверхні', size_hint_y=None, height=dp(30))

    # кнопки
    self.commit_button = Button(text='Підтвердити дані', size_hint_y=None, height=dp(30))
    self.reset_button = Button(text='Очистити дані', size_hint_y=None, height=dp(30))

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
      self.container.add_widget(Label(text='Введіть дані про температуру: ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.temperature_input)
      self.container.add_widget(Label(text='Введіть дані про вологість: ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.humidity_input)
      self.container.add_widget(Label(text='Введіть дані про швидкість руху повітря (м/с): ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.wind_speed_input)
      self.container.add_widget(Label(text='Введіть дані про кількість опадів в рік: ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.precipitation_input)
      self.container.add_widget(Label(text='Введіть дані про хмарність: (похмуро, мілива хмарність, безхмарно, хмарно)', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.cloud_cover_input)
      self.container.add_widget(Label(text='Введіть дані про атмосферний тиск: ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.atmoshperic_pressure_input)
      self.container.add_widget(Label(text='Введіть дані про пору року: ', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.season_input)
      self.container.add_widget(Label(text='Введіть дані про тип поверхні: (рівнинний, гірський, прибережний)', font_size='15sp', color=(0,0,0,1)))
      self.container.add_widget(self.location_input)
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
    clouds = self.cloud_cover_input.text.strip()
    pressure = self.atmoshperic_pressure_input.text.strip()
    season = self.season_input.text.strip()
    location = self.location_input.text.strip()

    clouds_input = clouds.lower()
    seasons_input = season.lower()
    locations_input = location.lower()

     # Перевірка на наявність даних
    if not temperature:
      self.temperature_input.hint_text_color = hex('#ff0008')
      self.temperature_input.hint_text = "Будь ласка, введіть температуру"
      return False
    if not humidity:
      self.humidity_input.hint_text_color = hex('#ff0008')
      self.humidity_input.hint_text = "Будь ласка, введіть вологість"
      return False
    if not wind:
      self.wind_speed_input.hint_text_color = hex('#ff0008')
      self.wind_speed_input.hint_text = "Будь ласка, введіть швидкість руху вітру"
      return False
    if not precipitation:
      self.precipitation_input.hint_text_color = hex('#ff0008')
      self.precipitation_input.hint_text = "Будь ласка, введіть кількість опадів"
      return False
    if not clouds:
      self.cloud_cover_input.hint_text_color = hex('#ff0008')
      self.cloud_cover_input.hint_text = "Будь ласка, введіть дані про хмарність"
      return False
    if not pressure:
      self.atmoshperic_pressure_input.hint_text_color = hex('#ff0008')
      self.atmoshperic_pressure_input.hint_text = "Будь ласка, введіть тиск"
      return False
    if not season:
      self.season_input.hint_text_color = hex('#ff0008')
      self.season_input.hint_text = "Будь ласка, введіть пору року"
      return False
    if not location:
      self.location_input.hint_text_color = hex('#ff0008')
      self.location_input.hint_text = "Будь ласка, введіть тип поверхні"
      return False

    # Перевірка чи дані записані правильно
    try:
      float(temperature)
    except ValueError:
      self.temperature_input.text = ''
      self.temperature_input.hint_text_color = hex('#ff0008')
      self.temperature_input.hint_text = "Температура повинна бути числом"
      return False
    
    try:
      float(humidity)
    except ValueError:
      self.humidity_input.text = ''
      self.humidity_input.hint_text_color = hex('#ff0008')
      self.humidity_input.hint_text = "Вологість повинна бути числом"
      return False
    
    try:
      float(wind)
    except ValueError:
      self.wind_speed_input.text = ''
      self.wind_speed_input.hint_text_color = hex('#ff0008')
      self.wind_speed_input.hint_text = "Швидкість повітря повинна бути числом"
      return False
    
    try:
      float(precipitation)
    except ValueError:
      self.precipitation_input.text = ''
      self.precipitation_input.hint_text_color = hex('#ff0008')
      self.precipitation_input.hint_text = "Кількість опадів повинна бути числом"
      return False
    
    try:
      float(pressure)
    except ValueError:
      self.atmoshperic_pressure_input.text = ''
      self.atmoshperic_pressure_input.hint_text_color = hex('#ff0008')
      self.atmoshperic_pressure_input.hint_text = "Атмосферний тиск повинен бути числом"
      return False
    
    # Перевірка для текстових полів вводу
    try:
      float(clouds)
      self.cloud_cover_input.text = ''
      self.cloud_cover_input.hint_text_color = hex('#ff0008')
      self.cloud_cover_input.hint_text = "Хмарність повинна бути словом"
      return False
    except ValueError:
      pass
      
    try:
      float(season)
      self.season_input.text = ''
      self.season_input.hint_text_color = hex('#ff0008')
      self.season_input.hint_text = "Пора року повинна бути словом"
      return False
    except ValueError:
      pass
      
    try:
      float(location)
      self.location_input.text = ''
      self.location_input.hint_text_color = hex('#ff0008')
      self.location_input.hint_text = "Тип поверхні повинен бути словом"
      return False
    except ValueError:
      pass

    # Перевірка правильлності в текстових полях вводу
    
    if clouds_input not in ["похмуро", "мілива хмарність", "безхмарно", "хмарно"]:
      self.cloud_cover_input.text = ''
      self.cloud_cover_input.hint_text_color = hex('#ff0008')
      self.cloud_cover_input.hint_text = "Перевірте правильність написання відповіді"
      return False
    if seasons_input not in ["зима", "осінь", "весна", "літо"]:
      self.season_input.text = ''
      self.season_input.hint_text_color = hex('#ff0008')
      self.season_input.hint_text = "Перевірте правильність написання відповіді"
      return False
    if locations_input not in ["рівнинний", "гірський", "прибережний"]:
      self.location_input.text = ''
      self.location_input.hint_text_color = hex('#ff0008')
      self.location_input.hint_text = "Перевірте правильність написання відповіді"
      return False
    

    return [[temperature, humidity, wind, precipitation, clouds, pressure, season, location]]


    
  def commit(self, inst):
    # Йдемо на наступний етап
    if self.stage < 2:
      data = self.input_check()
      if data is not None:
        prediction = knn_model.predict(data)
        result = weather_result_map.get(prediction[0], "невідомо")
        print(result)



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

    self.cloud_cover_input.text = ''
    self.cloud_cover_input.hint_text_color = hex('#000000')
    self.cloud_cover_input.hint_text = "Хмарність"

    self.atmoshperic_pressure_input.text = ''
    self.atmoshperic_pressure_input.hint_text_color = hex('#000000')
    self.atmoshperic_pressure_input.hint_text = "Атмосферний тиск"

    self.season_input.text = ''
    self.season_input.hint_text_color = hex('#000000')
    self.season_input.hint_text = "Пора року"

    self.location_input.text = ''
    self.location_input.hint_text_color = hex('#000000')
    self.location_input.hint_text = "Тип поверхні"