import serial
import tkinter as tk

# Replace 'COM3' with your actual port
ser = serial.Serial('COM3', 9600, timeout=1)

def send_text():
    '''
    entry.get() gets the text you typed in the input box
    ser.write(); sends the text over serial to the arduino
    the .encode() turns the text into bytes, which is what serial needs
    entry.delete() clears the input box after sending
    '''
    text = entry.get()
    ser.write((text + "\n").encode())  # Include newline to trigger LCD display
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Send to Arduino")

entry = tk.Entry(root, width=30)
entry.pack(padx=20, pady=10)

send_button = tk.Button(root, text="Send to LCD", command=send_text)
send_button.pack(pady=10)

root.mainloop()
