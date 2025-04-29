from random import *
recipes = {}
def fillRec(name: str,cuisine: str,ingredients: list,perpTime: int,diff:int,rating:float):
    if recipes.get(name,0) is not 0:
        return -1
    recipes[name]['cuisine'] = cuisine
    recipes[name]['ingredients']=ingredients
    recipes[name]['difficulty']=diff
    recipes[name][perpTime] = perpTime
    recipes[name][rating]= rating
def getIngred(name):
    out =[]
    while 1:
        x = input("Enter ingredients(leave empty to exit): ")
        if(x==''):
            break
        out.append(x)
    return out
def recom(cuisine: str):
    recList = []
    for k,v in recipes.items():
        if v['cuisine'] == cuisine.lower():
            recList.append(v['cuisine'])
    if len(recList)>0:
        print("based on your love of ")
