from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    coin = input('\nCoin: ')
    print(f'💸 Picking {coin} value...\n')
    coin = coin.replace(" ", "-").replace('$', '')
    url = f'https://coinmarketcap.com/currencies/{coin}/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Value
    value = soup.select_one('.priceValue').text

    # Price Change 24h:
    twofour_html = soup.select_one('.sc-5fd6bdfe-0')
    twofour = twofour_html.text
    if twofour_html.next.attrs['class'][0] == 'icon-Caret-up':
        twofour = '+' + twofour
    else:
        twofour = '-' + twofour

    # Rank 
    rank = soup.find('div', {
        'class': 'namePill namePillPrimary'
    }).text

    # Market
    market_cap = soup.find('div', {'class': 'statsValue'}).text

    # Image
    image = soup.find('meta', {
        'name': 'twitter:image'
    }).attrs['content']

    print(coin.capitalize() + ' - ' + rank)
    print(f'Price: {value}')
    print(f'Price Change 24h: {twofour}')
    print(f'Market Cap: {market_cap}')
    print(f'Image: {image}\n')
