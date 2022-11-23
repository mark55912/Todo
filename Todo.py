import getpass
NAME = getpass.getuser()


def lets_get_started():
    print('"new" - New')
    print('"delete" - Delete')
    print('"list" - List')
    print('"quit" - Quit')

    my_list = []
    while True:
        question = input("What would you like to do? ")
        ############ QUIT ###############
        if question == "quit":
            break
        ############ NEW ##################
        if question == "new":
            n = input("Enter new todo: ")
            my_list.append(n)
        ############# LIST ################
        if question == "list":
            temp_list = []
            with open(f"/home/{NAME}/.todo.txt", "r") as f:
                for line in f:
                    x = line[:-1]
                    temp_list.append(x)
            for i in range(len(temp_list)):
                print(f"{i}: {temp_list[i]}")
            temp_list.clear()
        ############## DELETE #################
        if question == "delete":
            temp_list = []
            with open(f"/home/{NAME}/.todo.txt", "r") as f:
                for line in f:
                    x = line[:-1]
                    temp_list.append(x)
            for i in range(len(temp_list)):
                print(f"{i}: {temp_list[i]}")
            temp_list.clear()
            ##############################

            d = int(input("Which number delete? "))

            new_list = []
            with open(f"/home/{NAME}/.todo.txt", "r") as f:
                for line in f:
                    x = line[:-1]
                    new_list.append(x)
            del new_list[d]
            with open(f"/home/{NAME}/.todo.txt", "w") as f:
                for new in new_list:
                    f.write(new + '\n')
                my_list.clear()

        ############# APPEND #################
        with open(f"/home/{NAME}/.todo.txt", "a") as f:
            for my in my_list:
                f.write(my + '\n')
            my_list.clear()
    print("Looks like you want to quit.")


def main():
    lets_get_started()


if __name__ == '__main__':
    main()
