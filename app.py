from Macros import Macros
from Chef import Chef
from foods import Foods


saturday = Macros("Saturday", 1707, 128, 256, 18, "weights")
sunday = Macros("Sunday", 1607, 140, 180, 35, "HIIT")
monday = Macros("Monday", 1507, 169, 75, 58, "weights")
tuesday = Macros("Tuesday", 1507, 169, 75, 58, "weights")
wednesday = Macros("Wednesday", 1707, 128, 256, 18, "rest")
thursday = Macros("Thursday", 1507, 169, 75, 58, "weights")
friday = Macros("Friday", 1507, 169, 75, 58, "rest")


Chicken = Foods("6oz", 6, 50, 0, 282)
steak = Foods("6oz", 20, 50, 0, 386)
Tuna = Foods("5oz", 1, 14, 0, 60)
Shrimp = Foods("8 medium", 1, 25, 0, 76)
Salmon = Foods("6oz", 11, 34, 0, 242)
pork = Foods("6oz", 6, 33, 1, 210)
Hotdog = Foods(1, 27, 8, 10, 320)
Yogurt = Foods("6oz", 0, 5, 18, 90)
Applesauce = Foods("4oz", 0, 1, 22, 90)
pasta = Foods("1 cup", 1, 7, 42, 210)
macncheese = Foods("6oz", 18, 21, 78, 570)
rice = Foods(".05 cup", 0, 6, 72, 320)
potato = Foods("1 cup", 0, 5, 35, 168)
corn = Foods("1 cup", 0, 3, 19, 88)
Greenveggie = Foods("1 cup", 0, 3, 6, 40)
Beans = Foods("0.5 cup", 1, 7, 21, 110)
Tofu = Foods("0.5 cup", 4, 7, 2, 63)
Peanutbutter = Foods("2 tbsp", 16, 7, 6, 190)
milk = Foods("1cup", 8, 8, 12, 148)
creamer = Foods("2 tbs", 3, 0, 10, 70)
pizzarolls = Foods("6 bites", 10, 6, 24, 200)

print(saturday.day)
print(saturday.activity)
print("menu options")
myChef = Chef()
myChef.hi_carb()

print(saturday.fat)
print(pasta.fat)
print(potato.fat)
print(Chicken.fat)
print(rice.fat)
print(steak.fat)
print(milk.fat)
print("remaining ")
print(float(saturday.fat)-(pasta.fat)-(rice.fat)-(Chicken.fat)-(pasta.fat)-(steak.fat)-(milk.fat))
print("----")