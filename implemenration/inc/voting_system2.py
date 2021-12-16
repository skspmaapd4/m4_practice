 def welcome(obj):
        today = date.today()
        datetime = today.strftime("%B %d, %Y")
        # print("-----------------------------------------------------------------------")
        # print("                 Heritage Institute of Technology                 ")

    # print("          COLLEGE OF ENGINEERING AND INFORMATION TECHNOLOGY         ")
    # print("                   Alijis Campus - " + datetime + "                  ")
    # print("-----------------------------------------------------------------------")
    # print("************* Welcome to SSG Elections for S.Y. 2021-2022 *************")

    def loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(2)
        done = True

    def error_loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(5)
        done = True

    def loading_result(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rPlease wait while reading the result...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(8)
        done = True

    def registration(obj):

        while True:
            print("-----------------------------REGISTRATION-----------------------------")
            print("")
            obj.f_name = input("First name: ")
            obj.l_name = input("Last name: ")
            obj.course = input("State in: ")
            obj.year_section = input("Year : ")
            try:
                obj.stud_id = int(input("Voter's ID: "))
            except ValueError:
                print("Voter's ID should be an integer....re-enter with a valid number!")
                obj.stud_id = int(input("Voter's ID: "))

            if obj.stud_id in students_id:
                students_id.remove(obj.stud_id)
                obj.loading()
                print("Done!")
                print('-----------------------Registered Successfully!-----------------------')
                print("Name: " + obj.f_name + " " + obj.l_name)
                print("Course: State in " + obj.course)
                print("Year : " + obj.year_section)
                print("Voter's ID: " + str(obj.stud_id))
                obj.president()
                obj.vice_pres()
                obj.secretary()
                obj.auditor()
                obj.treasurer()
                obj.media_info()
                obj.first_yr_rep()
                obj.sec_yr_rep()
                obj.third_yr_rep()
                obj.fourth_yr_rep()
                break
            else:
                obj.error_loading()
                print("Done!")
                print("------------------ID existed. You have already voted!----------------")
                print("---------------------------PLEASE TRY AGAIN--------------------------\n")
