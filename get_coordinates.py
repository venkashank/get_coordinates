import argparse
import requests

API_KEY = 'TYPE IN YOUR API KEY HERE'

def gmaplookup(location, api_key):
    """
    Builds the request URL by using the given location and API_KEY.
    Returns a json response from requests.
    """

    URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'
    return requests.get(URL).json()


def get_coords(response):
    """
    Extracts the latitude and longitude from the response.
    Returns a Dictionary with the Keys: Latitude and Longitude
    """

    latitude = response['results'][0]['geometry']['location']['lat']
    longitude = response['results'][0]['geometry']['location']['lng']
    coordinates = dict({
        'Latitude': latitude,
        'Longitude': longitude
    })
    return coordinates


if __name__ == '__main__':


    parser = argparse.ArgumentParser(
                        add_help=True,
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                        description="Script returns Latitude and Longitude of a location",
                        prefix_chars='-')

    parser.add_argument(
                        '-l', '--location',
                        help='Location that want coordinates for in quotation marks ""',
                        action='store',
                        dest='location',
                        default='New York City, New York',
                        required=True)

    args = parser.parse_args()
    
    print(get_coords(gmaplookup(args.location, API_KEY)))