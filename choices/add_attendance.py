import datetime
import json
from datetime import date
class AddAttendance:

 

    def read_json(self):

        with open('sample2.json') as access_json:
            data = json.load(access_json)
            
        return data["employee_details"]
    
    
    
    def details_list(self,data_file):

        list_of_details = []

        for i in range(len(data_file)):
            attendance = input(f"Mark P or A for {data_file[i]['Name']}  ")
            dict_employee_details = {
                
                "id":data_file[i]["Employee_ID"],
                "name":data_file[i]["Name"],
                "attendance":attendance
            }

            list_of_details.append(dict_employee_details)
        
        return list_of_details




    def enter_date(self):

        date_enter = input("Enter date")

        return date_enter

    def to_json(self,attendance_dict):

        with open('attendance_file.json','r') as access_json:
            data1 = json.load(access_json)
            access_json.close()


        
        data1["attendance_details"].append(attendance_dict)

        with open('attendance_file.json','w') as outfile:
            data2=json.dumps(data1,indent=4)
            outfile.write(data2)

    def choice4_func(self):

        data_file = self.read_json()
        date_dict = self.enter_date()
        list_of_details = self.details_list(data_file)
        

        attendance_dict = {
            "date":date_dict,
            "details":list_of_details
        }

        

        self.to_json(attendance_dict)

        

