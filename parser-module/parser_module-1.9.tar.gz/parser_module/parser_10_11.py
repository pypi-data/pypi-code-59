from parser_libraries import functions as f
import os
from bs4 import BeautifulSoup

URL = 'https://www.mid.ru/activity/shots/personnel/extraordinary_ambassador#main-content'


def parser():
    rel = 6
    html = f.get_html(URL)
    counter = 1
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')
        contents = soup.find('section', class_='block')
        contents = contents.find_all('tr')
        contents = contents[1:]
        people = []
        for content in contents:
            name = content.get_text().lower().replace('\n', ' ')
            while name.find('  ') != -1:
                name = name.replace('  ', ' ')
            work = name.find('ПОСТОЯННЫЙ ПРЕДСТАВИТЕЛЬ РОССИЙСКОЙ ФЕДЕРАЦИИ'.lower())
            if work == -1:
                work = 10
            else:
                work = 11
            try:
                date = name[name.find('.')-2:name.find('.')+8].replace('.', ' ')
                date = f.get_dig_date(date)
            except:
                date = f.get_dig_date('01 01 1901')
            name = name[1:name.find('.')-2]
            name = f.get_name(name)
            people.append({
                'image_link': '-',
                'first_name': name[1],
                'middle_name': name[2],
                'last_name': name[0],
                'link': URL,
                'bday': date['day'],
                'bmonth': date['month'],
                'byear': date['year'],
                'position_id': work
            })
        return people
    else:
        return [{'code': 2, 'script': os.path.basename(__file__)}]
