#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on April 2022
# This is the math program, showing whether your age is acceptable for the date


def main():
    # This function compares your age and the command

    # input
    age = input("Please enter your age: ")

    # process & output
    print("")
    try:
        age_int = int(age)
        if age_int > 25 and age_int < 40:
            print("You are an acceptable age.")
        else:
            print("You are not an acceptable age!")
    except Exception:
        print("{} is not a valid answer!".format(age))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
