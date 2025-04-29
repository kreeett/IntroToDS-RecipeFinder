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
    if recipes.get(name) is not None:
        return -1
    recipes[name] = {}
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
        if v['Cuisine'].lower() == cuisine.lower():
            recList.append(k)
    if len(recList)>0:
        print("based on your love of %s cuisine, try these recipes: \n"%cuisine)
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
        if name.lower() in k.lower().split():
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
        if((v['Difficulty'].lower()== diff.lower() or diff is None)and(v['Prep Time']<prepTime or prepTime is None)and (rating<v['Rating']or rating is None)):
           results.append(k)
    return results
##############################################################
while 1:
    try:
        choice = int(input('Welcome to the Recipe Finder!\nChoose an option:\n1. Get recipe recommendations\n2. Search for a recipe\n3. Filter recipes (by time/difficulty/rating)\n4. Add a new recipe\n5. Exit'))
    except:
        print("error Invalid choice")
        continue
    if choice ==1:
        cuisine = input("Enter your favorite cuisine: ")
        recom(cuisine)
    elif choice == 2:
        name = input("Enter the name of the recipe: ")
        findRecipe(name)
    elif choice == 3:
        diff = input("Enter the difficulty level (Easy, Medium, Hard): ").lower()
        prepTime = int(input("Enter the maximum preparation time in minutes: "))
        rating = float(input("Enter the minimum rating (0-5): "))
        results = filter(diff,prepTime,rating)
        if len(results)>0:
            print("Here are the recipes that match your criteria:")
            for i in results:
                printRecipe(i)
                print()
        else:
            print("No recipes found matching your criteria.")
    elif choice == 4:
        name = input("Enter the name of the recipe: ").lower()
        cuisine = input("Enter the cuisine: ").lower()
        ingredients = getIngred(name)
        prepTime = int(input("Enter the preparation time in minutes: "))
        diff = input("Enter the difficulty level (Easy, Medium, Hard): ").lower()
        rating = float(input("Enter the rating (0-5): "))
        fillRec(name,cuisine,ingredients,prepTime,diff,rating)
        print("Recipe added successfully!")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
