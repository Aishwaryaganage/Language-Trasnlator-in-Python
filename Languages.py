# pip install googletrans==4.0.0-rc1
from googletrans import Translator
translator = Translator()
language = {
    "bn":"Bangla",
    "en":"English",
    "ko":"Koren",
    "fr":"French",
    "de":"German",
    "he":"Hebrew",
    "hi":"Hindi",
    "it":"Italian",
    "ja":"Japanese",
    "la":"Latin",
    "ms":"Malay",
    "ne":"Nepali",
    "ru":"Russian",
    "ar":"Arabic",
    "zh":"Chinese",
    "es":"Spanish"
}
allow = True
while allow:
    user_code = input("Enter an language code to print list of languages and enter'options'\n")
    if user_code =="options":
        print("code:language")
        for item in language.items():
            print(f"{item[0]}=>{item[1]}")
        print()
    else:
        for lan_code in language.keys():
            if lan_code == user_code:
                print(f"You have selected {language[lan_code]}")
                allow= False
        if allow:
            print(" Not a valid language code")

while True: #Translation
    string  = input("Enter a text:  \nTo exit 'close':  \n select the language: \n")
    if string == 'close':
        print('\nHave a nice day')
        break

    translated = translator.translate(string, dest=user_code)
    print(f"\n{language[user_code]} translation:{translated.text} ")
    print(f'Pronunciation : {translated.pronunciation}')

    for item in language.items():
        # checking if source language is listed in language dictionary
        if translated.src == item[0]:
            print(f'Translated from : {item[1]}')
