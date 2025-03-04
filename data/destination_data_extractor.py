import re
import json
import requests

class WikiVoyageScraper:
    def extract_travel_info(self, destination):
        url = "https://en.wikivoyage.org/w/api.php"
        params = {
            "action": "query",
            "titles": destination,
            "prop": "extracts",
            "format": "json",
            "explaintext": False
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"Failed to fetch data from Wikivoyage for {destination}."
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        page_id = next(iter(pages))
        extract_text = pages[page_id].get("extract")
        
        with open("data/destination_data.txt", "w", encoding="utf-8") as file:
            file.write(extract_text)
        
        pattern = r"==\s*(.*?)\s*==\n(.*?)(?=\n==|\Z)"
        matches = re.findall(pattern, extract_text, re.DOTALL)
        
        sections_dict = {}
        i = 0
        while i < len(matches) - 1:
            if matches[i+1][0][0] == "=":
                sub_dict = {}
                sub_dict["Description"] = matches[i][1]
                j = i + 1
                while j < len(matches) - 1:
                    if matches[j][0].startswith("="):
                        sub_dict[matches[j][0]] = matches[j][1]
                        matches.pop(j)
                    else:
                        sections_dict[matches[i][0]] = sub_dict
                        break
                j += 1
            else:
                sections_dict[matches[i][0]] = matches[i][1]
            i += 1
        
        destination_dict = {}
        destination_dict[destination] = sections_dict
        
        with open("data/destination_data.json", "w") as file:
            json.dump(destination_dict, file, indent=4)
        
        return sections_dict