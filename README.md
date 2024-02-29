<div align="center">

# 🍔 Food Hunting Project 🍔

</div>

This repository is dedicated to the noble pursuit of food hunting! 🍕🍣🍩 We operate a Discord bot that provides daily updates on free food events at USF. Additionally, we offer a web page to display these food events.

---

## 🚀 Getting Started

**Step 1:** Clone the repository

**Step 2:** Install the required packages

```bash
pip install -r requirements.txt
```

**Step 3:** Copy the `.env.example` file and rename it to `.env` and fill in the required fields

**Step 4:** Run the bot

```bash
python bot.py
```

## Features 🌟

1. 📅 Provides information about free food events at 12am every day
2. 🤖 Responds to user's command '!food' to give the food events from the current time to the end of the day

## Roadmap 🗺️

| Version             | Features                                                                                                                                                                                                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **v0.3** (Upcoming) | - Create a web interface <br> - Train AI to classify food types from descriptions                                                                                                                                                                                                                          |
| **v0.2** (Upcoming) | - Deploy bot to AWS for running 24/7 <br> - Set up a lightweight database to cache events every 8hrs, so we don't have to scrape the website all the time <br> - Use Docker Compose to run selenium as an independent service <br> - Update the bot to use the database to send the food events to Discord |
| **v0.1** (alpha)    | - Create a Discord bot <br> - Scrape the free food events from BullsConnect <br> - Send the food events to the Discord channel at 12am every day <br> - Respond to user's command '!events' to give the food events from the current time to the end of the day                                            |
