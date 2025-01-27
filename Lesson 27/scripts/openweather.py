import requests

res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params = {"q": "Magnitogorsk",
                                  "APPID": "c8574326b301c23318bc5f4ec9fc9dec",
                                  "mode": "json", "units": "metric"
                                 }
    )
try:
    res.raise_for_status()
    data = res.json()
    print("Температура", data["main"]["temp"])
    #Попробуйте самостоятельно достать данные
except Exception as exc:
    print(exc)

