name = 'Zed A. Shaw'
age = 35 #not lying
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

cm_height = height * 2.54
kg_weight = weight / 2.2


print(f"Let's talk about {name}.")
print(f"He's {height} or {cm_height} inches tall.")
print(f"He's {weight} or {kg_weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the color")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")