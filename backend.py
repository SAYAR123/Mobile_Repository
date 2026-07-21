
import os
from dotenv import load_dotenv
from google import genai

# ----------------------------
# Mobile Repository
# ----------------------------

mobiles = []

# ----------------------------
# CRUD Operations
# ----------------------------

def add_mobile(name, brand, price):

    mobiles.append({
        "Name": name,
        "Brand": brand,
        "Price": price
    })


def view_mobiles():

    return mobiles


def update_mobile(old_name, new_name, brand, price):

    for mobile in mobiles:

        if mobile["Name"].lower() == old_name.lower():

            mobile["Name"] = new_name
            mobile["Brand"] = brand
            mobile["Price"] = price

            return True

    return False


def delete_mobile(name):

    for mobile in mobiles:

        if mobile["Name"].lower() == name.lower():

            mobiles.remove(mobile)

            return True

    return False


def search_mobile(keyword):

    keyword = keyword.lower()

    return [

        mobile

        for mobile in mobiles

        if keyword in mobile["Name"].lower()

        or keyword in mobile["Brand"].lower()

    ]


def sort_price():

    return sorted(mobiles, key=lambda x: x["Price"])


# ----------------------------
# Gemini AI
# ----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:

    client = genai.Client(api_key=API_KEY)

else:

    client = None


def ask_ai(question):

    if client is None:

        return "Gemini API key not found."

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=f"Give information about this mobile-phone related query as an expert:\n{question}"

        )

        return response.text

    except Exception:

        return (
            "🤖 Our AI assistant is taking a short break due to high demand.\n\n"
            "Please try again later.\n"
            "Meanwhile, you can continue using all the Mobile Repository features."
        )