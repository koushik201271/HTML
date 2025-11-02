from colorama import Fore, Style, init
import time
import statistics

init(autoreset=True)

student = []

def header(text):
    print(Fore.CYAN + "\n" + "=" *60)
    print(Fore.CYAN +f" {text.center(60)}")
    print(Fore.CYAN + "=" * 60)

def pause():
    input(Fore.YELLOW + "\n Press Enter to continue...")
       

def show_menu():
    header("Student Data Manager - Main Menu") 
    print(Fore.Yellow + "1. Add New Student")
    print("2. Diaply All Students")
    print("3. Scarch Student by ID")
    print("4. Uplode Student Record")
    print("5. Delete Student")
    print("6. Analyze Student Performance")
    print("7. Srot Students by Data")
    print("8. Export student List (Prweview Only)")
    print("9. Exit")
    print(Fore.CYAN + "=" * 60)

def add_student():
        header("ADD NEW STUDENT")
        try:
            sid = input(Fore.YELLOW + "Enter Student ID:").strip()
            name = input("Enter Student Name: ").strip()
            age = int(input("Enter Age: "))
            grade = input("Enter Grade (A/B/C/D/F): ").upper().strip()
            marks = float(input("Enter Average Marks: "))
            student = (sid, name, age, grade, marks)
            student.append(student)
            print(Fore.GREEN + f"\n student '{name}' added succesfully.")
        except ValueError:
                print(Fore.RED + "Invaild input! please enter numeric value where required.")
                pause()
                def display_all():
    header("ALL STUDENT RECORDS")
    if not students:
        print(Fore.RED + "No student records available.")
    else:
        print(Fore.CYAN + f"{'ID':<10}{'Name':<20}{'Age':<10}{'Grade':<10}{'Marks':<10}")
        print(Fore.CYAN + f"{'-' * 60}")
        for s in students:
            print(Fore.GREEN + f"{s[0]:<10}{s[1]:<20}{s[2]:<10}{s[3]:<10}{s[4]:<10.2f}")
        pause()

def search_student():
    header("SEARCH STUDENT BY ID")
    sid = input(Fore.YELLOW + "Enter Student ID to Search: ").strip()
    found = False
    for s in students:
        if s[0] == sid:
            print(Fore.GREEN + f"\nRecord Found:\nID: {s[0]}\nName: {s[1]}\nAge: {s[2]}\nGrade: {s[3]}\nMarks: {s[4]}")
            found = True
            break
    if not found:
        print(Fore.RED + "Student not found.")
    pause()

def update_student():
    header("UPDATE STUDENT DETAILS")
    sid = input(Fore.YELLOW + "Enter Student ID to Update: ").strip().upper()

    for i, s in enumerate(students):
        if s[0] == sid:
            print(Fore.GREEN + f"\nCurrent Record: {s}")

            try:
                name_input = input(Fore.WHITE + "Enter New Name (leave blank to keep current): ").strip()
                name = name_input.title() if name_input else s[1]

                age_input = input(Fore.WHITE + "Enter New Age (leave blank to keep current): ").strip()
                age = int(age_input) if age_input else s[2]
                

                grade_input = input(Fore.WHITE + "Enter New Grade (A/B/C/D/F) (leave blank): ").strip()
                grade = grade_input.upper() if grade_input else s[3]
                

                marks_input = input(Fore.WHITE + "Enter New Marks (leave blank to keep current): ").strip()
                marks = float(marks_input) if marks_input else s[4]


                students[i] = [s[0], name, age, grade, marks] 
                
                print(Fore.GREEN + "\nRecord updated successfully.")
            
            except ValueError:
                print(Fore.RED + "Invalid input (e.g., non-number for Age/Marks). Update aborted.")
            
            break
    else:
        print(Fore.RED + f"Student with ID {sid} not found.")

    pause()


def delete_student():
    header("DELETE STUDENT RECORD")
    sid = input(Fore.YELLOW + "Enter Student ID to Delete: ").strip().upper()
    
    for s in students:
        if s[0] == sid: 
            students.remove(s)
            print(Fore.GREEN + f"Student '{s[1]}' deleted successfully.")
            break
    else:
        print(Fore.RED + "Student not found.")
    
    pause()


def analyze_performance():
    header("CLASS PERFORMANCE ANALYSIS")
    if not students:
        print(Fore.RED + "No data to analyze.")
    else:
        marks_list = [s[4] for s in students]

        print(Fore.GREEN + f"Total Students: {len(students)}")
        print(Fore.GREEN + f"Highest Marks: {max(marks_list):.2f}")
        print(Fore.GREEN + f"Lowest Marks: {min(marks_list):.2f}")
        print(Fore.GREEN + f"Average Marks: {statistics.mean(marks_list):.2f}")
        
        top_marks = max(marks_list)
        top_students = [s for s in students if s[4] == top_marks]

        print(Fore.CYAN + "\nTop Performer(s):")
        for t in top_students:
            print(Fore.GREEN + f"- {t[1]} ({t[4]:.2f} Marks, Grade {t[3]})")
    
    pause()

def sort_students():
    header("SORT STUDENT DATA")
    print(Fore.WHITE + "1. Sort by Name")
    print(Fore.WHITE + "2. Sort by Marks (Descending)")
    print(Fore.WHITE + "3. Sort by Grade")
    
    choice = input(Fore.YELLOW + "Choose sorting method (1/2/3): ").strip()

    if choice == "1":
        
        students.sort(key=lambda s: s[1])
    elif choice == "2":

        students.sort(key=lambda s: s[4], reverse=True)
    elif choice == "3":

        students.sort(key=lambda s: s[3])
    else:
        print(Fore.RED + "Invalid option.")
        pause()
        return

    print(Fore.GREEN + "Data sorted successfully! Displaying results:")
    display_all()

def export_preview():
    header("EXPORT STUDENT DATA (PREVIEW)")
    if not students:
        print(Fore.RED + "No records to export.")
    else:
        print(Fore.YELLOW + "ID,Name,Age,Grade,Marks")
        
        for s in students:
            print(Fore.WHITE + f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]:.2f}")
        
        print(Fore.GREEN + "\nData is ready for copy/paste into a CSV file.")
    
    pause()



def main():
    header("WELCOME TO STUDENT DATA MANAGER SYSTEM")
    time.sleep(0.5)

    while True:
        show_menu()
        choice = input(Fore.YELLOW + "Enter your choice (1-9): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            analyze_performance()
        elif choice == "7":
            sort_students()
        elif choice == "8":
            export_preview()
        elif choice == "9":

            print(Fore.CYAN + "\nExiting System... Thank you!")
            break
        else:

            print(Fore.RED + "Invalid input. Please choose from 1 to 9.")
            time.sleep(1)

if __name__ == "__main__":
    main()