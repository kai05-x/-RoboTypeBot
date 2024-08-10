import pyautogui
import time
import tkinter as tk
from tkinter import PhotoImage, messagebox

# Function to wait for user to click on the desired location
def wait_for_user_click():
    messagebox.showinfo("Click Now", "Please click on the location where you want to type text within 6 seconds...")
    time.sleep(6)  # Wait for user to click on the desired location
    x, y = pyautogui.position()  # Get the position of the mouse click
    return x, y

# Function to be called when the Start button is pressed
def on_start():
    global text_to_type, interval
    
    text_to_type = text_entry.get("1.0", tk.END).strip()  # Get text from Text widget
    try:
        interval = float(interval_entry.get())  # Get the interval value from the Entry widget
    except ValueError:
        messagebox.showerror("Invalid Interval", "Please enter a valid number for the interval.")
        return
    
    x, y = wait_for_user_click()
    pyautogui.click(x, y)  # Move the mouse to the clicked position
    time.sleep(1)  # Give a little time before typing
    pyautogui.typewrite(text_to_type, interval=interval)

# Function to show the main program container
def show_main_container():
    # Hide the start screen
    start_screen.pack_forget()
    
    # Create the main container with text and interval entry
    global text_entry, interval_entry
    
    main_container = tk.Frame(root)
    main_container.pack(fill=tk.BOTH, expand=True)

    text_label = tk.Label(main_container, text="Text to type:")
    text_label.pack(pady=5)

    text_entry = tk.Text(main_container, wrap=tk.WORD, width=60, height=10)  # Larger text box with word wrap
    text_entry.pack(pady=10, padx=10)

    interval_label = tk.Label(main_container, text="Typing Interval (seconds):")
    interval_label.pack(pady=5)

    interval_entry = tk.Entry(main_container, width=10)
    interval_entry.insert(0, "0.15")  # Default value for the interval
    interval_entry.pack(pady=5)

    start_button = tk.Button(main_container, text="Start", command=on_start)
    start_button.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Auto Typing GUI")
root.geometry("600x400")

# Load and set the background image (replace with your actual image path)
background_image = PhotoImage(file="C:\\Users\\tiwar\\Desktop\\pyrecon\\domain\\hud-screen-sci-fi-cyber-black-white-background_115968-176.png")

# Create the start screen container
start_screen = tk.Frame(root)
start_screen.pack(fill=tk.BOTH, expand=True)

background_label = tk.Label(start_screen, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the image cover the entire container

start_button = tk.Button(start_screen, width=15,bg="light pink" , text="Start", command=show_main_container)
start_button.pack(pady=180, padx=180)

# Run the GUI event loop
root.mainloop()
