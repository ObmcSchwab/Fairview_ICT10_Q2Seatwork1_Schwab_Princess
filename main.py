from pyscript import display, document

# List of badminton club members
badminton_members = [
    "Zeek Fernandez ",
    "Cheree Mendoza",
    "Therese Reyes",
    "Zoey Ledres",
    "Princess Schwab ",
    "Adrian Gavina",
    "Kevin Polillo",
    "Anton Vinzon",
    "Nelson Velasco ",
    "Earl Aljo",
    "Elise Ramos",
     "Austin Ocampo",
    "Anton Vinzon" 
]

def check_member(e):
    # Get input values
    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()
    full_name = f"{first} {last}"

    # Membership check
    message = (
        f"🏸 Congratulations {full_name}! You are part of the Badminton Club."
        if full_name in badminton_members
        else f"❌ Sorry {full_name}, you are not on the Badminton Club list."
    )

    # Display result + extra message
    display(message, target="result")
    display("✨ Keep practicing and enjoy the game! ✨", target="extra")

