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
    },
    'Beef Tacos': {
        'Cuisine': 'Mexican',
        'Ingredients': ['Tortillas', 'Ground Beef', 'Lettuce', 'Cheese', 'Salsa'],
        'Prep Time': 25,
        'Difficulty': 'Medium',
        'Rating': 4.2
    },
    'Sushi Rolls': {
        'Cuisine': 'Japanese',
        'Ingredients': ['Rice', 'Nori', 'Fish', 'Vegetables'],
        'Prep Time': 60,
        'Difficulty': 'Hard',
        'Rating': 4.9
    },
    'French Onion Soup': {
        'Cuisine': 'French',
        'Ingredients': ['Onions', 'Beef Broth', 'Cheese', 'Bread'],
        'Prep Time': 50,
        'Difficulty': 'Medium',
        'Rating': 4.4
    },
    'Pad Thai': {
        'Cuisine': 'Thai',
        'Ingredients': ['Rice Noodles', 'Shrimp', 'Peanuts', 'Eggs', 'Bean Sprouts'],
        'Prep Time': 30,
        'Difficulty': 'Medium',
        'Rating': 4.6
    },
    'Falafel Wrap': {
        'Cuisine': 'Middle Eastern',
        'Ingredients': ['Falafel', 'Pita Bread', 'Hummus', 'Lettuce', 'Tomato'],
        'Prep Time': 35,
        'Difficulty': 'Medium',
        'Rating': 4.3
    },
    'Pancakes': {
        'Cuisine': 'American',
        'Ingredients': ['Flour', 'Eggs', 'Milk', 'Baking Powder', 'Sugar'],
        'Prep Time': 15,
        'Difficulty': 'Easy',
        'Rating': 4.0
    },
    'Greek Salad': {
        'Cuisine': 'Greek',
        'Ingredients': ['Tomatoes', 'Cucumber', 'Feta Cheese', 'Olives', 'Olive Oil'],
        'Prep Time': 10,
        'Difficulty': 'Easy',
        'Rating': 3.9
    }
}
def fillRec(name,label,cuisine=None,ingredients=None,prepTime=None,diff=None,rating=None):
    label.config(text="")
    if recipes.get(name) is not None:
        return -1
    recipes[name] = {}
    recipes[name]['Cuisine'] = cuisine.lower()
    recipes[name]['Ingredients']=[i.lower() for i in ingredients.split(',') if len(ingredients.split(','))>0]
    recipes[name]['Prep Time'] = prepTime
    recipes[name]['Difficulty']=diff
    recipes[name]['Rating']= rating
    label.config(text="Added")
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
def add_text(label,add):
    current = label["text"]
    new = current+'\n'+add
    label.config(text=new)
##########################################################
def printRecipe(name:str,label):
    add_text(label,f"Recipe: {name}")
    for k,v in recipes[name].items():
        if k == 'Prep Time':
            add_text(label,f"{k}: {v} minutes")
            continue
        add_text(label,f"{k}: {v}")
    add_text(label,"\n")
##########################################################
def recom(cuisine: str,label):
    recList = []
    label.config(text="")
    for k,v in recipes.items():
        if v['Cuisine'].lower() == cuisine.lower():
            recList.append(k)
    if len(recList)>0:
        add_text(label,"based on your love of %s cuisine, try these recipes: \n"%cuisine)
        for i in recList:
            printRecipe(i,label)
    else:
        x = randint(0,len(recipes)-1)
        j = 0
        for i in recipes.keys():
            if x == j:
                randomRecommendation = i
            j+=1
        add_text(label,"No recipes found in this cuisine, try this recipe instead!")
        printRecipe(randomRecommendation,label)
#############################################################
def findRecipe(name,label):
    found = []
    label.config(text="")
    for k,v in recipes.items():
        if name.lower() in k.lower().split():
            found.append(k)
    if len(found)<1:
        add_text(label,"No recipes with that name were found")
    else:
        for i in found:
            printRecipe(i,label)
#############################################################
def filter(label,diff=None,prepTime=None,rating=None):
    results = []
    label.config(text="")
    for k,v in recipes.items():
        if((v['Difficulty'].lower()== diff.lower() or diff is None)and(v['Prep Time']<prepTime or prepTime is None)and (rating<v['Rating']or rating is None)):
           results.append(k)
    if len(results)>0:
        add_text(label,"Here are the recipes that match your criteria:")
        for i in results:
            printRecipe(i,label)
    else:
        add_text(label,"No recipes found matching your criteria.")
##############################################################
import tkinter as tk
def show_frame(frame,label=None):
    if label is not None:
        label.config(text="")
    frame.tkraise()
################################################################
def printL(label,add):
    label.config(text=add)
##################################################################
def submit():
    selection = (choicebox.curselection())
    if selection:
        item = choicebox.get(selection[0])
        if item=="1.Get recipe recommendations":
            main.place_forget()
            show_frame(reco)
        elif item =="2.Search for a recipe":
            main.place_forget()
            show_frame(fnd)
        elif item == "3.Filter recipes(by time/difficulty/rating)":
            main.place_forget()
            show_frame(fltr)
        elif item=="4.Add a new recipe":
            main.place_forget()
            show_frame(add)
        else:
            root.destroy()
