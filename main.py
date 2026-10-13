from pyscript import display, document #link to index...?

members = [ "Zeek Fernandez ", "Cheree Mendoza", "Therese Reyes","Zoey Ledres", "Princess Schwab ", "Adrian Gavina", "Kevin Polillo", "Anton Vinzon", "Nelson Velasco ", "Earl Aljo","Elise Ramos", "Austin Ocampo", "Anton Vinzon" ] #im pretty sure this is the ganglang thats allowed

def get_IN(e):
    name1 = document.getElementById("fn").value
    name2 = document.getElementById("ln").value

    full_name = f"{name1.strip()} {name2.strip()}" #combines name
    is_member = full_name in members #true or false

    display("Oops! you are not on the Badminton Club list.", target="output") #displays when not a member (?)
