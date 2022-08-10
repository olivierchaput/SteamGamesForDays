from lxml import html
import requests

url = 'https://store.steampowered.com/search/?maxprice=free&specials=1'
resp = requests.get(url)

# Error messages
if resp.status_code == 200 :
    print('\nSuccesfully reached Steam (' + str(resp.status_code) + ')')
else :
    print('\nThere was an error in the request')


tree = html.fromstring(resp.content)
elements = tree.xpath('//*[@id="search_resultsRows"]/a/div[2]/div[1]/span')


for element in elements:
    print('----------------------------------')
    print('Game title : ' + element.text)
    print('Game URL : ' + element.getparent().getparent().getparent().attrib['href'] + '\n\n')


