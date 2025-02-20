import re
from typing import Dict, List, Tuple
import flask

class SpaceStationBot:
    def __init__(self):
        # Initialize knowledge base
        self.qa_pairs: List[Tuple[str, str]] = [
            ("what is this space station", "This is Dark Station, a unique scientific research project located in Earth's orbit. We conduct experiments, study new technologies, and monitor the state of our planet."),
            ("name of the space station", "Our space station is called 'Dark Station.' It is an advanced scientific complex in low Earth orbit."),
            ("energy", "The station uses powerful solar panels that convert solar energy into electricity."),
            ("how many people", "The station can accommodate up to 16 astronauts at the same time, depending on the current mission."),
            ("food|eat", "Astronauts eat specially prepared space food, which is stored in airtight packaging."),
            ("modernization|upgrade", "Yes, in the future, new modules and systems will be added to improve conditions for the crew and expand scientific research capabilities."),
            ("research|science|study", "Our space station focuses on the study of dark matter. We examine its interactions with ordinary matter, conduct experiments on gravitational anomalies, and work on new technologies that could enable more efficient use of energy related to dark matter."),
            ("life support|technology", "Life support technologies include systems that provide astronauts with oxygen, remove carbon dioxide, and regulate temperature and humidity. Backup systems are also in place for emergencies."),
            ("living conditions|work conditions", "The station is designed for long-term missions in microgravity. The crew has everything needed for work and rest: sleeping quarters, a dining area, and specialized laboratories for scientific research."),
            ("orbit", "Our space station is in low Earth orbit (LEO) at an altitude of about 400 kilometers."),
            ("goodbye|bye", "Goodbye! If you have more questions about Dark Station, feel free to ask next time!")
        ]

    def get_response(self, user_input: str) -> str:
        # Convert input to lowercase for better matching
        user_input = user_input.lower().strip()
        
        # Check for empty input
        if not user_input:
            return "Please ask a question about Dark Station. I'm here to help!"

        # Look for matches in our knowledge base
        for patterns, response in self.qa_pairs:
            # Check if any of the patterns match the input
            if any(re.search(pattern, user_input) for pattern in patterns.split('|')):
                return response

        # Default response if no match is found
        return "I'm not sure about that aspect of Dark Station. Could you try asking your question differently? I can tell you about our research, living conditions, life support systems, and more."

    def chat(self):
        print("Welcome to Dark Station! I'm your AI assistant. How can I help you? (Type 'bye' to exit)")
        
        while True:
            user_input = input("You: ")
            if user_input.lower().strip() in ['bye', 'goodbye', 'exit']:
                print("Bot:", self.get_response("goodbye"))
                break
                
            response = self.get_response(user_input)
            print("Bot:", response)

# Example usage
if __name__ == "__main__":
    bot = SpaceStationBot()
    bot.chat()