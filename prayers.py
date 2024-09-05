import requests
import tkinter as tk
from tkinter import ttk, messagebox


def fetch_prayers_data(city, country):
  # Construct the API URL with the provided city and country
  url = f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2"

  try:
    # Send a GET request to the API URL
    response = requests.get(url)
    
     # Parse the response as JSON data
    info = response.json()
    
    # Check if the "data" key exists in the JSON response
    if "data" in info:
      
      # Access the first item (index 0) in the "data" list
      data = info["data"][0]

      # Extract the prayer timings from the selected data
      timings = data["timings"]
      return timings
    else:
      return None
      # Handle exceptions and return an error message
  except Exception as e:
    return f"Undefined Error! {e}"

def gui_fetch_prayers_data():
  city = city_entry.get()
  country = country_entry.get()
  if city and country:
    res = fetch_prayers_data(city, country)
    for name, time in res.items():
      results.insert(tk.END, f"{name}: {time}")
  else:
    messagebox.showerror("Error Message", "Unable to fetch the prayer time, Please enter correct city and country")
  

# Create the main application window using tkinter
app = tk.Tk()
app.title("Prayer Times")

# Create a frame to hold widgets with some padding
frame = ttk.Frame(app, padding=20)
frame.grid(row=0, column=0)

# Create a label widget for the "City" input
city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=5)

# Create an entry widget for users to input the city
city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=5)

# Create a label widget for the "Country" input
country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=5)

# Create an entry widget for users to input the country
country_entry = ttk.Entry(frame, width=20)
country_entry.grid(row=1, column=1, pady=5)

# Create a button widget for fetching prayer times, and link it to the `gui_fetch_prayers_data` function
button = ttk.Button(frame, text="Get Prayer Time", command=gui_fetch_prayers_data)
button.grid(row=2, column=0, columnspan=2, pady=5)

# Create a Listbox widget to display prayer time results
results = tk.Listbox(frame, height=11, width=30)
results.grid(row=3, column=0, columnspan=2, pady=5)

# Start the main event loop of the application
app.mainloop()
