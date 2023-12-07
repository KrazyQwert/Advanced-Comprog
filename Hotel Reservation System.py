class Hotel:
    def __init__(self):
        self.room_no = 0
        self.name = ""
        self.address = ""
        self.phone = ""

    def main_menu(self):
        choice = 0
        while choice != 5:
            print("\n\t\t\t\t*************************")
            print("\n\t\t\t\t SIMPLE HOTEL MANAGEMENT ")
            print("\n\t\t\t\t      * MAIN MENU *")
            print("\n\t\t\t\t*************************")
            print("\n\n\n\t\t\t1.Book A Room")
            print("\t\t\t2.Customer Records")
            print("\t\t\t3.Rooms Allotted")
            print("\t\t\t4.Edit Record")
            print("\t\t\t5.Exit")
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

    def add(self):
        flag = 0
        with open("Record.dat", "a") as fout:
            print("\n Enter Customer Details")
            print("\n ----------------------")
            print("\n\n Room no: ")
            print("\n Total no. of Rooms - 60")
            print("\n Ordinary Rooms from 1 - 20")
            print("\n Luxury Rooms from 21 - 40")
            print("\n Royal Rooms from 41 - 60")
            r = int(input("\n Enter The Room no. you want to stay in :- "))
            flag = self.check(r)

            if flag:
                print("\n Sorry..!!! Room is already booked")
            else:
                self.room_no = r
                self.name = input(" Name: ")
                self.address = input(" Address: ")
                self.phone = input(" Phone No: ")
                fout.write(f"{self.room_no},{self.name},{self.address},{self.phone}\n")
                print("\n Room is booked...!!!")

        print("\n Press any key to continue.....!!")
        input()

    def display(self):
        r = int(input("\n Enter room no. for a particular customer's details :- "))
        with open("Record.dat", "r") as fin:
            found = False
            for line in fin:
                data = line.split(',')
                if int(data[0]) == r:
                    print("\n Customer Details")
                    print("\n ----------------")
                    print(f"\n\n Room no: {data[0]}")
                    print(f" Name: {data[1]}")
                    print(f" Address: {data[2]}")
                    print(f" Phone no: {data[3]}")
                    found = True
                    break

            if not found:
                print("\n Sorry Room no. not found or vacant....!!")
            print("\n\n Press any key to continue....!!")
            input()

    def rooms(self):
        print("\n\t\t\t    List Of Rooms Allotted")
        print("\n\t\t\t    ----------------------")
        print("\n\n Room No.\tName\t\tAddress\t\t\t\tPhone No.\n")
        with open("Record.dat", "r") as fin:
            for line in fin:
                data = line.split(',')
                print(f"\n\n {data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}")

        print("\n\n\n\t\t\tPress any key to continue.....!!")
        input()

    def edit(self):
        choice = int(input("\n EDIT MENU\n ---------\n\n 1.Modify Customer Record\n 2.Delete Customer Record\n 3. Bill Of Customer\n Enter your choice: "))
        r = int(input("\n Enter room no: "))
        if choice == 1:
            self.modify(r)
        elif choice == 2:
            self.delete_rec(r)
        elif choice == 3:
            self.bill(r)
        else:
            print("\n Wrong Choice.....!!")
        print("\n Press any key to continue....!!!")
        input()

    def check(self, r):
        flag = False
        with open("Record.dat", "r") as fin:
            for line in fin:
                data = line.split(',')
                if int(data[0]) == r:
                    flag = True
                    break
        return flag

    def modify(self, r):
        flag = False
        with open("Record.dat", "r") as file:
            lines = file.readlines()
        with open("Record.dat", "w") as file:
            for line in lines:
                data = line.split(',')
                if int(data[0]) == r:
                    print("\n Enter New Details")
                    print("\n -----------------")
                    self.name = input(" Name: ")
                    self.address = input(" Address: ")
                    self.phone = input(" Phone no: ")
                    file.write(f"{r},{self.name},{self.address},{self.phone}\n")
                    print("\n Record is modified....!!")
                    flag = True
                else:
                    file.write(line)
        if not flag:
            print("\n Sorry Room no. not found or vacant...!!")

    def delete_rec(self, r):
        flag = False
        lines = []
        with open("Record.dat", "r") as fin:
            for line in fin:
                data = line.split(',')
                if int(data[0]) == r:
                    print("\n Name: ", data[1])
                    print(" Address: ", data[2])
                    print(" Phone No: ", data[3])
                    ch = input("\n\n Do you want to delete this record(y/n): ")
                    if ch.lower() == 'n':
                        lines.append(line)
                    flag = True
                else:
                    lines.append(line)
        with open("Record.dat", "w") as fout:
            fout.writelines(lines)

        if not flag:
            print("\n Sorry room no. not found or vacant...!!")
        else:
            print("\n Record deleted successfully!")

    def bill(self, r):
        found = False
        with open("Record.dat", "r") as f1:
            for line in f1:
                data = line.split(',')
                if int(data[0]) == r:
                    if 1 <= int(data[0]) <= 20:
                        print("Your bill = 2000")
                    elif 21 <= int(data[0]) <= 40:
                        print("Your bill = 5000")
                    elif 41 <= int(data[0]) <= 60:
                        print("Your bill = 7000")
                    found = True
                    break
        if not found:
            print("Room no. not found")
        input("Press any key to continue...")

if __name__ == "__main__":
    h = Hotel()
    print("\n\t\t\t****************************")
    print("\n\t\t\t* HOTEL RESERVATION SYSTEM *")
    print("\n\t\t\t****************************")
    print("\n\t\t\t\t\t BSIT-2101")
    print("\n\n\n\t\t\tPress any key to continue....!!")
    input()

    h.main_menu(
    )