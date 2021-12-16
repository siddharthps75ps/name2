import json
from filename import FileName

fl = FileName()





class DeleteEmployee:
    

    def choice3_func():

        def list_of_employees_id(data_as_list):
                employee_ids = []
                length = len(data_as_list['employee_details'])

                for i in range(length):
                    employee_ids.append(data_as_list['employee_details'][i]['Employee_ID'])

                return employee_ids


        def read_from_json():
            with open('sample2.json','r') as access_json:
                data = json.load(access_json)
                access_json.close()

            return data
        

        
        def find_position(employee_ids,id):
            
            position = employee_ids.index(id)
            return position
        
            
        




        


        data_as_list = read_from_json()
        employee_ids = list_of_employees_id(data_as_list)
        print(f'Registered Employee IDs are: {employee_ids}')
        id_to_delete = input("Enter Employee ID to delete")

        if id_to_delete in employee_ids:

            position = find_position(employee_ids,id_to_delete)
            to_remove = data_as_list['employee_details'][position]
            data_as_list['employee_details'].remove(to_remove)

            data = json.dumps(data_as_list,indent=4)
            with open('sample2.json','w') as outfile:
                outfile.write(data)
                outfile.close()






