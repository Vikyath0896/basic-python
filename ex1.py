class VacuumCleanerAgent:
    def __init__(self, locations):
        self.locations = locations
        self.location_index = 0  # Initial location index
        self.percept = None  # Percept (dirty or clean)

    def sense(self, percept):
        self.percept = percept

    def act(self):
        if self.percept == "dirty":
            self.clean()
        else:
            self.move()

    def clean(self):
        print(f"Cleaning {self.locations[self.location_index]}")
        # Assume cleaning action takes place here
        print(f"{self.locations[self.location_index]} is now clean")

    def move(self):
        self.location_index = (self.location_index + 1) % len(self.locations)
        print(f"Moving to {self.locations[self.location_index]}")

# Example
if __name__ == "__main__":
    num_locations = int(input("Enter the number of locations: "))
    locations = [chr(ord('A') + i) for i in range(num_locations)]  # Generate alphabet names for locations
    agent = VacuumCleanerAgent(locations)

    while True:
        user_input = input(f"Enter percept (dirty/clean) or 'exit' to quit at {agent.locations[agent.location_index]}: ").lower()

        if user_input == 'exit':
            break

        agent.sense(user_input)
        agent.act()
