import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Parse JSON response
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    def program_school(self):
        programs_list = []
        programs = self.get_programs()
        
        # Check if programs is not None and is a list
        if programs is not None and isinstance(programs, list):
            for program in programs:
                # Check if "agency" key exists in the program dictionary
                if isinstance(program, dict) and "agency" in program:
                    programs_list.append(program["agency"])
                else:
                    print("Invalid program structure:", program)
        else:
            print("Invalid or missing 'programs' data.")

        return programs_list

# Create an instance of GetPrograms
programs_instance = GetPrograms()

# Call program_school method
programs_schools = programs_instance.program_school()

# Print the result
for school in set(programs_schools):
    print(school)
