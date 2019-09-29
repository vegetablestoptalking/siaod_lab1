# TESTING
from LinkedList import List as own_list
from Stack import Stack as own_stack
from Queue import Queue as qu
from tkinter import *
from tkinter import scrolledtext

arr = own_list()
st = own_stack()
queue = qu(1, 4)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)

arr.append_from(["hello", "my", "big", "hell", "looking", "hearth", "", "how"])


def strings_count(arr):
    count = 0
    if len(arr[len(arr) - 1]) != 0:
        char = arr[len(arr) - 1][0]
    else:
        return count

    for i in range(len(arr)):
        # description: we add one if our element is not an !!! empty string(lambda) !!!
        # or return the same count if the condition is not met
        # lambda: we check is string empty, cause otherwise it can fall
        count = count + 1 if char == (lambda mas: mas[0] if len(mas) != 0 else "")(
            arr[i]) else count  # IT WORKS AAAAAAAAA

    return count


def stack_sum(st):
    sum = 0
    for i in range(len(st)):
        sum += st[i]
    return sum


def append_list():
    arr.append(txt.get())


def append_stack():
    st.push(txt.get())


def append_queue():
    queue.enqueue(txt.get())


def clear_all():
    arr = own_list()
    st = own_stack()
    queue = qu(1, 4)
    scr.delete(1.0, END)


def print_list():
    scr.insert(INSERT, '-----------ЛИСТ----------\n')
    scr.insert(INSERT, str(arr) + '\n')
    scr.insert(INSERT, '-------------------------\n')


def print_q():
    scr.insert(INSERT, '---------ОЧЕРЕДЬ---------\n')
    scr.insert(INSERT, str(queue) + '\n')
    scr.insert(INSERT, '-------------------------\n')


def print_st():
    scr.insert(INSERT, '-----------СТЭК----------\n')
    scr.insert(INSERT, str(st) + '\n')
    scr.insert(INSERT, '-------------------------\n')


window = Tk()
window.title("Лабораторная работа 1")
window.geometry('800x350')
txt = Entry(window, width=30)
txt.grid(column=1, row=3)
scr = scrolledtext.ScrolledText(window, width=40, height=10)
scr.grid(column=1, row=0)
btn_add_ls = Button(window, text="Добавить элемент в лист", command=append_list)
btn_add_ls.grid(column=3, row=0)
btn_add_st = Button(window, text="Добавить элемент в стэк", command=append_stack)
btn_add_st.grid(column=3, row=1)
btn_add_qu = Button(window, text="Добавить элемент в очередь", command=append_queue)
btn_add_qu.grid(column=3, row=2)
btn_clear = Button(window, text="Очистить всё", command=clear_all)
btn_clear.grid(column=0, row=1)
btn_print_list = Button(window, text="Распечатать лист", command=print_list)
btn_print_list.grid(column=0, row=2)
btn_print_queue = Button(window, text="Распечатать очередь", command=print_q)
btn_print_queue.grid(column=0, row=3)
btn_print_stack = Button(window, text="Распечатать стэк", command=print_st)
btn_print_stack.grid(column=0, row=4)
window.mainloop()
