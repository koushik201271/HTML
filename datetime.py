import detetime 
import calender


def print_menu():
    print("\nDate & Calender utility")
    print("1. Show today's date")
    print("2. Calender days between two dates")
    print("3. Show calender for a month")
    print("4. Show current time of Netrokona")
    print("5. Show weekdays")
    print("6. Calculate age from birthdate")
    print("7. Days remaining to next year")
    print("8. check if a year is leap year")
    print("9. Show next holliday (demo)")
    print("10. Exit")

    def Show_today_():
        today = detetime.date.today()
        print(f"Today's date :, {today}")

    def days_between():
        d1 = input("Enter first date (YYYY-MM-DD): ")
        d2 = input("Enter second date (YYYY-MM-DD): ")
        try:
            data1 = detetime.datetime.strptime(d1, "%Y-%m-%d").data()
            data2 = detetime.datetime.strptime(d2, "%Y-%m-%d").data()
            diff = abs((data2 - data1).days)
            print(f"Days between: {diff} ")
        except ValueError:
            print("Invalid date format.")

     def show_weekdays():
            d = input("Enter a date (YYYY-MM-DD): ")
            try:
                date_obj = detetime.datetime.strptime(d, "%Y-%m-%d").date()
                print(f"{d} is a:  [date_obj.strptime('%A')]")
        except ValueError:
                print("Invalid date format.")
    def show_month_calender():
        try:
            year = int(input("Enter year(e.g. 2025)"))
            month = int(input("Enter month (1-12):"))\
        except Exception:
            print("Invalid input.")
    def show_time():
        now = datetime.now(ZoneInfo("Asia/Netrokona"))
        print(f"Curent time is Netrokona: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    def calculate_age():
        dob_input = input("Enter your date of birth(YYYY-MM-DD):")
        try:
            dob = datetime.datetime.strftime(dob_input, "%Y-%m-%d").date()
            today = datetime.date.today()
            years = today.year - dob.year - ((today.month, today.day)<(dob.month, dob.day))
            month = (today.month - dob.month) % 12
            