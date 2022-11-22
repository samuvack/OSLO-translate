from deep_translator import GoogleTranslator

import json
  
# Opening JSON file
f = open('infrastructuur-voc_es.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)


for i in range(len(data['classes'])):
    filter = data['classes']

    try:
        naam_nl = filter[i]['label']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['label']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['definition']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['definition']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['usage']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['usage']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

for i in range(len(data['properties'])):
    filter = data['properties']

    try:
        naam_nl = filter[i]['label']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['label']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['definition']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['definition']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['usage']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['usage']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

for i in range(len(data['externalproperties'])):
    filter = data['externalproperties']

    try:
        naam_nl = filter[i]['label']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['label']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['definition']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['definition']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['usage']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['usage']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

for i in range(len(data['externals'])):
    filter = data['externals']

    try:
        naam_nl = filter[i]['label']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['label']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['definition']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['definition']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')

    try:
        naam_nl = filter[i]['usage']['nl']
        print(naam_nl)
        translated = GoogleTranslator(source='nl', target='es').translate(naam_nl)
        filter[i]['usage']['es'] = translated
        print(translated)
    except:
        print('doesnt exist')



with open("infrastructuur-voc_es_translated.json", "w") as outfile:
    json.dump(data, outfile)
  
# Closing file
f.close()


