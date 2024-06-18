import tkinter as tk
from tkinter import messagebox

class RepairRequest:
    def __init__(self, name, contact_info, repair_type, description):
        self.name = name
        self.contact_info = contact_info
        self.repair_type = repair_type
        self.description = description
        self.status = "Pending"  # Начальный статус заявки

    def __str__(self):
        return f"Заявка от {self.name} на {self.repair_type}.\nСтатус: {self.status}"

    def mark_completed(self):
        self.status = "Completed"
        messagebox.showinfo("Заявка завершена", f"Заявка на {self.repair_type} от {self.name} завершена.")

class RepairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система заявок на ремонт")
        self.root.geometry("300x200")  # Установка размеров главного окна

        self.requests = []

        # Создание элементов интерфейса
        self.label = tk.Label(root, text="Выберите действие:")
        self.label.pack(pady=10)

        self.button_new = tk.Button(root, text="Создать новую заявку", command=self.create_request)
        self.button_new.pack()

        self.button_show = tk.Button(root, text="Показать все заявки", command=self.show_requests)
        self.button_show.pack()

        self.button_complete = tk.Button(root, text="Завершить заявку", command=self.complete_request)
        self.button_complete.pack()

        self.button_exit = tk.Button(root, text="Выйти", command=root.quit)
        self.button_exit.pack()

    def create_request(self):
        # Окно для создания новой заявки
        top = tk.Toplevel(self.root)
        top.title("Новая заявка")
        top.geometry("400x300")  # Установка размеров окна создания заявки

        tk.Label(top, text="Имя:").pack()
        name_entry = tk.Entry(top)
        name_entry.pack()

        tk.Label(top, text="Контактная информация:").pack()
        contact_entry = tk.Entry(top)
        contact_entry.pack()

        tk.Label(top, text="Тип ремонта:").pack()
        repair_entry = tk.Entry(top)
        repair_entry.pack()

        tk.Label(top, text="Описание проблемы:").pack()
        desc_entry = tk.Entry(top)
        desc_entry.pack()

        def submit_request():
            name = name_entry.get()
            contact_info = contact_entry.get()
            repair_type = repair_entry.get()
            description = desc_entry.get()

            request = RepairRequest(name, contact_info, repair_type, description)
            self.requests.append(request)
            messagebox.showinfo("Заявка создана", "Заявка успешно создана.")
            top.destroy()

        submit_button = tk.Button(top, text="Отправить заявку", command=submit_request)
        submit_button.pack()

    def show_requests(self):
        # Окно для отображения всех заявок
        if not self.requests:
            messagebox.showinfo("Список заявок", "Нет заявок для отображения.")
        else:
            top = tk.Toplevel(self.root)
            top.title("Список заявок")
            top.geometry("600x400")  # Установка размеров окна списка заявок

            for idx, req in enumerate(self.requests, start=1):
                tk.Label(top, text=f"{idx}. {req}").pack()

    def complete_request(self):
        # Окно для завершения заявки
        if not self.requests:
            messagebox.showinfo("Завершение заявки", "Нет заявок для завершения.")
        else:
            top = tk.Toplevel(self.root)
            top.title("Завершить заявку")
            top.geometry("400x300")  # Установка размеров окна завершения заявки

            tk.Label(top, text="Выберите заявку для завершения:").pack()
            for idx, req in enumerate(self.requests, start=1):
                tk.Label(top, text=f"{idx}. {req}").pack()

            req_index_entry = tk.Entry(top)
            req_index_entry.pack()

            def complete():
                try:
                    req_index = int(req_index_entry.get()) - 1
                    if 0 <= req_index < len(self.requests):
                        self.requests[req_index].mark_completed()
                        top.destroy()
                    else:
                        messagebox.showerror("Ошибка", "Некорректный номер заявки.")
                except ValueError:
                    messagebox.showerror("Ошибка", "Введите номер заявки.")

            complete_button = tk.Button(top, text="Завершить", command=complete)
            complete_button.pack()

# Создание главного окна приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = RepairApp(root)
    root.mainloop()