########################################################################
root = tk.Tk()
root.title("Recipe Picker")
root.geometry("400x800")
#######################
main = tk.Frame(root)
reco = tk.Frame(root)
fnd = tk.Frame(root)
fltr = tk.Frame(root)
add = tk.Frame(root)
for frame in (main,reco,fnd,fltr,add):
    frame.place(x=0,y=0,relwidth=1,relheight=1)
#######################
main.pack()
welcome = tk.Label(main,text="Welcome to saif's recipe picker!")
welcome.pack()
choose = tk.Label(main,text='Choose an option: ')
choose.pack()
choicebox = tk.Listbox(main,height=5,width=35)
choicebox.insert(tk.END,"1.Get recipe recommendations")
choicebox.insert(tk.END,"2.Search for a recipe")
choicebox.insert(tk.END,"3.Filter recipes(by time/difficulty/rating)")
choicebox.insert(tk.END,"4.Add a new recipe")
choicebox.insert(tk.END,"5.Exit")
choicebox.pack()
choicebox.bind("<<ListboxSelect>>", lambda event: submit())
sel = tk.Label(main,text="")
sel.pack()
canvas = tk.Canvas(main,width=400,height=400,bg='white')
canvas.pack()

########################
recoTitle = tk.Label(reco,text="Enter your favourite cuisine")
recoTitle.pack()
cuis = tk.Entry(reco)
cuis.pack()
recoOut = tk.Label(reco,text="")
recoOut.pack()
recoSubButton = tk.Button(reco,text="Submit",command = lambda: recom(cuis.get(),recoOut))
recoSubButton.pack()
recoBackButton = tk.Button(reco,text="Back to main menu",command=lambda: show_frame(main,recoOut))
recoBackButton.pack()

##################################
fndTitle = tk.Label(fnd,text="Enter the name of the recipe")
fndTitle.pack()
fndName = tk.Entry(fnd)
fndName.pack()
fndOut = tk.Label(fnd,text="")
fndOut.pack()
fndSubButton = tk.Button(fnd,text="Search",command=lambda: findRecipe(fndName.get(),fndOut))
fndSubButton.pack()
fndBackButton = tk.Button(fnd,text="Back to main menu",command=lambda: show_frame(main,fndOut))
fndBackButton.pack()

###################################
fltrTitle1 = tk.Label(fltr,text="Enter difficulty")
fltrTitle1.pack()
fltrDifficulty = tk.Listbox(fltr,height=3)
fltrDifficulty.insert(tk.END,"Easy")
fltrDifficulty.insert(tk.END,"Medium")
fltrDifficulty.insert(tk.END,"Hard")
fltrDifficulty.pack()
fltrTitle2 = tk.Label(fltr,text="Max prep time")
fltrTitle2.pack()
fltrPrepTime= tk.Scale(fltr,from_=1,to=120,orient='horizontal')
fltrPrepTime.pack()
fltrTitle3 = tk.Label(fltr,text="Min Rating")
fltrTitle3.pack()
fltrRating = tk.Scale(fltr,from_=1,to=5,orient='horizontal',tickinterval=0.1)
fltrRating.pack()
fltrOut = tk.Label(fltr,text="")
fltrOut.pack()
fltrSubButton = tk.Button(fltr,text="Search",command=lambda: filter(fltrOut,fltrDifficulty.get(fltrDifficulty.curselection()[0]),int(fltrPrepTime.get()),int(fltrRating.get())))
fltrSubButton.pack()
fltrBackButton = tk.Button(fltr,text="Back to main menu",command=lambda: show_frame(main,fltrOut))
fltrBackButton.pack()
###################################
addTitle1 = tk.Label(add,text="Enter the name of the recipe")
addTitle1.pack()
addName = tk.Entry(add)
addName.pack()
addTitle2 = tk.Label(add,text="Enter cuisine")
addTitle2.pack()
addCuisine = tk.Entry(add)
addCuisine.pack()
addTitle3 = tk.Label(add,text="Add a list of ingredients(seperated by commas)")
addTitle3.pack()
addIngredients = tk.Entry(add)
addIngredients.pack()
addTitle4 = tk.Label(add,text="Add difficulty")
addTitle4.pack()
addDifficulty = tk.Listbox(add,height=3)
addDifficulty.insert(tk.END,"Easy")
addDifficulty.insert(tk.END,"Medium")
addDifficulty.insert(tk.END,"Hard")
addDifficulty.pack()
addTitle5 = tk.Label(add,text="Add Prep time")
addTitle5.pack()
addPrepTime = tk.Scale(add,from_=5,to=120,orient='horizontal',resolution=5)
addPrepTime.pack()
addTitle6 = tk.Label(add,text="Add Rating")
addTitle6.pack()
addRating = tk.Scale(add,from_=1,to=5,orient='horizontal',resolution=0.1)
addRating.pack()
ingredientList = addIngredients.get().split(',')
addOut = tk.Label(add,text='')
addOut.pack()
addSubButton = tk.Button(add,text="Add",command=lambda: fillRec(addName.get(),addOut,addCuisine.get(),addIngredients.get(),addPrepTime.get(),addDifficulty.get(addDifficulty.curselection()[0]),addRating.get()))
addSubButton.pack()
addBackButton = tk.Button(add,text="Back to main menu",command=lambda: show_frame(main,fltrOut))
addBackButton.pack()
###################################
show_frame(main)
root.mainloop()
