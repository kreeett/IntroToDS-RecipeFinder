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
def fillRec(name,label,cuisine=None,ingredients=None,prepTime=None,diff=None,rating=None):#Function to add an item to the data
    label.config(text="")#clear previous outputs from the gui
    if recipes.get(name.lower().title()) is not None:#use the .get function to test if the added item already exists or not
        label.config(text="already exists")#change the existing label
        return -1
    recipes[name] = {}#create the dictionary for the added item
    recipes[name]['Cuisine'] = cuisine.lower()#add the value for cuisine
    recipes[name]['Ingredients']=[i.lower() for i in ingredients.split(',') if len(ingredients.split(','))>0]#add ingredients split by commas
    recipes[name]['Prep Time'] = prepTime#add prep time
    recipes[name]['Difficulty']=diff#add difficulty
    recipes[name]['Rating']= rating #add rating
    label.config(text="Added")#confirm addition
##########################################################
def add_text(label,add):#function to add text to an existing label
    current = label["text"]#copy the current text
    new = current+'\n'+add#add the added string to the existing one seperated by a new line
    label.config(text=new)#change the label to the text value
##########################################################
def printRecipe(name:str,label):#function to print a reicpe
    add_text(label,f"Recipe: {name}")#print the recipe (used the add_text function to print multiple recipes without overwriting)
    for k,v in recipes[name].items():#loop over the recipe for each value and key
        if k == 'Prep Time':#special case to print the prep time with the word minute
            add_text(label,f"{k}: {v} minutes")
            continue
        add_text(label,f"{k}: {v}")#print the current key and value
    add_text(label,"\n")#seperate printed recipes
##########################################################
def recom(cuisine: str,label):#function to get recommendation
    recList = []
    label.config(text="")#clear previous text
    for k,v in recipes.items():#check if the recommended cuisine exists
        if v['Cuisine'].lower() == cuisine.lower():
            recList.append(k)#if so add the keys to a list
    if len(recList)>0:#if the cuisine is in the data print the recipes that match
        add_text(label,"based on your love of %s cuisine, try these recipes: \n"%cuisine)
        for i in recList:
            printRecipe(i,label)
    else:#if not print a random recipe from the data
        x = randint(0,len(recipes)-1)#using a random indice
        j=0
        for i in recipes.keys():#get the random recipe
            if j==x:
                randomRecommendation = i
            j+=1
        add_text(label,"No recipes found in this cuisine, try this recipe instead!")
        printRecipe(randomRecommendation,label)
#############################################################
def findRecipe(name,label):
    found = []
    label.config(text="")
    for k,v in recipes.items():#search if the name matches an existing recipe
        if name.lower() in k.lower().split():
            found.append(k)#if so add it to the list
    if len(found)<1:
        add_text(label,"No recipes with that name were found")
    else:
        for i in found:
            printRecipe(i,label)
#############################################################
def filter(label,diff=None,prepTime=None,rating=None):
    results = []
    label.config(text="")
    for k,v in recipes.items():#search the recipes to find recipes that match the criteria
        if((v['Difficulty'].lower()== diff.lower() or diff is None)and(v['Prep Time']<prepTime or prepTime is None)and (rating<v['Rating']or rating is None)):
           results.append(k)
    if len(results)>0:
        add_text(label,"Here are the recipes that match your criteria:")
        for i in results:
            printRecipe(i,label)
    else:
        add_text(label,"No recipes found matching your criteria.")
##############################################################
import tkinter as tk#import gui library
def show_frame(frame,label=None):#function to display the frame(page)
    if label is not None:
        label.config(text="")#empty the given label
    frame.tkraise()
################################################################
def printL(label,add):#print text into a label
    label.config(text=add)
##################################################################
def submit():#get the selection from the main menu
    selection = (choicebox.curselection())#get the current selection
    if selection:#make sure something is selected
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
            root.destroy()#leave when option 5 is chosen
########################################################################
root = tk.Tk()#set the root page
root.title("Recipe Picker")#set the title
root.geometry("400x800")#set the starting size
#######################
main = tk.Frame(root)#create the main page
reco = tk.Frame(root)#create the recommendation page
fnd = tk.Frame(root)#create the find page
fltr = tk.Frame(root)#create the filter page
add = tk.Frame(root)#create the find page
for frame in (main,reco,fnd,fltr,add):#set all the frames in the same position so they overlap
    frame.place(x=0,y=0,relwidth=1,relheight=1)
