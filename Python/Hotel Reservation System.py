class Hotel:
    # ... (your existing code)

    def main_menu(self):
        choice = 0
        while choice != 5:
            print("\n\t\t\t\t*************************")
            print("\n\t\t\t\t SIMPLE HOTEL MANAGEMENT ")
            print("\n\t\t\t\t      * MAIN MENU *")
            print("\n\t\t\t\t*************************")

            # ASCII art for a simple hotel image
            print("\n\t\t\t\t    __|__")
            print("\t\t\t\t---o0o---")

            print("\n\n\n\t\t\t1. Book A Room")
            print("\t\t\t2. Customer Records")
            print("\t\t\t3. Rooms Allotted")
            print("\t\t\t4. Edit Record")
            print("\t\t\t5. Exit")
            print("\n\n\t\t\tEnter Your Choice: ")
            choice = int(input())

            if choice == 1:
                self.add()
            elif choice == 2:
                self.display()
            elif choice == 3:
                self.rooms()
            elif choice == 4:
                self.edit()
            elif choice == 5:
                break
            else:
                print("\n\n\t\t\tWrong choice.....!!!")
                print("\n\t\t\tPress any key to continue....!!")
                input()

    # ... (your existing code)


if __name__ == "__main__":
    h = Hotel()
    print("\n\t\t\t****************************")
    print("\n\t\t\t* HOTEL RESERVATION SYSTEM *")
    print("\n\t\t\t****************************")
    print("\n\t\t\t\t\t BSIT-2101")
    print("\n\n\n\t\t\tPress any key to continue....!!")
    input()

    h.main_menu()
