from pathlib import Path
import json

# read the data as a string and convert to a Python object
path = Path('ch16-downloading-data/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# create a more readable version of the data file
path = Path('ch16-downloading-data/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)