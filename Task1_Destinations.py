# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# Destinations unique to your airline
unique_to_us = our_routes.difference(competitor_routes)

# Destinations unique to the competitor airline
unique_to_competitor = competitor_routes.difference(our_routes)

# Destinations that neither airline shares
neither_shared = our_routes.symmetric_difference(competitor_routes)

print("Destinations that both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_to_us)
print("Destinations unique to the competitor airline:", unique_to_competitor)
print("Destinations that neither airline shares:", neither_shared)
