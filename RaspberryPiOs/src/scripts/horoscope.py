import datetime
import random
import math
from collections import defaultdict
from typing import List, Tuple, Dict
from colorama import Fore, Back, Style, init

init(autoreset=True)

class CelestialBody:
    def __init__(self, name: str, symbol: str, degrees: float):
        self.name = name
        self.symbol = symbol
        self.degrees = degrees

class ZodiacSign:
    def __init__(self, name: str, symbol: str, start_date: Tuple[int, int], end_date: Tuple[int, int], 
                 element: str, quality: str, ruling_planet: str):
        self.name = name
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.element = element
        self.quality = quality
        self.ruling_planet = ruling_planet

class AstrologicalChart:
    def __init__(self, zodiac_sign: ZodiacSign, ascendant: ZodiacSign, moon_sign: ZodiacSign):
        self.zodiac_sign = zodiac_sign
        self.ascendant = ascendant
        self.moon_sign = moon_sign
        self.planets = self._generate_planet_positions()

    def _generate_planet_positions(self) -> List[CelestialBody]:
        planets = [
            ("Солнце", "☉"), ("Луна", "☽"), ("Меркурий", "☿"), ("Венера", "♀"), ("Марс", "♂"),
            ("Юпитер", "♃"), ("Сатурн", "♄"), ("Уран", "♅"), ("Нептун", "♆"), ("Плутон", "♇")
        ]
        return [CelestialBody(name, symbol, random.uniform(0, 360)) for name, symbol in planets]

