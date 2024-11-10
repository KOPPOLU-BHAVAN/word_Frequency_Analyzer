
# Top Words Frequency Analyzer

This project allows users to input a URL and the number of top frequent words they want to analyze from that page. The backend fetches the page content, processes the text, and returns the top N most frequent words, which are then displayed in a table on the frontend.

## Project Structure

The project is organized into two main parts:
1. **Frontend**: Contains the HTML and CSS files that create the user interface.
2. **Backend**: A Python Flask API that handles requests from the frontend, fetches webpage content, and processes it.

### Project Structure

```plaintext
project-folder/
├── backend/
│   └── app.py                # Backend Python file with Flask
├── frontend/
│   ├── index.html            # Frontend HTML file
│   └── style.css             # CSS file for styling the frontend
└── README.md                 # Project documentation
```

## Setup

### Prerequisites

Make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)

### Step 1: Setting up the Backend

1. Navigate to the `backend` folder in your terminal.
2. Install the required Python libraries:
   ```bash
   pip install flask beautifulsoup4 requests
   ```
3. Start the Flask server by running:
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000`.

### Step 2: Setting up the Frontend

1. Navigate to the `frontend` folder.
2. Open `index.html` in your preferred text editor.
3. To view the frontend, you can use a local server like Python's built-in HTTP server or the VS Code Live Server extension.
   
   If using Python’s HTTP server:
   ```bash
   python -m http.server 5500
   ```
   Then, open your browser and go to `http://127.0.0.1:5500` to see the frontend.

### Step 3: Running the Application

1. Make sure both the frontend and backend are running.
2. Open the frontend in your browser, enter a URL (e.g., `https://example.com`), specify the number of top words (e.g., 10), and click "Fetch Top Words".
3. The backend will fetch the page content, process it, and return the most frequent words, which will be displayed in a table on the frontend.

## Functionality

- **Input Fields**:
  - **URL**: Enter the URL of the webpage you want to analyze.
  - **Number of Top Words**: Enter the number of frequent words to display (e.g., 10).
  
- **Backend**:
  - The backend fetches the content of the provided URL.
  - It processes the text and calculates the most frequent words.
  - Returns the top N words and their frequencies to the frontend.

- **Frontend**:
  - Displays a table with the top N frequent words and their respective frequencies.
  - Shows a loader while the backend is processing the data.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap (for styling)
- **Backend**: Python, Flask, BeautifulSoup (for web scraping), Requests (for HTTP requests)
- **Libraries**: Bootstrap for styling the frontend and animations



## Troubleshooting

- **Failed to fetch data**: Make sure the backend Flask server is running.
- **MIME type error for CSS**: Ensure the `style.css` file is in the correct folder and is referenced correctly in `index.html`.
- **Loader not appearing**: Verify that the JavaScript is correctly controlling the loader visibility and that the backend is responding with valid data.


