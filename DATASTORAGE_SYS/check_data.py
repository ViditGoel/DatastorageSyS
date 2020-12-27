import json
import DATASTORAGE_SYS.config.configuration as con
from datetime import datetime, timedelta
from dateutil.parser import parse

class check_data_values:
    def check_create_data(self, new_data, KEY):
        data_obj = json.dumps(new_data)
        if len(data_obj) > 1000000000:
            return False, "Data Size limit will exceed 1GB size(NOT ACCEPTABLE)."
        if len(KEY) > 32:
            return False, "Key size must be smaller than 32"
        if len(str(new_data[KEY])) > 16000:
            return False, "Values must be smaller tha 16kb"

        return True, "DATA IS FINE"

    def check_time_span(self, data, KEY):
        # Time of creation
        created_time = data[KEY]["created_at"]
        # Parse the datetime from the string date.
        created_time = parse(created_time)

        # Parse the time_to_live from data
        time_to_live = int(data[KEY]["time_to_live"])

        # Passed time till now:
        expired_datetime = created_time + timedelta(seconds=time_to_live)

        # Left time:
        remaining_seconds = (expired_datetime - datetime.now()).total_seconds()

        if remaining_seconds <= 0:
            with open(con.db_path+con.db_name) as jsondb_f1:
                data1 = json.load(jsondb_f1)
                del data1[KEY]
                json_format = json.dumps(data1)
                with open(con.db_path+con.db_name,"w+") as jsondb_f2:
                    jsondb_f2.write(json_format)

            return True, "Time span already complete there is no data"
        return False, "Data is live with its time and "





