# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


import os.path as path

DATA_DIR = path.join(path.abspath(''), 'data')


def parse_table_file(file_name):
    table_parsed = []
    with open(path.join(DATA_DIR, file_name), 'r', encoding="utf8") as file:
        next(file)
        for line in file:
            if len(line) == 0:
                continue
            row = [x for x in line.rstrip().split(' ') if len(x) > 0]
            table_parsed.append(row)
    return table_parsed


class Employee:
    def __init__(self, table_row: str):
        f_name, l_name, salary, position, hours_capacity = table_row
        self.f_name = f_name
        self.l_name = l_name
        self.salary = int(salary)
        self.position = position
        self.hours_capacity = int(hours_capacity)


class TimeSheetRecord:
    def __init__(self, table_row: str):
        f_name, l_name, hours = table_row
        self.f_name = f_name
        self.l_name = l_name
        self.hours = int(hours)


class PayrollRec:
    def __init__(self, employee, timesheet_rec):
        self.employee = employee
        self.t_rec = timesheet_rec
        self.payout = PayrollRec.calc_payout(timesheet_rec.hours, employee.hours_capacity)

    @staticmethod
    def calc_payout(hours=0, hours_capacity=160):
        payroll = 1
        payout_k = hours / hours_capacity
        if payout_k < 1:
            payroll *= payout_k
        elif payout_k > 1:
            payroll *= (1 + (payout_k - 1) * 2)
        return round(payroll, 4)


class Accountancy:
    def __init__(self, workers_file_name, timesheet_file_name):
        self.workers_file_name = workers_file_name
        self.timesheet_file_name = timesheet_file_name
        self.payroll = []

    def calculate_payrolls(self):
        employees = list(map(Employee, parse_table_file(self.workers_file_name)))
        timesheet = list(map(TimeSheetRecord, parse_table_file(self.timesheet_file_name)))

        payroll = []

        for employee in employees:
            timesheet_rec = next(x for x in timesheet if x.f_name == employee.f_name and x.l_name == employee.l_name)
            if timesheet_rec is not None:
                payroll.append(PayrollRec(employee, timesheet_rec))

        self.payroll = payroll
        return self.payroll

    def print_payroll(self):
        for p in self.payroll:
            print('{} {} {}/{} {}/{}'.format(p.employee.f_name, p.employee.l_name, p.t_rec.hours, p.employee.hours_capacity, p.payout, p.employee.salary))


acc = Accountancy('workers', 'hours_of')
acc.calculate_payrolls()
acc.print_payroll()
