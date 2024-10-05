# File: sports_stats_scraper.py
import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape sports statistics from a static page
def scrape_static_page(url):
    # Send a GET request to fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract player stats from a table
        table = soup.find('table', {'id': 'stats-table'})  # Adjust the table ID to match the website structure
        rows = table.find_all('tr')

        player_data = []

        # Loop through rows and extract data
        for row in rows[1:]:  # Skip header row
            cells = row.find_all('td')
            player_name = cells[0].text.strip()
            goals = cells[1].text.strip()
            player_data.append((player_name, goals))  # Store player stats as tuples

        # Save the player stats to a CSV file
        save_to_csv(player_data, 'player_stats.csv')

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Function to scrape statistics from a form submission page
def scrape_with_form_submission(url, date):
    form_data = {
        'game_date': date  # Adjust the field name according to the website's form
    }

    # Send a POST request with the form data
    response = requests.post(url, data=form_data)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract game results from a table
        table = soup.find('table', {'id': 'results-table'})  # Adjust the table ID to match the website structure
        rows = table.find_all('tr')

        game_results = []

        for row in rows[1:]:  # Skip header row
            cells = row.find_all('td')
            team1 = cells[0].text.strip()
            team2 = cells[1].text.strip()
            score = cells[2].text.strip()
            game_results.append((team1, team2, score))  # Store game results as tuples

        # Save the game results to a CSV file
        save_to_csv(game_results, 'game_results.csv')

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Function to save data to a CSV file
def save_to_csv(data, filename):
    # Open CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        if 'player' in filename:
            # Write headers for player stats
            writer.writerow(['Player Name', 'Goals'])
        else:
            # Write headers for game results
            writer.writerow(['Team 1', 'Team 2', 'Score'])

        # Write data rows
        for row in data:
            writer.writerow(row)

# Example usage
if __name__ == "__main__":
    # Scrape static page for player statistics
    scrape_static_page('https://example.com/sports-stats')

    # Scrape form-submission page for specific game date results
    scrape_with_form_submission('https://example.com/game-results', '2023-10-01')

    # Add a delay between requests to avoid overloading the server
    time.sleep(2)
