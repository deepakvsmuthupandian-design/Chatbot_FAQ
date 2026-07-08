import os
from dotenv import load_dotenv
from google import genai


class FAQModel:

    def __init__(self):
        # Load .env file from the same project folder
        load_dotenv()

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            print("ERROR: GEMINI_API_KEY was not found.")
            print("Create a .env file in chatbotfaq folder.")
            self.client = None
        else:
            self.client = genai.Client(api_key=self.api_key)
            print("Gemini API key loaded successfully.")

    def find_best_match(self, user_input):

        if self.client is None:
            return (
                "API key is missing. Please add GEMINI_API_KEY in the .env file."
            )

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=(
                    "You are a helpful educational chatbot. "
                    "Answer the user's question clearly and simply.\n\n"
                    f"User question: {user_input}"
                )
            )

            if response.text:
                return response.text

            return "The AI did not return an answer. Please try another question."

        except Exception as error:
            print("\n----- GEMINI ERROR -----")
            print(error)
            print("------------------------\n")

            return f"API connection error: {str(error)}"

    def get_all_topics(self):
        return [
            "AI",
            "Machine Learning",
            "Python",
            "Programming",
            "General Knowledge"
        ]