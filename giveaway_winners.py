import pandas as pd
import random

# Loading the CSV file, Add csv file path to "  r""  "
file_path = file_path = r""

data = pd.read_csv(file_path)

# Defining a function to calculate weights based on the criteria
def calculate_weight(row):
    if row["Are you subscribed to Amogh? (Link to Amogh's Channel)"].strip().lower() != "yes":
        return 0  # Exclude if not subscribed
    
    weight = 1.0  # Base weight
    
    # Increase weight for subscription
    weight += 0.1

    # Adjust weight based on Lamborghini Revuelto key status
    key_status = row["Do you have the key for the Lamborghini Revuelto?*"].strip()
    if key_status == "Yes, I have the Key, but I need blueprints for the car." or key_status == "No, I don't have the key.":
        weight += 0.02
    elif key_status == "Yes, I have the key and my Revuelto is maxed":
        weight += 0  # No additional weight for maxed cars

    return weight

# Calculated weights for each participant
data["Weight"] = data.apply(calculate_weight, axis=1)

# Filtered valid entries (weight > 0)
valid_entries = data[data["Weight"] > 0]

# Randomly select 10 winners based on weights
winners = valid_entries.sample(n=10, weights="Weight", random_state=42)

# Extracted the winner details
winners_list = winners[
    ["Your Nickname (the name you go by)", "Your Asphalt Unite Player ID (found in game profile & inbox)*"]
]

# Displayed the winners
print("The 10 Giveaway Winners Are:")
print(winners_list)

# Save the winners to a new CSV file
winners_list.to_csv("Giveaway_Winners.csv", index=False)
