from random import *
recipes = {}
def fillRec(name: str,cuisine: str,ingredients: list,prepTime: int,diff:str,rating:float):
    if recipes.get(name,0) is not 0:
        return -1
    recipes[name]['cuisine'] = cuisine.lower()
    recipes[name]['ingredients']=[i.lower() for i in ingredients]
    recipes[name]['difficulty']=diff
    recipes[name]['prepTime'] = prepTime
    recipes[name]['rating']= rating
##########################################################
def getIngred(name):
    out =[]
    while 1:
        x = input("Enter ingredients(leave empty to exit): ")
        if(x==''):
            break
        out.append(x)
    return out
##########################################################
def printRecipe(name):
    print("recipe: ",name)
    for k,v in recipes[name].items():
        if k == 'prepTime':
            print(k,': ',v,' minutes')
            continue
        print(k,': ',v)
##########################################################
def recom(cuisine: str):
    recList = []
    for k,v in recipes.items():
        if v['cuisine'] == cuisine.lower():
            recList.append(v['cuisine'])
    if len(recList)>0:
        print("based on your love of %s cuisine, try these recipes: \n")
        for i in recList:
            printRecipe(i)
            print()
    else:
        x = randint(0,len(recipes)-1)
        j = 0
        for i in recipes.keys():
            if x == j:
                reco = i
            j+=1
        print("No recipes found in this cuisine, try this recipe instead!")
        printRecipe(reco)
#############################################################
def findRec():

#############################################################