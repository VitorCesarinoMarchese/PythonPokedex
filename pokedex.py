import requests
import tkinter as tk

def getpokemon(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/"
    url = url + pokemon
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  
        result_text = f"Tipo: {data["types"][0]["type"]["name"]}"
    else:
        print(f"Error: {response.status_code}")
        print("Verifique o nome do pokemon")
        return f"Error: {response.status_code}"

# Create the main window
root = tk.Tk()
root.title("Pokemon Type Check")

# Set the window size (width x height)
root.geometry("500x400")

# Create a label
label = tk.Label(root, text="Search your Pokémon")
label.pack(pady=10)

# Create a text entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button
button = tk.Button(root, text="Submit", command=lambda: getpokemon(entry.get()))
button.pack(pady=10)

# Create a label to display results
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=20)

# Run the application
root.mainloop()