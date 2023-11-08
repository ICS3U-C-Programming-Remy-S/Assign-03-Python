#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 15, 2023
# This program will ask the user
# for their a and y coordinates
# and it will tell them what quadrant or axis they
# are on with try catch


def main():
    # Get the user x and y as a string and display message about program
    print("This program will ask the user for their a and y coordinates and it")
    print("will tell them what quadrant or axis they are on.")
    user_x_str = input("Please enter your x coordinate: ")
    user_y_str = input("Please enter your y coordinate: ")

    # Catch if the user x is something invalid
    try:
        # Convert user x as a string to int
        user_x_int = int(user_x_str)

        try:
            # Convert user x as a string to int
            user_y_int = int(user_y_str)

            if user_x_int > 0 and user_y_int > 0:
                # Message for top right quadrant
                print(
                    "\n({}, {}) are in the top right quadrant.".format(
                        user_x_str, user_y_str
                    )
                )

            elif user_x_int > 0 and user_y_int < 0:
                # Message for bottom right quadrant
                print(
                    "\n({}, {}) are in the bottom right quadrant.".format(
                        user_x_str, user_y_str
                    )
                )

            elif user_x_int < 0 and user_y_int > 0:
                # Message for top left quadrant
                print(
                    "\n({}, {}) are in the top left quadrant.".format(
                        user_x_str, user_y_str
                    )
                )

            elif user_x_int == 0 and user_y_int == 0:
                # Message for origin point
                print(
                    "\n({}, {}) are at the origin point.".format(user_x_str, user_y_str)
                )

            # messages for axis points
            elif user_x_int == 0 or user_y_int == 0:
                if user_x_int == 0 and user_y_int > 0:
                    # Message for top y-axis point
                    print(
                        "\n({}, {}) are on top y-axis.".format(user_x_str, user_y_str)
                    )

                elif user_x_int == 0 and user_y_int < 0:
                    # Message for bottom y-axis
                    print(
                        "\n({}, {}) are on bottom y-axis.".format(
                            user_x_str, user_y_str
                        )
                    )

                elif user_x_int > 0 and user_y_int == 0:
                    # Message for top x-axis
                    print(
                        "\n({}, {}) are on top x-axis.".format(user_x_str, user_y_str)
                    )

                else:
                    # Message for bottom x-axis
                    print(
                        "\n({}, {}) are on bottom x-axis.".format(
                            user_x_str, user_y_str
                        )
                    )
            else:
                # Message for bottom left quadrant
                print(
                    "\n({}, {}) are on bottom left quadrant.".format(
                        user_x_str, user_y_str
                    )
                )

        # Display a message to the user if they entered a y that is not valid
        except Exception:
            # Message for invalid user input
            print(
                "\n({}, {}) are not a valid coordinates.".format(user_x_str, user_y_str)
            )

    # Display a message to the user if they entered a x that is not valid
    except Exception:
        # Message for invalid user input
        print("\n({}, {}) are not a valid coordinates.".format(user_x_str, user_y_str))


if __name__ == "__main__":
    main()
