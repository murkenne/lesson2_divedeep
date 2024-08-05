'''Task 1: Code Correction You are provided with a Python script that 
is supposed to help in event planning, 
but it has errors. Identify and fix them.'''

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

if attendees > 100:
    recommend = "audio system and projector"
else:
    recommend = "projector"
print(venue)
print(f"Recommended equipment: " + recommend)







'''Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance your code to recommend
additional things like "audio system" or "projector" based on the number of attendees.'''