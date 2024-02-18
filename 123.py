from deta import Deta

#deta = Deta("c07jfupdsmg_p62nqhnHwentnUYMZRxqXC4fxCzNEKyG")#MG
deta = Deta("c0hqbepjrcp_YWerRut2VNYfRixXNojXJ3Hy3kN3SxnK")#TG bot


db = deta.Base("maths")
db_content = db.fetch().items
print(len(db_content))


#db.put({"Atentiom":'хух'})
#db.put({"key":'0'})
#db.put({'Country':'e','sms':'[eq'})
#db.put({'Graph1':'url','Graph2':'url','Graph3':'url','Graph4':'url','Atention':'ll','Count':2})
#db.put({'teh':'Japan','eco':'Kitay'})
#db.put({'key':'2','id':'123','nikc':'lol',"name":'Леша'})
db.put({'key':'1','lore':'None'})
#db.put({'key': 'ID Country_Name ', "money": 1200, "roket": 2, "shit": ['123','321'], "up": ['543','345'],'sunks_for_who': 'Mexica', 'reserch': 0})
#Cколько денег у россии
#item=db.get('Russia')
#print(item['money'])

#Вся база
print(db_content)