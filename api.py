import urllib
import requests
from secret import APP_ID, APP_CODE

def reverse_geocode(lat, lon, location='address'):
    """Reverse geocode lat and lon coordiantes using the Geocoder API

    The following API is used
    https://developer.here.com/api-explorer/rest/geocoder/reverse-geocode

    :param float lat: latitude coordinate
    :param float lon: longitude coordinate
    :param str location: specify country, state, or address (default address)
    ;return: specified information about location
    :rtype: str
    """

    # Encode parameters
    coordinates = str(lat) + ',' + str(lon)
    params = urllib.parse.urlencode({'prox': coordinates,
                                     'mode': 'retrieveAddresses',
                                     'maxresults': 1,
                                     'gen': 9,
                                     'app_id': APP_ID,
                                     'app_code': APP_CODE,
                                     })
    # Contruct request URL
    # url = 'https://geo.fcc.gov/api/census/area?' + params
    url = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?' + params
    # Get response from API
    response = requests.get(url)
    # Parse json in response
    data = response.json()
    if location == 'country':
        return data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Country"]
    elif location == 'state':
        return data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["State"]
    return data["Response"]["View"][0]["Result"][0]["Location"]["Address"]['Label']

