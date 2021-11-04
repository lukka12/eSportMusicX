from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQCrY7bPPrmPfksLhD_GI7l1P7XPrUBfL9Y4qyPRwuaEVfDke7SDN5kXLLZfiLcig7XbOcT_26CiER5WCQaKdTRuzxUjvIjKb_U-BQA-2jB9X9p2E5r_7g6MIM-HpmwhVKN9FWF50RX78oHWhUy7KjaNq1w-Z1QvZ9_YpBCl4_-20pLHrHfEQRRLTm9IA8-9RxQHncE3tsneQKgoce1TqWgPbtl0iws8Jh_AnHYKNoytSfng5eOdf9RcwcccTqUgs93iSLppO99X0TIA155_PKXbdeICCw64xbh333ze2eCa8wrQxaj2ksFp2NmHi0CoIzKireAamjaHM9pXU35HWk14e27vYQA")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
BOT_NAME = getenv("BOT_NAME", "𝙂𝙖𝙡𝙖𝙭𝙞𝙣𝙖")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GalaXinaVcAssistant")
BOT_USERNAME = getenv("BOT_USERNAME", "GalaXinaBot")


API_ID = int(getenv("API_ID", "8755605"))
API_HASH = getenv("API_HASH", "9d067982dcaa2f7020957036e2a1cb89")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2067182444").split()))
