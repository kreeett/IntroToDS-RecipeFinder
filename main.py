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
'''
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
    '''
import tkinter as tk
root = tk.Tk()
root.title("Recipe Picker")
root.geometry("400x400")
frame = tk.Frame(root)
welcome = tk.Label(frame,text="Welcome to saif's recipe picker!")
welcome.pack()
choose = tk.Label(frame,text='Choose an option: ')
choose.pack()
choicebox = tk.Listbox(frame)
choicebox.insert(1,"1.Get recipe recommendations")
choicebox.insert(2,"2.Search for a recipe")
choicebox.insert(3,"3.Filter recipes(by time/difficulty/rating)")
choicebox.insert(4,"4.Add a new recipe")
choicebox.insert(5,"5.Exit")
choicebox.pack()
selection = (choicebox.curselection())
if selection==5:
    root.quit()
root.mainloop()
'''
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Greet", command=greet)
button.pack()
label = tk.Label(root, text="")
label.pack()
frame = tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Inside a frame")
label.pack()
var = tk.BooleanVar()
check = tk.Checkbutton(root, text="I agree", variable=var)
check.pack()
option = tk.StringVar()
rb1 = tk.Radiobutton(root, text="Option 1", variable=option, value="1")
rb2 = tk.Radiobutton(root, text="Option 2", variable=option, value="2")
rb1.pack()
rb2.pack()
listbox = tk.Listbox(root)
listbox.insert(1, "Apple")
listbox.insert(2, "Banana")
listbox.insert(3, "Cherry")
entry = var
listbox.pack()
root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title("Form Example")
root.geometry("400x300")
frame = tk.Frame(root)
frame.pack(pady=20)
tk.Label(frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)
tk.Label(frame, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1)
label = tk.Label(frame,text="")
label.grid(row=3,column=1)
def submit():
    name = name_entry.get()
    age = age_entry.get()
    label.config(text=f"Name: {name}, Age: {age}")
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack()
root.mainloop()
import tkinter as tk
def say_hello():
    label.config(text="Hello!")

root = tk.Tk()
root.title("Menu Example")
root.geometry("400x400")
frame=tk.Frame(root)
frame.pack(pady=20)
label = tk.Label(frame,text="")
label.pack()
# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" dropdown menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Say Hello", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add "File" menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Set menu bar to the root window
root.config(menu=menu_bar)
root.mainloop()
'''