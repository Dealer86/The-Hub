# <span style="color: #007bff;">The Hub</span>
The Hub is a place where you can retrieve and display news articles based on user-specified country and category also current/upcoming events from your preferred location.
### Deployment Instructions

### Windows:
1. Clone the git repository: `git clone https://github.com/Dealer86/The-Hub.git`.
2. CD into your created directory.
3. Create a new virtual environment by running `python -m venv .venv/`.
4. Activate the virtual environment by running `.\env\Scripts\activate`.
5. Upgrade pip by running `python.exe -m pip install --upgrade pip`.
6. Install the required dependencies by running `pip install -r requirements.txt`.
7. Change NEWS_API_KEY and SERPAPI_KEY located in project settings.py with your real API KEY from https://newsapi.org/ and https://serpapi.com/
8. Be sure the CD into the events_newsletter_project directory where manage.py module lives.
9. Run: `python manage.py runserver`
10. Check http://127.0.0.1:8000/.
