#Nested Dictioanry

dx={
    'name':"Heena",
    'fav_game':"football",
    'subject':"Python"}

d1={
    'name':"Nitya",
    'fav_games':['Football','Cricket','Hocky'],
    'subjects':{'math':90,'sci':87,'phy':83}}


for k,v in dx.items():
    print(f'{k} = {v}')

#access list as element from dict
print(d1['fav_games'][1])

# access dictionarty element from another dictionary
print(d1['subjects']['sci'])



