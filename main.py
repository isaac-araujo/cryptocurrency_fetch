from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    coin = input('Coin: ')
    print(f'💸 Picking {coin} value...')
    coin = coin.replace(" ", "-").replace('$', '')
    url2 = f'https://coinmarketcap.com/currencies/{coin}/'
    page = requests.get(url2)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Value
    value = soup.select_one('.priceValue ').text

    # Price Change 24h:
    twofourhtml = soup.select_one('.sc-5fd6bdfe-0')
    twofour = twofourhtml.text
    if twofourhtml.next.attrs['class'][0] == 'icon-Caret-up':
        twofour = '+ ' + twofour
    else:
        twofour = '- ' + twofour

    # Rank 
    rank = soup.find('div', {
        'class': 'namePill namePillPrimary'
    }).text

    # Market
    market = soup.find('div', {'class': 'statsValue'}).text

    # Image
    # image = soup.find('div', {'class': 'sc-16r8icm-0'}).find("img")
    # image.attrs['src']

    print(coin.capitalize() + ' - ' + rank)
    print(f'Price: {value}')
    print(f'Price Change 24h: {twofour}')
    print(f'Market Cap: {market}')
    # print(f'Image: {image.attrs["src"]}')
