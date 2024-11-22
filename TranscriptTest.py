import requests

# Define the server URL (adjust the port if necessary)
url = "http://127.0.0.1:8000/analyze-text"

# Define the payload with the address
payload = {
"transcript": """
[00:00:00]
Speaker 1: David 22 for a disorderly.
Speaker 2: [unintelligible]
Speaker 1: It's gonna be 650 South Forest on the roof there are a group of nine to 12 subjects on the roof throwing objects off of it.
[00:00:10]
Speaker 3: Two East.
Speaker 4: Central staff left.
Speaker 5: Two eleven traffic Cross and Adams.
[00:00:18]
Speaker 1: Twenty-two twenty-nine [unintelligible] 911 hang-up.
[00:00:22]
[unintelligible]
[00:00:24]
Speaker 6: Twenty-two
Speaker 7: Zero Paul Xavier King Zero Zero
[00:00:31]
[unintelligible]
Speaker 8: Clear cross [unintelligible].
[00:00:35]
Speaker 1: Six Zero Six Zero Deller. There's a male that said we don't need the cops here, when he answered he said it was an accident.
[00:00:46]
Speaker 9: Twenty-two Michigan then.
Speaker 4: [unintelligible]
[00:00:48]
Speaker 3: David twenty-two arrival.
[00:00:50]
Speaker 2: Arrival.
Speaker 6: Seven Six Nine arrival I need mileage four nine three seven six.
[00:00:57]
Speaker 1: Clear forty-two at the red light.
Speaker 7: Zero two four we'll be in route to Wheeler to get some fuel.
[00:00:60]
Speaker 1: Clear.
[unintelligible]
Speaker 2: Clear here.
Speaker 3: David twenty-two subject appears to be DOA [unintelligible] subject appears to be DOA [unintelligible].
[00:01:10]
Speaker 1: Clear. Clear.
Speaker 4: Two Twelve robbery.
[00:01:15]
Speaker 2: Zero twenty-six for a noise complaint.
Speaker 4: Control [unintelligible]
[00:01:20]
Speaker 2: Thank you
Speaker 1: Two thirteen North Ingalls for a loud party with loud music.
[00:01:25]
Speaker 6: Twenty two [unintelligible].
[unintelligible]
Speaker 2: Copy
Speaker 7: Twenty-nine I'm out.
Speaker 2: Copy
[00:01:32]
Speaker 3: Six thirty.
Speaker 5: Six thirty go ahead.
Speaker 4: Can you go to Leena please.
[unintelligible]
[unintelligible]
[00:01:39]
Speaker 4: Twenty-two [unintelligible] a plate.
[00:01:40]
Speaker 1: Go ahead.
Speaker 4: Four Queen Charles King Two Seven Four Q C K Two Seven.
Speaker 1: Valid on 2009 Mercury Sable [unintelligible].
[00:01:50]
Speaker 5: Seven six five C five.
Speaker 3: Seven two eight three six seventy-two thousand eight hundred and thirty-six.
Speaker 5: Clear thank you.
Speaker 6: [unintelligible] you wanna try calling that number back it's pretty dark and quiet here.
[00:02:00]
[unintelligible]
Speaker 7: Paul on the route to Saint Jones, my partner's in there.
Speaker 1: Clear.
Speaker 8: Two six seven O seven
[00:02:10]
Speaker 1: Seven o seven.
Speaker 5: Seven o seven.
Speaker 9: Turn on [unintelligible]
Speaker 3: [unintelligible] is saying that the children should be with another male there, I don't know if you were going or not but just letting you know. 
[00:02:22]
Speaker 3: Clear.
[unintelligible]
[unintelligible]
[00:02:27]
Speaker 4: Show me a route to [unintelligible].
Speaker 1: Five three two South Fifth there is a nineteen to twenty year old female who had too much to drink, vomiting, somewhat unresponsive, weak pulse, light breathing.
[00:02:37]
Speaker 2: Central on the air for Ann Arbor city fire rescue one two for a medical at five thirty-two South Fifth Avenue. We have a twenty year old female unconscious and breathing. Report is high intox. HVA's in route priority one. Timeout: midnight forty-nine.
[00:02:55]
Speaker 1: Clear.
Speaker 2: Two eleven.
Speaker 4: Two eleven [unintelligible].
[00:03:00]
Speaker 3: Seven twenty-two we'll be clear [unintelligible].
Speaker 5: Twenty-two can you send me that [unintelligible] in.
[00:03:06]
Speaker 1: Affirm. Two twelve [unintelligible].
Speaker 4: Yeah I'm in contact with the subject they said they don't need [unintelligible] everything is okay.
Speaker 1: Okay, I'll show you complete twelve ninety clear.
[00:03:16]
[unintelligible]
Speaker 3: Seven two in arrival at transit.
Speaker 2: Clear [unintelligible].
Speaker 3: Seven one.
Speaker 2: Go ahead.
Speaker 3: I meant I have a stop B course and the bypass, Edward Union John seven four seven seven.
[00:03:31]
[unintelligible]
[00:03:35]
Speaker 1: [unintelligible] responding to four nine zero [unintelligible] for a fifty-five year old female having chest pain and difficulty breathing, she was declared conscious and breathing at hospital
[00:03:47]
[unintelligible]
Speaker 4: Seven O seven for an arrival. Seven O seven
Speaker 2: Go ahead.
[00:03:50]
Speaker 4: I'll be attempting conflict at department fifty-eight.
Speaker 3: Zebra two six in the area.
Speaker 1: Clear.
Speaker 2: Clear. [unintelligible]
[00:04:00]
[unintelligible]
Speaker 1: Clear.
Speaker 3: David twenty-two arrival. [unintelligible]
Speaker 1: Arrival.
[unintelligible]
Speaker 1: Clear. Seven O one secure the [unintelligible].
[00:04:12]
Speaker 3: Secure thank you.
Speaker 1: Clear. Seven O seven do you see yourself [unintelligible].
Speaker 5: Confirm [unintelligible] thank you.
Speaker 1: Clear.
[00:04:20]
Speaker 3: Seven six five complete.
Speaker 1: Clear complete.
Speaker 4: [unintelligible]
[00:04:25]
Speaker 1: Go ahead.
Speaker 4: We're gonna be Michigan at Ann Arbor we're at four Henry David five six five two one eight a black chevy cruise.
Speaker 1: Clear Michigan Ann Arbor.
[00:04:34]
Speaker 3: [unintelligible] two O four responding direct.
Speaker 2: [unintelligible] direct we can answer.
[00:04:40]
Speaker 5: Five six zero South.
Speaker 2: Five six three.
Speaker 4: Washtenaw Gulf side. Edward Henry Xray six eight seven
Speaker 2: Clear Washtenaw [unintelligible] zero six security.
Speaker 4: Secure complete thank you.
[00:04:53]
Speaker 2: Clear
Speaker 3: Seven O one can you get me one hook started.
Speaker 2: [unintelligible]
Speaker 6: Adam two one detail complete.
Speaker 1: Complete. Eighteen Frank one security on your [unintelligible].
[00:05:03]
[unintelligible]
Speaker 1: Five six three security on your stop.
Speaker 6: Five six three I'm secure.
Speaker 1: [unintelligible] two fourteen two twelve two eleven for a [unintelligible].
[00:05:12]
Speaker 5: Two O nine go for it.
Speaker 2: South and then one one one eight Monroe eleven eighteen Monroe off of Second. Still working on getting further uncooperative female advising she just got pepper sprayed there's some yelling in the background.
[00:05:23]
[unintelligible]
Speaker 2: [unintelligible] city unit's heading towards that FA. Updated address's gonna be one three one eight Monroe street. Caller's advising that a female came up to her door advising she was pepper sprayed in the [unintelligible] there. We're still trying to figure it out.
[00:05:37]
[unintelligible]
[unintelligible]
Speaker 3: Seven O one
[00:05:41]
Speaker 1: Seven O one
Speaker 3: You can disregard on that hook.
Speaker 1: Clear
[00:05:46]
Speaker 4: Two fourteen who exactly is fighting do we know?
Speaker 6: [unintelligible] arrival.
Speaker 4: [unintelligible]
Speaker 1: [unintelligible] traffic on Metro East [unintelligible].
[00:05:55]
[beep beep]
Speaker 6: Seven two eight complete [unintelligible].
[00:06:00]
Speaker 2: Clear
[beep beep]
Speaker 3: [unintelligible] heading to [unintelligible] South Wallace [unintelligible] South Wallace. Subject is a laying in  the street with a butcher knife, uh larger size Hispanic male screaming and yelling our caller disconnected.
[00:06:18]
[beep]
Speaker 6: Clear
Speaker 4: Two O nine can you send me medical for a 
Speaker 6: young lady [unintelligible] she can breath [unintelligible]
Speaker 2: Affirm we haven't found [unintelligible] inside at thirteen eighteen Monroe.
[00:06:32]
Speaker 1: County [unintelligible]
[beep]
Speaker 4: Yes ma'am [unintelligible]
Speaker 1: [unintelligible] thirteen eighteen Monroe Street secure. [unintelligible].
[00:06:43]
[beep]
Speaker 5: Five six [unintelligible] service good night.
Speaker 4: Five eight [unintelligible].
Speaker 3: Sixteen O five traffic [unintelligible].
Speaker 6: [unintelligible]
Speaker 7: [unintelligible]
[00:06:54]
Speaker 3: Two Nora Robert Robert Three Six uh black Volkswagen.
Speaker 1: Clear.
[00:07:00]
[beep beep beep]
[unintelligible]
Speaker 2: Clear all secure for first and [unintelligible] secure on Monroe. West Monroe traffic.
[00:07:10]
Speaker 3: This man will be covering Superior township as a complaint guard til zero four.
Speaker 2: Clear.
"""
}

# Send the POST request
response = requests.post(url, json=payload)
# Print the response from the server
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

url = "http://127.0.0.1:8000/check-proximity"

for addy in response.json():
    print(addy)
    formatted_addy = {
        "address": {
            "address": addy["address"]
        }
    }   
    print(formatted_addy)
    payload = formatted_addy
    newResponse = requests.post(url, json=payload)

