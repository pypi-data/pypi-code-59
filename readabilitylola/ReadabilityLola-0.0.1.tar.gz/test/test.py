import bahasa 
with open("bahasa.txt", "rb") as f:
        text = f.read()
bahasa_string = str(text,'utf-8', 'ignore').lower()

bahasa.Bahasa(bahasa_string).spike()

import hindi
with open("hindi.txt", "rb") as f:
        text = f.read()
hindi_string = str(text,'utf-8', 'ignore').lower()
hindi.Hindi(hindi_string).score()