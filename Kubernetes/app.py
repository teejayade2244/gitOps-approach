import sys
from bs4 import BeautifulSoup
import requests

def fetch_and_visualize(url):
    try:
        # Force UTF-8 encoding for output
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')
        
        print("Fetching document...")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract coordinates and characters
        print("Processing coordinates...")
        data = []
        cells = soup.find_all('td')
        current_set = []
        processed = 0
        
        for cell in cells:
            value = cell.text.strip()
            if value:
                current_set.append(value)
                if len(current_set) == 3:
                    try:
                        if current_set[0] != 'x-coordinate':  # Skip header
                            x = int(current_set[0])
                            char = current_set[1]
                            y = int(current_set[2])
                            data.append((x, char, y))
                            processed += 1
                            if processed % 50 == 0:
                                print(f"Processed {processed} coordinates...")
                    except ValueError:
                        pass  # Skip invalid data silently
                    current_set = []
        
        # Create grid
        max_x = max(x for x, _, _ in data)
        max_y = max(y for _, _, y in data)
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
        # Fill grid
        for x, char, y in data:
            grid[y][x] = char
        
        # Print grid with proper encoding
        print("\nVisualization:")
        for row in grid:
            try:
                line = ''.join(row)
                print(line, flush=True)
            except UnicodeEncodeError:
                # Fallback for systems that can't display the characters
                line = ''.join('█' if c == '█' else '░' if c == '░' else ' ' for c in row)
                print(line, flush=True)
                
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
    fetch_and_visualize(url)