from file_operations import VERSION
from faker import Faker
import random
import file_operations

fake = Faker("ru_RU")

skills = ["Стремительный прыжок".replace("е", "е͠ "), "Электрический выстрел".replace("е", "е͠ "), "Ледяной удар".replace("е", "е͠ ")]


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



file_operations.render_template("charsheet.svg", "result.svg", context)

