import json

class SearchAndView:


    def choice5_func():

        

    
        def search_options():

            print("Choose The Method You Want To View")
            print("\n 1.Filter by Date")
            print("\n 2.Filter by Department")
            print("\n 3.Search for Employee ID")

            choice = int(input("Enter Choice"))
            return choice

            


        def read_attendance_json():

            with open('attendance_file.json','r') as access_json:
                data = json.load(access_json)
            return data["attendance_details"]


        def get_date_index(file_data):
            date_input = input("Enter date to search")
            
            for i in range(len(file_data)):
                if file_data[i]["date"] == date_input:
                    return i
                else:
                    print("Date not found")
                    break


        def filter_by_date(index,file_data):
            
            date_index = index

            for i in range(len(file_data[date_index]["details"])):
                print("\n")
                print(file_data[date_index]["details"][i])

        
        
        
        
        def read_json_employee():
            with open('sample2.json','r') as access_json:
                data = json.load(access_json)
            return data["employee_details"]

        
        def get_id_list(file_data_employee):
            id_list = []
            for i in range(len(file_data_employee)):
                id_list.append(file_data_employee[i]["Employee_ID"])

            return set(id_list)
            




        
        def get_department_list(file_data_employee):
            department_list = []
            for i in range(len(file_data_employee)):
                department_list.append(file_data_employee[i]["Department"])

            return set(department_list)

        def get_employee_id_from_department(dept,file_data_employee):

            emp_id_list = []

            for i in range(len(file_data_employee)):
                if file_data_employee[i]["Department"]==dept:
                    emp_id_list.append(file_data_employee[i]["Employee_ID"])
                else:
                    pass

                
            return emp_id_list


        
        choice = search_options()
        
        if choice == 1:
            file_data = read_attendance_json()
            date_index = get_date_index(file_data)
            filter_by_date(date_index,file_data)

        if choice == 2:
            
            file_data_attendance = read_attendance_json()
            file_data_employee = read_json_employee()
            department_list = get_department_list(file_data_employee)
            date_index = get_date_index(file_data_attendance)
            
            
            print(f"Choose Department  \n 1.{list(department_list)[0]} \n 2.{list(department_list)[1]} \n 3.{list(department_list)[2]}")
            choice = int(input("Select a Department"))

            if choice == 1:
                
                emp_id_list = get_employee_id_from_department(list(department_list)[0],file_data_employee)
                
                print(f"Attendance Details of {list(department_list)[0]} Department")
                for i in (file_data_attendance[date_index]["details"]):
                    if i["id"] in emp_id_list:
                        print(i)

                    




        if choice == 3:

            file_data_attendance = read_attendance_json()
            file_data_employee = read_json_employee()
            id_list = get_id_list(file_data_employee)
            date_index = get_date_index(file_data_attendance)

            print (f"Choose an ID {list(id_list)}")

            input_id = input()

            if input_id in list(id_list):
                for i in (file_data_attendance[date_index]["details"]):
                    if i['id']==input_id:
                        print(i)




                        
                


            


                    






                    
                                

                



            






            

