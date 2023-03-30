import view
import logic
import util

def main():
    while True:
        size = int(input("input size of list: "))
        if size > 0:
            break
        else:
            view.write("invalid data, try again")
    ls = util.create_list(size)

    #rnd_init_list(ls)
    util.user_init_list(ls)

    second = logic.find_second_max_value(ls)

    msg=f"Second max value {second}"
    view.write(ls)
    view.write(msg)

if __name__ == "__main__":
    main()
