import webbrowser

SITES = {
    # 🌐 General
    "google": "https://www.google.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://duckduckgo.com",

    # 📚 Learning
    "wikipedia": "https://www.wikipedia.org",
    "khan academy": "https://www.khanacademy.org",
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "udemy": "https://www.udemy.com",
    "cs50": "https://cs50.harvard.edu",
    "geeks for geeks": "https://www.geeksforgeeks.org",
    "tutorialspoint": "https://www.tutorialspoint.com",

    # 🎥 Entertainment
    "youtube": "https://www.youtube.com",
    "netflix": "https://www.netflix.com",
    "hotstar": "https://www.hotstar.com",
    "prime video": "https://www.primevideo.com",
    "spotify": "https://open.spotify.com",
    "gaana": "https://gaana.com",
    "wynk": "https://wynk.in",

    # 📱 Social Media
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://twitter.com",
    "threads": "https://www.threads.net",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "quora": "https://www.quora.com",
    "pinterest": "https://www.pinterest.com",
    "snapchat": "https://web.snapchat.com",

    # 👨‍💼 Productivity & Tools
    "gmail": "https://mail.google.com",
    "google drive": "https://drive.google.com",
    "google docs": "https://docs.google.com",
    "google meet": "https://meet.google.com",
    "notion": "https://www.notion.so",
    "canva": "https://www.canva.com",
    "zoom": "https://zoom.us",
    "onedrive": "https://onedrive.live.com",

    # 👨‍💻 Developer Tools
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt": "https://chat.openai.com",
    "replit": "https://replit.com",
    "codepen": "https://codepen.io",
    "w3schools": "https://www.w3schools.com",
    "figma": "https://www.figma.com",

    # 💼 Career
    "naukri": "https://www.naukri.com",
    "linkedin jobs": "https://www.linkedin.com/jobs",
    "indeed": "https://www.indeed.com",
    "internshala": "https://internshala.com",
    "glassdoor": "https://www.glassdoor.com",

    # 📰 News
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "the hindu": "https://www.thehindu.com",
    "times of india": "https://timesofindia.indiatimes.com",
    "ndtv": "https://www.ndtv.com",
    "moneycontrol": "https://www.moneycontrol.com",
}

def open_website(command):
    for key in SITES:
        if key in command:
            webbrowser.open(SITES[key])
            return
    print("Website not found.")
