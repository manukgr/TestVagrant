import requests
import testdata.urls
import testdata.credentials


def get_temperature(location: str) -> str:
    """
      :param location: Location to fetch weather
      :return:

    """
    req = requests.get(testdata.urls.open_weather_url, params={"q": location,
                                                               "appid": testdata.credentials.open_weather_key,
                                                               "units": "metric"})
    assert req.status_code == 200, "Seems like some issue with weather API"

    return str(req.json()['main']['temp'])


if __name__ == "__main__":
    print(get_temperature("Chandigarh"))