####################### main page
main.pack()#place the frame
welcome = tk.Label(main,text="Welcome to saif's recipe picker!")
welcome.pack()
choose = tk.Label(main,text='Choose an option: ')
choose.pack()
choicebox = tk.Listbox(main,height=5,width=35)#make a list of the page options
choicebox.insert(tk.END,"1.Get recipe recommendations")
choicebox.insert(tk.END,"2.Search for a recipe")
choicebox.insert(tk.END,"3.Filter recipes(by time/difficulty/rating)")
choicebox.insert(tk.END,"4.Add a new recipe")
choicebox.insert(tk.END,"5.Exit")
choicebox.pack()
choicebox.bind("<<ListboxSelect>>", lambda event: submit())#switch the screen based on input
canvas = tk.Canvas(main,width=400,height=400,bg='white')#add a white canvas to cover any other frames in the background
canvas.pack()

######################## recommendation page
recoTitle = tk.Label(reco,text="Enter your favourite cuisine")
recoTitle.pack()
cuis = tk.Entry(reco)#get input
cuis.pack()
recoOut = tk.Label(reco,text="")#output
recoOut.pack()
recoSubButton = tk.Button(reco,text="Submit",command = lambda: recom(cuis.get(),recoOut))#submit button (activates the recom function)
recoSubButton.pack()
recoBackButton = tk.Button(reco,text="Back to main menu",command=lambda: show_frame(main,recoOut))#goes back to main menu by pushing the main menu to the front
recoBackButton.pack()

################################## search page
fndTitle = tk.Label(fnd,text="Enter the name of the recipe")
fndTitle.pack()
fndName = tk.Entry(fnd)#input
fndName.pack()
fndOut = tk.Label(fnd,text="")#output
fndOut.pack()
fndSubButton = tk.Button(fnd,text="Search",command=lambda: findRecipe(fndName.get(),fndOut))
fndSubButton.pack()
fndBackButton = tk.Button(fnd,text="Back to main menu",command=lambda: show_frame(main,fndOut))
fndBackButton.pack()

################################### filter page
fltrTitle1 = tk.Label(fltr,text="Enter difficulty")
fltrTitle1.pack()
fltrDifficulty = tk.Listbox(fltr,height=3)#list of difficulties
fltrDifficulty.insert(tk.END,"Easy")
fltrDifficulty.insert(tk.END,"Medium")
fltrDifficulty.insert(tk.END,"Hard")
fltrDifficulty.pack()
fltrTitle2 = tk.Label(fltr,text="Max prep time")
fltrTitle2.pack()
fltrPrepTime= tk.Scale(fltr,from_=5,to=120,orient='horizontal',resolution=5)#slider with a five unit interval
fltrPrepTime.pack()
fltrTitle3 = tk.Label(fltr,text="Min Rating")
fltrTitle3.pack()
fltrRating = tk.Scale(fltr,from_=1,to=5,orient='horizontal',resolution=0.1)#slider with a 0.1 unit interval
fltrRating.pack()
fltrOut = tk.Label(fltr,text="")
fltrOut.pack()
fltrSubButton = tk.Button(fltr,text="Search",command=lambda: filter(fltrOut,fltrDifficulty.get(fltrDifficulty.curselection()[0]),int(fltrPrepTime.get()),int(fltrRating.get())))
fltrSubButton.pack()
fltrBackButton = tk.Button(fltr,text="Back to main menu",command=lambda: show_frame(main,fltrOut))
fltrBackButton.pack()
################################### adder page 
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
addIngredients = tk.Entry(add)#enter the list of ingredients seperated by commas
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
ingredientList = addIngredients.get().split(',')#split the ingredients into a list
addOut = tk.Label(add,text='')
addOut.pack()
addSubButton = tk.Button(add,text="Add",command=lambda: fillRec(addName.get(),addOut,addCuisine.get(),addIngredients.get(),addPrepTime.get(),addDifficulty.get(addDifficulty.curselection()[0]),addRating.get()))
addSubButton.pack()
addBackButton = tk.Button(add,text="Back to main menu",command=lambda: show_frame(main,fltrOut))
addBackButton.pack()
###################################
show_frame(main)#start with the main menu
root.mainloop()#loop over the interface
