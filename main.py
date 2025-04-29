from random import *
recipes = {
'Spaghetti Carbonara': {
'Cuisine': 'Italian',
'Ingredients': ['Pasta', 'Eggs', 'Cheese', 'Bacon'],
'Prep Time': 20,
'Difficulty': 'Medium',
'Rating': 4.5
},
'Chicken Tikka Masala': {
'Cuisine': 'Indian',
'Ingredients': ['Chicken', 'Yogurt', 'Spices', 'Tomato Sauce'],
'Prep Time': 45,
'Difficulty': 'Hard',
'Rating': 4.8
},
'Avocado Toast': {
'Cuisine': 'American',
'Ingredients': ['Bread', 'Avocado', 'Salt', 'Pepper'],
'Prep Time': 5,
'Difficulty': 'Easy',
'Rating': 3.7
}
}
def fillRec(name,cuisine=None,ingredients=None,prepTime=None,diff=None,rating=None):
    if recipes.get(name,None) is not None:
        return -1
    recipes[name]['Cuisine'] = cuisine.lower()
    recipes[name]['Ingredients']=[i.lower() for i in ingredients]
    recipes[name]['Difficulty']=diff
    recipes[name]['Prep Time'] = prepTime
    recipes[name]['Rating']= rating
##########################################################
def getIngred(name:str):
    out =[]
    while 1:
        x = input("Enter ingredients(leave empty to exit): ")
        if(x==''):
            break
        out.append(x)
    return out
##########################################################
def printRecipe(name:str):
    print("Recipe: ",name)
    for k,v in recipes[name].items():
        if k == 'Prep Time':
            print(k,': ',v,' minutes')
            continue
        print(k,': ',v)
##########################################################
def recom(cuisine: str):
    recList = []
    for k,v in recipes.items():
        if v['Cuisine'] == cuisine.lower():
            recList.append(v['Cuisine'])
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
                randomRecommendation = i
            j+=1
        print("No recipes found in this cuisine, try this recipe instead!")
        printRecipe(randomRecommendation)
#############################################################
def findRecipe(name):
    found = []
    for k,v in recipes.items():
        if name in k.split():
            found.append(k)
    if len(found)<1:
        print("No recipes with that name were found")
    else:
        for i in found:
            printRecipe(i)
            print()
#############################################################
def filter(diff=None,prepTime=None,rating=None):
    results = []
    for k,v in recipes.items():
        if((v['Difficulty']== diff or diff is None)and(v['Prep Time']<prepTime or prepTime is None)and (rating>v['rating']or rating is None)):
           results.append(k)
    return results
##############################################################

