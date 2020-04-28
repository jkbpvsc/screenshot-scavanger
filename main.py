import asyncio

import bases
import requests
import time
from pyppeteer import launch

base_url = "https://prnt.sc/"

async def start():
    ids = generate_ids()
    browser = await launch()
    page = await browser.newPage()

    for id in ids:
        try:
            src = await get_image_url(id, page)
            save_image(src, id)
        except:
            print("Failed saving: " + id)


async def get_image_url(id, page):
    await page.goto(base_url + id)

    image_src = await page.evaluate(''' () => {
        return document.getElementsByClassName('screenshot-image')[0].src
    } ''')

    return image_src


def generate_ids():
    start = bases.decode('s60q97', 32)
    end = start + 1000
    numbers = map(lambda n: bases.encode(n, 32), range(start, end))
    print(numbers)

    return numbers

def normalise_number_to_len(number, flen):
    number_string = str(number)
    length = len(number_string)
    dlen = flen - length

    return '0' * dlen + number_string

def save_image(url, id):
    with open('images/' + id + '.png', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    print('Successfully saved image ' + id + '.png, url: ' + url)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start())
