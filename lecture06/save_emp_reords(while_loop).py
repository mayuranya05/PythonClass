def main():

    num_emps = int(input('How many employee records ' + \
                         'do you want to create? '))
    
    emp_file = open('employees.txt', 'w')

    for count in range(1, num_emps + 1) :
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.writh(name + '\n')
        emp_file.writh(id_num + '\n')
        emp_file.writh(dept + '\n')

        print()

    emp_file.close()
    print('Employee records written to employees.txt')

main()