from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQCzuVtZPlKlK7fhgkBhthAY496SSya5n4PhVL6Bxt9GFjKaSSEsyFVl3Xx_cN0KdBvIx4f5NIb4ZVcbjrBWUkKgd81GbhHSGyR7yIoE5ollJOyYraK4-HrDFdMyDxpcAXfh1W6j6chX5CHYxnMaZToT-XjyrWV21twKCWImy1FyqhBzPRgSJjZ1nuuKklR7F-sriOWIeWXRlCXp0mzyfaGppig_8U7UQ3dlZsBsrZtgQg-5BWMMTv1Cj6HSlsm0BWrcNIXIjScP72V3O0z86RXaKvA1DX8kiyaNalX5bEaR3ATx09MwU7qiRJzh_ihufrmqdnZzYSap9TPKxB6N4pWMe27vYQA")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
BOT_NAME = getenv("BOT_NAME", "𝙂𝙖𝙡𝙖𝙭𝙞𝙣𝙖")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GalaXinaVcAssistant")
BOT_USERNAME = getenv("BOT_USERNAME", "GalaXinaBot")


API_ID = int(getenv("API_ID", "8755605"))
API_HASH = getenv("API_HASH", "9d067982dcaa2f7020957036e2a1cb89")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2067182444").split()))
