# Tic-Tac-Toe game player vs player.
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-tac-Toe")

# x starts so true
clicked = True
count = 0


# game logic.

def reset():
    global clicked, count
    clicked = True
    count = 0
    for button in buttons:
        button["text"] = " "


count1 = 0


def check_tie(count1):
    for button in buttons:
        count1 += 1
        if button["text"] == "X" or "O":
            if count != 9:
                return False
            else:
                if check_win != "X" and "O":
                    return True
                else:
                    return False


def check_win():
    # check rows
    for i in range(0, 9, 3):
        if buttons[i]["text"] == buttons[i + 1]["text"] == buttons[i + 2]["text"] != " ":
            return True

    # check columns
    for i in range(3):
        if buttons[i]["text"] == buttons[i + 3]["text"] == buttons[i + 6]["text"] != " ":
            return True

    # check diagonals
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != " ":
        return True
    elif buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != " ":
        return True

    return False


# Button clicking
def b_click(button):
    global clicked, count
    # print(count)
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1

        if check_win():
            messagebox.showinfo("Tic-Tac-toe", "X wins!")
            # for i in winning_indices:
            #     buttons[i].config(bg='green')
            # messagebox.showinfo("Tic-Tac-toe", "X wins!")
            reset()
        elif check_tie(count1):
            messagebox.showinfo("Tic-Tac-toe", "Tie game!")
            reset()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        if check_win():
            # for i in winning_indices:
            #     buttons[i].config(bg='green')
            messagebox.showinfo("Tic-Tac-toe", "O wins!")
            reset()
        elif check_tie(count1):
            messagebox.showinfo("Tic-Tac-toe", "Tie game!")
            reset()
    else:
        messagebox.showerror("Tic-Tac-toe", "That box has already been selected.\n Play at another box.")


buttons = []


def create_buttons():
    global buttons
    for i in range(9):
        button = Button(root, text=" ", font=('consolas', 30), width=3, height=3, bg="white",
                        command=lambda i=i: b_click(buttons[i]))
        button.grid(row=int(i / 3), column=i % 3)
        buttons.append(button)


create_buttons()

root.mainloop()
