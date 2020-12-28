import json
import DATASTORAGE_SYS.config.configuration as con
import portalocker
#import threading
from os import path
from datetime import datetime
import DATASTORAGE_SYS.check_data as check

class DataStoreCRD:
    def create_data(self,KEY,DATA1,DATA2,time_to_live,default="Saved successfully"):
        try:
            with open(con.db_path+con.db_name) as jsondb_f1:
                #portalocker.lock(jsondb_f1, portalocker.LOCK_EX)
                data=json.load(jsondb_f1)
                #portalocker.lock(jsondb_f1, portalocker.LOCK_UN)
                if KEY in data.keys():
                    return "","BAD TRY! This key: '"+KEY+"' already existed...TRY AGAIN!"
                data[KEY]={"NAME":DATA1,"SUBJECT":DATA2,"time_to_live":time_to_live,"created_at":str(datetime.now())}
                obj=check.check_data_values()
                result,status=obj.check_create_data(data,KEY)
                if result==False:
                    return "","BAD TRY! "+status
                json_format = json.dumps(data)
                with open(con.db_path+con.db_name,"w+") as jsondb_f2:
                    #portalocker.lock(jsondb_f2, portalocker.LOCK_EX)
                    jsondb_f2.write(json_format)
                    #portalocker.lock(jsondb_f2, portalocker.LOCK_UN)

            #READING DATA
            return json_format, status+" and "+default
        except:
            j=json.dumps({})
            with open(con.db_path+con.db_name,"w+") as jsondb_f1:
                jsondb_f1.write(j)
            obj=DataStoreCRD()
            json_format, sta=obj.create_data(KEY,DATA1,DATA2,time_to_live,"Database not existed!....NEW DATABASE IS CREATED AND SAVED SUCCESSFULLY")
            return json_format, sta

    def read_data(self,KEY,default="Here is your data: "):
        try:
            with open(con.db_path+con.db_name) as jsondb_f1:
                #portalocker.lock(jsondb_f1, portalocker.LOCK_EX)
                data=json.load(jsondb_f1)
                #portalocker.lock(jsondb_f1, portalocker.LOCK_UN)
                obj=check.check_data_values()
                result,status=obj.check_time_span(data,KEY)
                if result == True:
                    return "BAD TRY! "+status
                json_format = json.dumps(data[KEY])
            return status+default+json_format
        except Exception:
            return "Key "+ KEY +" expires or not existed."

    def delete_data(self,KEY,default="Data is deleted associated with this key: "):
        try:
            with open(con.db_path+con.db_name) as jsondb_f1:
                #portalocker.lock(jsondb_f1, portalocker.LOCK_EX)
                data=json.load(jsondb_f1)
                #portalocker.lock(jsondb_f1, portalocker.LOCK_UN)
                obj=check.check_data_values()
                result,status=obj.check_time_span(data,KEY)
                if result == True:
                    return "BAD TRY! "+status
                del data[KEY]
                json_format = json.dumps(data)
                with open(con.db_path+con.db_name,"w+") as jsondb_f2:
                    #portalocker.lock(jsondb_f2, portalocker.LOCK_EX)
                    jsondb_f2.write(json_format)
                    #portalocker.lock(jsondb_f2, portalocker.LOCK_UN)
            #READING DATA
            return default+str(KEY)
        except Exception:
            return "Key: "+KEY+" not existed or may be expired."




