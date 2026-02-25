from tkinter import *
from tkinter import messagebox

# 도서:저자 저장용 딕셔너리
books = {}

def update_listbox():
    """리스트박스 내용을 최신 상태로 갱신"""
    listbox.delete(0, END)
    for title, author in books.items():
        listbox.insert(END, f"{title} - {author}")

def add_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()

    if title == "" or author == "":
        messagebox.showinfo("결과", "도서명과 저자명을 모두 입력하세요.")
        return

    books[title] = author
    messagebox.showinfo("결과", f"'{title}' 도서가 추가되었습니다.")
    entry_title.delete(0, END)
    entry_author.delete(0, END)
    update_listbox()

def search_book():
    title = entry_title.get().strip()

    if title == "":
        messagebox.showinfo("검색 결과", "도서명을 입력하세요.")
        return

    if title in books:
        messagebox.showinfo("검색 결과", f"'{title}' 도서는 목록에 있으며 저자는 '{books[title]}' 입니다.")
    else:
        messagebox.showinfo("검색 결과", f"'{title}' 도서를 찾을 수 없습니다.")

def delete_book():
    title = entry_title.get().strip()

    if title == "":
        messagebox.showinfo("삭제 결과", "도서명을 입력하세요.")
        return

    if title in books:
        del books[title]
        messagebox.showinfo("삭제 결과", f"'{title}' 도서가 삭제되었습니다.")
        entry_title.delete(0, END)
        entry_author.delete(0, END)
        update_listbox()
    else:
        messagebox.showinfo("삭제 결과", f"'{title}' 도서는 목록에 없습니다.")

# 윈도우 생성
root = Tk()
root.geometry("350x380")
root.title("도서 관리 프로그램 (도서/저자 딕셔너리 버전)")

# 도서명 입력
Label(root, text="도서명").pack()
entry_title = Entry(root, width=30)
entry_title.pack(pady=5)

# 저자명 입력
Label(root, text="저자명").pack()
entry_author = Entry(root, width=30)
entry_author.pack(pady=5)

# 버튼 3개
btn_add = Button(root, text="도서 추가하기", width=15, command=add_book)
btn_add.pack(pady=3)

btn_search = Button(root, text="도서 검색하기", width=15, command=search_book)
btn_search.pack(pady=3)

btn_delete = Button(root, text="도서 삭제하기", width=15, command=delete_book)
btn_delete.pack(pady=3)

# 리스트박스 추가
listbox = Listbox(root, width=45, height=10)
listbox.pack(pady=10)

root.mainloop()
