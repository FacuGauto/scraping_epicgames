import requests

response = requests.get('https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=es-MX&country=AR&allowCountries=AR')
games = response.json()['data']['Catalog']['searchStore']['elements']
promoitions_games = []
for game in games:
  if game['promotions'] is None:
    continue
  if not game['promotions']['promotionalOffers']:
    continue
  promotion = {}
  promotion['title'] = game['title']
  for promotionalOffer in game['promotions']['promotionalOffers'][0]['promotionalOffers']:
    promotion['startDate'] = promotionalOffer['startDate']
    promotion['endDate'] = promotionalOffer['endDate']
    promotion['discountPercentage'] = promotionalOffer['discountSetting']['discountPercentage']
    
    if promotion['discountPercentage'] == 0:
      promoitions_games.append(promotion)
      
for game in promoitions_games:
  date = game['endDate'].split('T')[0]
  print(f"{game['title']} gratis hasta {date}")
  