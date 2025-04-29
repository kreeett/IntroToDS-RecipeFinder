recipes = {}
def fillRec(name: str,cuisine: str,ingredients: list,perpTime: int,diff:int,rating:int):
    if recipes.get(name,0) is not 0:
        return -1
    recipes[name]['cuisine'] = cuisine
    recipes[name]['ingredients']=ingredients
    recipes[name]['difficulty']=diff
    recipes[name][perpTime] = perpTime
    recipes[name][rating]= rating
    
        