class HoroscopeGenerator:
    def __init__(self):
        self.zodiac_signs = self._initialize_zodiac_signs()
        self.aspects = ["Любовь", "Карьера", "Здоровье", "Финансы", "Личностный рост"]
        self.predictions = self._load_predictions()
        self.colors = {
            "Овен": "красный", "Телец": "зеленый", "Близнецы": "желтый", "Рак": "серебряный",
            "Лев": "золотой", "Дева": "коричневый", "Весы": "розовый", "Скорпион": "темно-красный",
            "Стрелец": "фиолетовый", "Козерог": "черный", "Водолей": "синий", "Рыбы": "бирюзовый"
        }

    def _initialize_zodiac_signs(self) -> List[ZodiacSign]:
        return [
            ZodiacSign("Овен", "♈", (3, 21), (4, 19), "Огонь", "Кардинальный", "Марс"),
            ZodiacSign("Телец", "♉", (4, 20), (5, 20), "Земля", "Фиксированный", "Венера"),
            ZodiacSign("Близнецы", "♊", (5, 21), (6, 20), "Воздух", "Мутабельный", "Меркурий"),
            ZodiacSign("Рак", "♋", (6, 21), (7, 22), "Вода", "Кардинальный", "Луна"),
            ZodiacSign("Лев", "♌", (7, 23), (8, 22), "Огонь", "Фиксированный", "Солнце"),
            ZodiacSign("Дева", "♍", (8, 23), (9, 22), "Земля", "Мутабельный", "Меркурий"),
            ZodiacSign("Весы", "♎", (9, 23), (10, 22), "Воздух", "Кардинальный", "Венера"),
            ZodiacSign("Скорпион", "♏", (10, 23), (11, 21), "Вода", "Фиксированный", "Плутон"),
            ZodiacSign("Стрелец", "♐", (11, 22), (12, 21), "Огонь", "Мутабельный", "Юпитер"),
            ZodiacSign("Козерог", "♑", (12, 22), (1, 19), "Земля", "Кардинальный", "Сатурн"),
            ZodiacSign("Водолей", "♒", (1, 20), (2, 18), "Воздух", "Фиксированный", "Уран"),
            ZodiacSign("Рыбы", "♓", (2, 19), (3, 20), "Вода", "Мутабельный", "Нептун")
        ]

    def _load_predictions(self) -> Dict[str, Dict[str, List[str]]]:
        predictions = defaultdict(lambda: defaultdict(list))
        for sign in self.zodiac_signs:
            for aspect in self.aspects:
                predictions[sign.name][aspect] = [
                    f"Влияние {sign.ruling_planet}а усилит ваши способности в сфере {aspect.lower()}а.",
                    f"Энергия {sign.element}а поможет вам преодолеть трудности в {aspect.lower()}е.",
                    f"Ваше {sign.quality.lower()} качество проявится наиболее ярко в {aspect.lower()}е.",
                    f"Сегодня {sign.name} может ожидать неожиданных поворотов в {aspect.lower()}е.",
                    f"Звезды советуют {sign.name} обратить особое внимание на {aspect.lower()}.",
                ]
        return predictions

    def get_zodiac_sign(self, birth_date: datetime.date) -> ZodiacSign:
        for sign in self.zodiac_signs:
            start = datetime.date(birth_date.year, *sign.start_date)
            end = datetime.date(birth_date.year, *sign.end_date)
            if start <= birth_date <= end:
                return sign
        return self.zodiac_signs[-1]

    def generate_astrological_chart(self, birth_date: datetime.date) -> AstrologicalChart:
        zodiac_sign = self.get_zodiac_sign(birth_date)
        ascendant = random.choice(self.zodiac_signs)
        moon_sign = random.choice(self.zodiac_signs)
        return AstrologicalChart(zodiac_sign, ascendant, moon_sign)

    def calculate_compatibility(self, sign1: ZodiacSign, sign2: ZodiacSign) -> float:
        base_compatibility = random.uniform(0.5, 1.0)
        element_bonus = 0.1 if sign1.element == sign2.element else 0
        quality_bonus = 0.1 if sign1.quality == sign2.quality else 0
        return min(base_compatibility + element_bonus + quality_bonus, 1.0)

    def generate_horoscope(self, birth_date: datetime.date, current_date: datetime.date) -> str:
        chart = self.generate_astrological_chart(birth_date)
        zodiac_sign = chart.zodiac_sign
        horoscope = f"{Fore.CYAN}{Style.BRIGHT}Гороскоп для {zodiac_sign.name} {zodiac_sign.symbol} на {current_date.strftime('%d.%m.%Y')}:\n\n"

        for aspect in self.aspects:
            prediction = random.choice(self.predictions[zodiac_sign.name][aspect])
            horoscope += f"{Fore.YELLOW}{aspect}{Style.RESET_ALL}: {prediction}\n\n"

        lucky_number = random.randint(1, 100)
        lucky_color = self.colors[zodiac_sign.name]

        horoscope += f"{Fore.GREEN}Счастливое число: {lucky_number}\n"
        horoscope += f"Счастливый цвет: {lucky_color}\n\n"

        horoscope += f"{Fore.MAGENTA}Астрологическая карта:\n"
        horoscope += f"Солнечный знак: {zodiac_sign.name} {zodiac_sign.symbol}\n"
        horoscope += f"Асцендент: {chart.ascendant.name} {chart.ascendant.symbol}\n"
        horoscope += f"Лунный знак: {chart.moon_sign.name} {chart.moon_sign.symbol}\n\n"

        horoscope += f"{Fore.BLUE}Положение планет:\n"
        for planet in chart.planets:
            sign = self.zodiac_signs[math.floor(planet.degrees / 30)]
            horoscope += f"{planet.name} {planet.symbol}: {sign.name} {sign.symbol} ({planet.degrees:.2f}°)\n"

        compatibility = self.calculate_compatibility(zodiac_sign, chart.moon_sign)
        horoscope += f"\n{Fore.RED}Совместимость с Лунным знаком: {compatibility:.2%}\n"

        horoscope += f"\n{Fore.WHITE}{Style.BRIGHT}Совет дня: {self.get_daily_advice(zodiac_sign)}\n"

        return horoscope

    def get_daily_advice(self, sign: ZodiacSign) -> str:
        advices = [
            f"Сегодня энергия {sign.element}а особенно сильна. Используйте это для достижения своих целей.",
            f"Ваше {sign.quality.lower()} качество поможет вам справиться с неожиданными ситуациями.",
            f"Прислушайтесь к влиянию {sign.ruling_planet}а и доверьтесь своей интуиции.",
            "Сегодня хороший день для медитации и самопознания.",
            "Будьте открыты новым возможностям, они могут прийти с неожиданной стороны."
        ]
        return random.choice(advices)

class HoroscopeApp:
    def __init__(self):
        self.generator = HoroscopeGenerator()

    def run(self):
        print(f"{Fore.CYAN}{Style.BRIGHT}Добро пожаловать в продвинутый генератор гороскопов!{Style.RESET_ALL}")
        while True:
            try:
                birth_date_str = input(f"{Fore.GREEN}Введите вашу дату рождения (ДД.ММ.ГГГГ): {Style.RESET_ALL}")
                birth_date = datetime.datetime.strptime(birth_date_str, "%d.%m.%Y").date()
                current_date = datetime.date.today()
                
                horoscope = self.generator.generate_horoscope(birth_date, current_date)
                print("\n" + "=" * 50 + "\n")
                print(horoscope)
                print("=" * 50 + "\n")
                
                again = input(f"{Fore.YELLOW}Хотите сгенерировать еще один гороскоп? (да/нет): {Style.RESET_ALL}").lower()
                if again != 'да':
                    print(f"{Fore.MAGENTA}{Style.BRIGHT}Спасибо за использование продвинутого генератора гороскопов!{Style.RESET_ALL}")
                    break
            except ValueError:
                print(f"{Fore.RED}Ошибка: Пожалуйста, введите дату в формате ДД.ММ.ГГГГ{Style.RESET_ALL}")

if __name__ == "__main__":
    app = HoroscopeApp()
    app.run()
