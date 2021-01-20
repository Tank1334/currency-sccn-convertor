import requests as reqst
import json as jsn



def api(currency):

    response = reqst.get("http://api.shaycryptoco.in/price/trx")#requesting api
    json = response.json() #api-json

    json = json[currency] #requesting currency

    text = f"The value of sccn to {currency} is {json}" 

    return text

print(api('trx'))