# Your code goes here:
def render_person(name, birthdate, eye_color, age, gender):
    descrição = f"{name} is a {age} years old {gender} born in {birthdate} with {eye_color} eyes"
    return descrição


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))