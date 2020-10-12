import re
import bs4
import requests
import googletrans
import json
from googletrans import Translator
translator = Translator()
parsed_json = (json.loads(Lang))
print(parsed_json)
#googletrans.LANGUAGES = 
#result = translator.translate('Mikä on nimesi', dest='fi')
#, dest={dest}'
def text(input_text,language):

    result = translator.translate(input_text)
    return result.text

"""
    params = {"text": input_text}
    target_url = "https://translate.google.com/#view=home&op=translate&sl=en&tl=fr.php"

    target_url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(target_url, data=params)
    # the html returned is in poor form normally.
    soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    
    giz = soup.find_all(text=True)
    giz_text = giz[38].strip("\r\n")  # Hacky, but consistent.
"""
