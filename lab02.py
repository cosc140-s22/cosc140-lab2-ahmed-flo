from enum import Enum
class FoodCategory(Enum):
	VEGETABLE = 1
	FRUIT = 2
	GRAIN = 3 
	PROTEIN = 4
	DAIRY = 5
	OIL = 6
	OTHER = 7

class FoodItem(object):
	def __init__(self,name,category,cal):
		self.name = name
		self.category = FoodCategory(category)
		self.cal = int(cal)

	def name(self):
		return self.name

	def category (self):
		return self.category

	def calories_per_100g(self):
		return self.cal

	def __str__(self):
		return F"{self.name} ({self.category}) {self.cal}cal/100g"

class FoodServing(object):
 
	def __init__(self,fooditem,amount):
		self.fooditem = fooditem
		self.amt = amount

	def food (self):
		return self.fooditem

	def amount (self):
		return self.amt

	def calories (self):
		return int (self.fooditem.calories_per_100g()/100 * self.amt)

	def __str__ (self):
		return F"{self.amt}g of {self.fooditem}"


class Meal (object): 
  def __init__ (self):
    self.list = []

  def addFood (self, serving):
    self.list.append (serving)

  def calories (self):
    sum = 0
    for serving in self.list:
      sum += serving.calories()
    return sum

  def __str__ (self):
    string = ""
    for serving in self.list: 
      string += str(serving) +"\n"
    return string
    
      