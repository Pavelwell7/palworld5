import os
import random
import file_operations
from file_operations import VERSION
from faker import Faker

def main():

 fake = Faker("ru_RU")

 os.makedirs ( "python_dragons" , exist_ok=True)

 skills = ["Стремительный прыжок", "Электрический выстрел", "Огненный заряд"]
 random_skills = random.sample(skills, 3)

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
 for i, skill in enumerate(random_skills, 1):
    for old, new in replacements.items():
        skill = skill.replace(old,new)  
    context[f"skill_{i}"] = skill

 for j in range(1,11):
    file_name = f"python_dragons/result_{j}.svg"
   
    file_operations.render_template("charsheet.svg", file_name, context)
   
if __name__ == '__main__':
    main()
