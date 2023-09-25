# flagG.py
# Celvis
# This script will continue to try and guess the number until it gets it correct, from there the rest of flagG is up to you to figure out

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
            # Error handling
            print("Unexpected response:", response.text)
    else:
        # output if the number is correct
        print("The correct number was found:", mid)

        # output the response from the site
        print(response.text)
        break
