from data.destination_data_extractor import WikiVoyageScraper

class TripPlanner:
    def __init__(self):
        self.wiki_voyage_scraper = WikiVoyageScraper()
        self.destination = None
        self.travel_date = None
        self.duration = None
        self.budget = None
        self.trip_type = None
        self.transport_mode = None
        self.interests = None

    def get_trip_plan(self):
        trip_plan = {
            "destination": self.destination,
            "travel_date": self.travel_date,
            "duration": self.duration,
            "budget": self.budget,
            "trip_type": self.trip_type,
            "transport_mode": self.transport_mode,
            "interests": self.interests
        }
        return trip_plan