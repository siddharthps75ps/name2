from choices.add_employee import AddEmployee
from choices.edit_employee import EditEmployee
from choices.delete_employee import DeleteEmployee
from choices.add_attendance import AddAttendance



class MainChoice:

    def select_choice(self, ch):

        if ch==1:
            ob=AddEmployee
            ob.choice1_func()

        elif ch==2:
            ob=EditEmployee
            ob.choice2_func()

        elif ch==3:
            ob=DeleteEmployee
            ob.choice3_func()

        elif ch==4:
            ob=AddAttendance
            ob.choice4_func()

        

        
            
        

