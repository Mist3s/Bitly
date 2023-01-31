import sys
import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {
        'Authorization': 'Bearer {}'.format(token)
        }

    request_body = {
        "long_url": url
        }

    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                             headers=headers, json=request_body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    headers = {
        'Authorization': 'Bearer {}'.format(token)
        }

    params = {
        'units': -1
        }

    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url),
                            headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {
        'Authorization': 'Bearer {}'.format(token)
        }

    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url),
                            headers=headers)
    return response.ok


def main():
    load_dotenv("token.env")
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", nargs='+', help="укажите ссылку")
    args = parser.parse_args(sys.argv[1:])
    for url in args.url:
        disassembled_url = urlparse(url)
        collected_url = f'{disassembled_url.netloc}{disassembled_url.path}'
        if not is_bitlink(token, collected_url):
            try:
                print('Битлинк: {}'.format(shorten_link(token, url)))
            except requests.exceptions.HTTPError as error_:
                print(error_)
            continue
        try:
            print('По вашей ссылке прошли: {} раз(а)'.format(count_clicks(token, collected_url)))
        except requests.exceptions.HTTPError as error_:
            print(error_)


if __name__ == "__main__":
    main()