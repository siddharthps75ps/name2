 def mark_attendance(file_data):


            date = input("Enter date")

            date_data = {
                "date":date
            }


            with open('attendance_file.json','r') as access_json:
                    data = json.load(access_json)
                    access_json.close()


                data["attendance_details"].append(attendance_data)



                
                with open('attendance_file.json','w') as outfile:
                    data = json.dumps(data,indent=4)
                    outfile.write(data)
                    outfile.close()
                

  
                


                
                with open('attendance_file.json','r') as access_json:
                    data = json.load(access_json)
                    access_json.close()


                data["attendance_details"].append(attendance_data)



                
                with open('attendance_file.json','w') as outfile:
                    data = json.dumps(data,indent=4)
                    outfile.write(data)
                    outfile.close()



        file_data = read_data()
        mark_attendance(file_data)
        
        
        


        
        

            
details_of_employees = {
                #     "id":emp_id,
                #     "name":name,
                #     "attendance":attendance
                # }
                
                # attendance_data = {
                #     "date":date,
                #     "details": details_of_employees

        
    
    
        emp_id = file_data["employee_details"][i]["Employee_ID"]
                # name = file_data["employee_details"][i]["Name"]
                # attendance = input(f"Enter attendance for {emp_id}  {name} ")