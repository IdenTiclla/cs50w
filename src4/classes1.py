class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():
    # Create flight.
    f = Flight(origin="New york", destination="Paris", duration=540)

    # Change the value of a variable
    f.duration = 110

    # Print details about flight.
    print(f"origin: {f.origin}, destination: {f.destination} and duration: {f.duration}") 

if __name__ == "__main__":
    main()
