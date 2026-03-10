# Traffic Light Simulation

import time

# List (Data Type) storing signals as Dictionary
signals = [
    {"color": "RED", "message": "STOP", "time": 5},
    {"color": "GREEN", "message": "GO", "time": 5},
    {"color": "YELLOW", "message": "WAIT", "time": 2}
]

# Boolean variable
running = True

# Function to display signal
def show_signal(signal):
    print(f"{signal['color']} LIGHT - {signal['message']}")
    time.sleep(signal["time"])
    print("-------------------------")

# Main function
def traffic_light():
    global running
    
    while running:
        for signal in signals:
            show_signal(signal)
        
        choice = input("Continue Traffic Light? (yes/no): ")
        if choice.lower() != "yes":
            running = False
            print("Traffic Light Simulation Stopped.")

# Run program
if __name__ == "__main__":
    traffic_light()