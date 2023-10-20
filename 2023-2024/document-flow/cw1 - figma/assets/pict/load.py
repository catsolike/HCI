import re
import requests
from bs4 import BeautifulSoup
import cloudscraper
# __cf_bm:"XpUwCCQac641fwsufnDDWQULjCuyW1lvIVcdhmL5Ecc-1695179729-0-AdiDNWQIBoQCcT2UbgWQheLSFfcvTl67c2u+A0zdhF/crK/gyBz2AICTzH1iqVGagBqzeJm+R82tirhIS70S26o="
site = 'https://store.epicgames.com/ru/'

headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}

cookies2 = {"__cf_bm":"_WNFNSa769rbzHrpozkruBZyG3ZjUb1vN.7yPCEZqaM-1695180661-0-AVJ54oobGw63NeH6LIWF+v4VdERVITCQpw7XXUbAHbg9iJzvwjwnld9+VhwgEHV9z15/B4RkchusaxP9BEyJTn0=",
           "cf_clearance":"Bhe36twwfQUbOrGlq_F3CxTWCCHDYEDtjKqmRFnhzwQ-1695178710-0-1-91d45798.e54b002a.6507e8fb-0.2.1695178710",
           "_epicSID": "665c266c805f43368ec33ad25676b47f",
           "EPIC_DEVICE": "f22f22ffdec6439a9f8d1ba9adc6a888",
           "EPIC_LOCALE_COOKIE":"ru",
           "EPIC_SESSION_AP": "W_6DU8F5_useV9GXIBCdbA.u-8-azUJ2lrcjSz6oiDtf6DZfCQGJhEn8VKHO8wMU0i8vuuOuBioa7AxLKKlHyhe_pv5titHVpj3A_a_65fM6Ys1Ry4McSoMvpzLJm7Ym0aWg-I9mXRtcVkXMQslBOlqqww0Y18XOYqUVZyigrERA94KRY09GYvG8gTA26VGtdWjWpwWWfezk7DlxgUdxfrQWAhJPpyA3vY7ZgehVWw3nuy9mLtOOp6X03NcUGo3yogKHTRLBeoXzFT2_t4ggOIIRSR_IklTl80y4vw5ZCE2roXldbY5aOaZmhsIzvfADmLhbrfRMeiOsXHiBpmdaus_ec3T8-iKoaGLSRLde93b25hyBgNqJUPLngdM1eXnSObavSdWkHPskPbFm7KDDteQ8joKPZZ402padBmtIR75-wXjdENV_wHyyN53yZs1AlCftQsniI0M-WrbV9spuoAAmPzwQatyNKbeWQS7F0ITHaMVc98SBYMZsiXczuOFHiM.1694009738088.86400000.0RM1Qozh74Rd4J2RhyQvuw",
           "EPIC_SESSION_REPUTATION":"8h1rhTxqNxbfOkRH0jPx8Q.HcnFEhAvfsssyioohcZxUmCfc1BKXHvh0N4NMAN-ngaZdr_qEoOrEajy6Ujjq66WgG6JW5eNHtVRO6c56bOSQGMUDh2NWRA-PHkbmMuWO4-WU0Qqid964nyOwNp536CwzW9AOm4b_5WXAHQaDb9CB4BS3imiXuvGuvu_L4mxxtb7yyb4We2f_5FPHkevoVuFGJQXmHMKT8YOVJNYE7nLxlocbyvRaaSTxhaCjj3s-Z0CAPLm3OLN1LkRx-srJTl5HAxnnL0iF162xLCakOIj9di46CcbPkzTQVhgAhduQFz__bn2M3_JIihYhdYwQJQ1RldVgUc0S_eycdcpg5BJPQknAWa0t-w8-dwBnKbOmxXwsATkhA3poALyFhRw7LdL4LKtVhkrITTjwrfY8l3TxQ.1694009737882.86400000.9XElmN-6YKbfo1AsJFsOaQ",
           "HasAcceptedAgeGates":"Russia%3A9007199254740991"}

r = requests.get(site, headers=headers,cookies=cookies2)
print(r.text)

# soup = BeautifulSoup(response.text, 'html.parser')
# img_tags = soup.find_all('img')

# urls = [img['src'] for img in img_tags]


# for url in urls:
#     filename = re.search(r'/([\w_-]+[.](jpg|gif|png|avif))$', url)
#     if not filename:
#          print("Regex didn't match with the url: {}".format(url))
#          continue
#     with open(filename.group(1), 'wb') as f:
#         if 'http' not in url:
#             # sometimes an image source can be relative 
#             # if it is provide the base url which also happens 
#             # to be the site variable atm. 
#             url = '{}{}'.format(site, url)
#         response = requests.get(url)
#         f.write(response.content)