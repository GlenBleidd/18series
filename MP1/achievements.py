import json
import requests

url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"

params = dict(
	appid = '292030',
	key = 'D18401BF1463803306AA025A3E417F41',
	steamid = '76561198094977602'
)

resp = requests.get(url=url, params=params)
data = resp.json()


def disp():
	print ('The Witcher 3 Achievements')
	for item in range(0, len(data['playerstats']['achievements'])):
		name = data['playerstats']['achievements'][item]['name'] 
		status = data['playerstats']['achievements'][item]['achieved']
		if status == 1:
			current = 'Achieved'
		elif status == 0:
			current = 'Unachieved'
		print('Name: ' + name +'\tStatus: ' + current)

disp()

