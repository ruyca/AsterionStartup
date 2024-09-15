# AsterionStartup
This Flask application allows users to submit their business proposals, and in return, it uses OpenAI's ChatGPT to generate a SWOT (Strengths, Weaknesses, Opportunities, and Threats) analysis based on the provided information. The app processes the user data and returns the results in a user-friendly format.

## Features
- Accepts business proposal data from users.
- Uses OpenAI's ChatGPT to analyze the data and generate a SWOT analysis.
- Returns the analysis to the user through the app interface.

## Technologies
- **Flask**: To handle HTTP requests and manage the web interface.
- **OpenAI GPT**: For generating SWOT analysis based on the user input.
- **dotenv**: For managing environment variables securely.
- **Python**: General backend logic.

## Setup Instructions
### Prerequisites
- Python 3.x
- Pip (Python package installer)
- OpenAI API key

### Steps to Recreate the Project
1. Clone the repository:
```
git clone https://github.com/ruyca/AsterionStartup.git
cd AsterionStartup
```

2. Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Set up environment variables:

Create a .env file in the root directory of the project and add your OpenAI API key:
```
touch .env
```
Inside .env file:
```
OPENAI_API_KEY=your_openai_api_key_here
```
5. Run the application:
```
flask run
```
6. Access the application:
Open your web browser and go to http://127.0.0.1:5000/.

## Environment Variables
Ensure you have the following in your .env file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## License
This project is licensed under the MIT License.

