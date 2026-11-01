A = input("Enter status of Room A (Clean/Dirty): ").lower()
B = input("Enter status of Room B (Clean/Dirty): ").lower()

location = input("Enter vacuum location (A/B): ").upper()

while True:
    if location == "A":
        if A == "dirty":
            print("Room A is dirty. Cleaning Room A.")
            A = "clean"
        else:
            print("Room A is cleaned. Moving to Room B.")
            location = "B"

    else:
        if B == "dirty":
            print("Room B is dirty. Cleaning Room B.")
            B = "clean"
        else:
            print("Room B is cleaned. Moving to Room A.")
            location = "A"

    if A == "clean" and B == "clean":
        print("Both rooms are cleaned!")
        break

print("Cleaning completed.")
