import requests
import json

#uses https://developer.oxforddictionaries.com/faq and get an API App ID and Key
app_id = "your Application ID"
app_key = "your Application Key"
language = "en-gb"
base_url ="https://od-api.oxforddictionaries.com/api/v2" 


def get_definition(target_word):
    end_point = "entries"
    url = f"{base_url}/{end_point}/{language}/{target_word.lower()}?fields=definitions"

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    try: 
        main_dict = json.loads(r.text)
        results = main_dict['results']
        lexical = results[0]['lexicalEntries']
        entries = lexical[0]['entries']
        senses = entries[0]['senses']
        definitions = senses[0]['definitions']
        definition = definitions[0]
        return definition
    except Exception:
        #not bothering for checking for status 200, or no result, just return
        #nothing. 
        return ""
    
