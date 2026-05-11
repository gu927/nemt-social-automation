import datetime
import json
import os
import random

def get_daily_theme():
    day_name = datetime.datetime.now().strftime('%A').lower()
    try:
        with open('content/themes.json') as f:
            themes = json.load(f)
        return themes.get(day_name, themes['monday'])
    except:
        return {"theme": "General NEMT Care", "examples": ["Professional service you can trust."]}

# Example post generator (expand with AI-style templates)
def generate_post(theme):
    base = f"Good {datetime.datetime.now().strftime('%A')} from SpeedCare Transportation in Bakersfield!\n\n"
    base += f"{theme['theme']}: {random.choice(theme.get('examples', ['']))}\n\n"
    base += "At SpeedCare, we provide safe, reliable, wheelchair-accessible non-emergency medical transportation. 24/7 service you can trust. 💙\n\n"
    base += "📍 Bakersfield & Kern County\n"
    base += "📞 661-490-0641\n"
    base += "#SpeedCare #NEMT #Bakersfield #MedicalTransportation"
    return base

if __name__ == "__main__":
    theme = get_daily_theme()
    post = generate_post(theme)
    print(post)
    # In real workflow: post to Facebook
