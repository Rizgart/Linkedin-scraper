import sqlite3
from linkedin_scraper import Person, actions
from selenium import webdriver
import csv

driver = webdriver.Chrome("C:/Users/Nozad/Documents/selenium/Ny mapp/chromedriver.exe")
driver.implicitly_wait(8)

email = "didoj77152@yncyjs.com"
password = "#####"
actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal

profileUrl = []

check = 'https://www.linkedin.com/'

with open('profiler.csv', newline='', encoding="mbcs") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        res = [idx for idx in row if idx.lower().startswith(check.lower())]
        profileUrl.append(res)

conn = sqlite3.connect('profiler.db')
c = conn.cursor()

count = 1
while True:
    urls = ''.join(profileUrl[count])
    person = Person(urls, driver=driver, scrape=False)
    person.scrape(close_on_complete=False)
    count = count + 1

    name = ''.join(person.name)
    about = ' '.join(person.about)
    personUrl = ''.join(person.linkedin_url)
    personExperience = '; '.join(map(str, person.experiences))
    personSkills = '; '.join(person.skills)

    if person.job_title == "Utvecklare" or "Testare" or "Testautomatiserare" or "Software Tester" or "Automationsutvecklare" or "Automations developer":
        c.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?)',
                   (name, about, personUrl, personExperience, personSkills))
        conn.commit()

