
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from test import cartoonize_image  # Import the cartoonize function from test.py



def browse_file():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    
    if file_path:
        # Generate output file name by appending "_cartoon" to the original file name
        output_path = os.path.splitext(file_path)[0] + "_cartoon.jpg"  
        
        try:
            # Apply cartoon effect and save the image
            cartoonize_image(file_path, output_path)
            
            # Inform the user that the process is complete
            messagebox.showinfo("Success", f"Cartoonized image saved as {output_path}")
        except Exception as e:
            # Handle any error that might occur
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("No file selected", "Please select an image file")

# Set up the main application window
root = tk.Tk()
root.title("Cartoonizer")

# Set the size of the window and prevent resizing
root.geometry("600x400")  # Width x Height (larger window)
root.resizable(False, False)  # Prevent resizing the window

# Set the background color
root.configure(bg="#f0f8ff")  # Light blue background color

# Create a frame to center the button
frame = tk.Frame(root, bg="#f0f8ff")  # Use the same background color
frame.pack(expand=True)  # Expand the frame to fill the space

# Create the "Select Image" button with more color and styling
btn_browse = tk.Button(frame, 
                       text="Select Image", 
                       command=browse_file, 
                       width=20, 
                       height=2,  # Increase height for a bigger button
                       font=("Arial", 14),  # Change font style and size
                       bg="#ff6347",  # Tomato red background color
                       fg="white",  # White text color
                       relief="raised",  # Raised button effect
                       bd=5,  # Border width
                       activebackground="#ff4500",  # Active button color when clicked
                       activeforeground="yellow")  # Text color when clicked
btn_browse.pack()  # Center the button in the frame

# Run the application
root.mainloop()
