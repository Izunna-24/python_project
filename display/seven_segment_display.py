
def show_zero():
    return """
        # # # #
        #     #
        #     #
        #     #
        # # # #
            """


def show_one():
    return """
              #
              #
              #
              #
              #
            """


def show_two():
    return """
        # # # #
              #
        # # # #
        #     
        # # # #
            """


def show_three():
    return """
        # # # #
              #
        # # # #
              #
        # # # #
            """


def show_four():
    return """
        #     #
        #     #
        # # # #
              #
              #
            """


def show_five():
    return """
        # # # #
        #     
        # # # #
              #
        # # # #
            """


def display_segment_6():
    return """
        # # # #
        #     
        # # # #
        #     #
        # # # #
            """


def show_seven():
    return """
        # # # #
              #
              #
              #
              #
            """


def show_eight():
    return """
        # # # #
        #     #
        # # # #
        #     #
        # # # #
            """


def show_nine():
    return """
        # # # #
        #     #
        # # # #
              #
        # # # #
            """


def show_seven_segment(user_input: str):
    match user_input:
        case "11111100":
            return show_zero()

        case "01100000":
            return show_one()

        case "11011010":
            return show_two()

        case "11110010":
            return show_three()

        case "01100110":
            return show_four()

        case "10110110":
            return show_five()

        case "10111110":
            return display_segment_6()

        case "11100000":
            return show_seven()

        case "11111110":
            return show_eight()

        case "11100110":
            return show_nine()



