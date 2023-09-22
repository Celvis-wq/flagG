# flagG.py
# Celvis

# Import
import requests

# the given url
getUrl = "http://172.25.0.20"

# the range of nubmers
low = 1
high = 1000

# while loop
while low <= high:
    mid = (low + high) // 2
    guessUrl = f"{getUrl}?guess={mid}"
    
    # Send the GET request
    response = requests.get(guessUrl)
    
    # Check
    if "wrong" in response.text.lower():
        if "too low" in response.text.lower():
            low = mid + 1
        elif "too high" in response.text.lower():
            high = mid - 1
        else:
            # error handling
            print("Unexpected response:", response.text)
            break
    else:
        # output if the number was guessed correctly
        print("Found the number:", mid)
        break