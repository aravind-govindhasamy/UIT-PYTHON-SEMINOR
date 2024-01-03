import time
import pyautogui

def send_proposal_message():
    proposal_message = "Will you marry me?"
    num_attempts = 10
    
    for attempt in range(1, num_attempts + 1):
        time.sleep(5)  # Give some time to switch to the desired text input area
        pyautogui.typewrite(proposal_message, interval=0.1)  # Type the message with a slight delay
        pyautogui.press('enter')  # Press Enter key to send the message

        # Simulate a response (you would replace this with actual logic based on her response)
        response = input(f"Attempt {attempt}/{num_attempts}: What is her response? (Type 'yes' or 'no'): ")

        if response.lower() == 'yes':
            print("Congratulations! She said yes!")
            break
        elif response.lower() == 'no':
            print("I will wait for you with a heart ♥️")
        else:
            print("Invalid response. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    send_proposal_message()
