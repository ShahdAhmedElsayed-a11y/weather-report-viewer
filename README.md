# Weather Report Viewer

Python app that fetches current weather from the OpenWeatherMap REST API,
parses the JSON response, stores it in a custom class, and prints a formatted summary.

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and put your OpenWeatherMap API key in it
5. Run: `python main.py`

## Notes
- Get a free API key at https://openweathermap.org/api
- Never commit your `.env` file.
