import requests
from prettytable import PrettyTable

def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        events = response.json()
        latest_events = events[:1]  # Get the 5 latest events
        
        # Create a table
        table = PrettyTable()
        table.field_names = ["Event Type", "Repository", "Created At"]
        
        # Add rows to the table
        for event in latest_events:
            event_type = event.get("type")
            repo_name = event.get("repo", {}).get("name")
            created_at = event.get("created_at")
            table.add_row([event_type, repo_name, created_at])
        
        print(table)
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
username=input("Enter user name: ")
get_user_activity(username)
