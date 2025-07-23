from file_operations import VERSION
from faker import Faker
import random
import file_operations

fake = Faker("ru_RU")

skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар"]


random_skills = random.sample(skills, 3)

context = {
  "first_name": (fake.first_name()),
  "last_name": (fake.last_name()),
  "job": fake.job(), 
  "town": fake.city(),

  "strength": (random.randint(3, 18)),
  "agility": (random.randint(3, 18)),
  "endurance": (random.randint(3, 18)),
  "intelligence": (random.randint(3, 18)),
  "luck": (random.randint(3, 18)),

  "skill_1": random_skills[0],
  "skill_2": random_skills[1],
  "skill_3": random_skills[2]

}

replacements = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'й͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋'
    }

def replace_letters(context, replacements):
    for old, new in replacements.items():
      context = context.replace(old, new)
    return context

context["skill_1"] = replace_letters(context["skill_1"], replacements)
context["skill_2"] = replace_letters(context["skill_2"], replacements)
context["skill_3"] = replace_letters(context["skill_3"], replacements)   


file_operations.render_template("charsheet.svg", "result.svg", context)

