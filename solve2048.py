import sys
import copy
import terminaltables

steps = ['R', 'L', 'D', 'U']
rule = []
numrs = []
goal = 32768
case = 3

def create_rule(rule, rulestr):
    arr = rulestr.split(';')
    for n in range(0, len(arr)):
        idx = int(arr[n][:1], 16)
        val = arr[n][2:-1].split(',')
        for m in range(0, len(val)):
            if len(val[m]) == 1:
                rule[idx][0] = int(val[m], 16)
            else:
                lav = val[m].split(':')
                rule[idx][1].update({int(lav[1], 16) : int(lav[0], 16)})

def function(table, direction, number, case, goal, rule):
    ept = -1

    if 0 <= direction:
        x = 0
        y = 0
        lil_end = 0
        big_end = 3

        if direction == 0:
            x = 1
        elif direction == 1:
            x = -1
            lil_end = 3
            big_end = 0
        elif direction == 2:
            y = 1
        else:
            lil_end = 3
            big_end = 0
            y = -1

        for n in range(0, 4):
            for m in range(0, 4):
                if table[n][m] < 2:
                    table[n][m] = 0

        if y == 0:
            for n in range(0, 4):
                m = lil_end
                while m != big_end and m != big_end + x:
                    if table[n][m] == table[n][m + x] != 0:
                        table[n][m + x] *= 2

                        for i in range(m, lil_end, -x):
                            table[n][i] = table[n][i - x]
                        table[n][lil_end] = -1
                        ept += 1

                        m += x
                    m += x
        else:
            for n in range(0, 4):
                m = lil_end
                while m != big_end and m != big_end + y:
                    if table[m][n] == table[m + y][n] != 0:
                        table[m + y][n] *= 2

                        for i in range(m, lil_end, -y):
                            table[i][n] = table[i - y][n]
                        table[lil_end][n] = -1
                        ept += 1

                        m += y        
                    m += y
   
        insert = 2
        if len(case) > number and case[-(number + 1)] == '1':
            insert = 4
        
        if ept == -1:
            return False
        elif ept == 0:
            for n in range(0, 4):
                for m in range(0, 4):
                    if table[n][m] == -1:
                        table[n][m] = insert
                    elif table[n][m] == goal:
                        return ';'
        else:
            idx = 0
            if numrs[ept] in rule[ept][1]:
                idx = rule[ept][1][numrs[ept]]
            else:
                idx = rule[ept][0]
            
            for n in range(0, 4):
                for m in range(0, 4):
                    if table[n][m] == -1:
                        if idx == 0:
                            table[n][m] = insert
                        else:
                            table[n][m] = 0
                        idx -= 1
                    elif table[n][m] == goal:
                        return ';'

            numrs[ept] += 1

    for n in range(0, 4):
        route = function(copy.deepcopy(table), n, number + 1, case, goal, rule)
        if route:
            route = steps[n] + route
            return route
    
    return False

def main():
    global case, goal, rule, numrs
    fixed = 4
    num = -1
    table = []

    for n in range(0, 16):
        rule.append([0, {}])
        numrs.append(0)

    print('type table data (press Enter for default):')
    for n in range(0, 4):
        s = input()
        if s == '':
            table = [[32, 256, 512, 2048], [8, 128, 1024, 4096], [4, 64, 16384, 8192], [4, 8, 128, 256]]
            break
        table.append(list(map(int, s.split())))
    else:
        for n in range(0, 4):
            for m in range(0, 4):
                if table[n][m] > goal:
                    goal = table[n][m]
                elif table[n][m] < 2:
                    table[n][m] = 0
        goal *= 2
        fixed = 1
        case = 0

    print('input table:')
    fancytable = terminaltables.AsciiTable(table)
    fancytable.inner_row_border = True
    print(fancytable.table)

    file = False
    argc = int(len(sys.argv))
    for n in range(1, argc, 2):

        if sys.argv[n] == '-c':
            case = int(sys.argv[n + 1])

        elif sys.argv[n] == '-c0b':
            case = int(sys.argv[n + 1], 2)

        elif sys.argv[n] == '-o':
            file = open(sys.argv[n + 1], 'a')
            print('writing output data to file: %s' %file.name)

        elif sys.argv[n] == '-f':
            fixed = 2 ** int(sys.argv[n + 1])

        elif sys.argv[n] == '-n':
            num = int(sys.argv[n + 1])

        elif sys.argv[n] == '-r':
            rulestr = sys.argv[n + 1]
            create_rule(rule, rulestr)
            try:
                pass
            except:
                print('incorrect string format in option: "%s"' %rulestr)
                return

        else:
            print('Unknown option:', sys.argv[n])
            return

    n = 0
    while n != num:
        for m in range(0, 16):
            numrs[m] = 0

        route = function(copy.deepcopy(table), -1, -1, bin(case)[2:], goal, rule)

        out = str(case) + '=' + bin(case) + ':\n\t'
        if route:
            out += route[:-1] + '\n'
        else:
            out += "<Corresponding route does not exist>\n"
        
        if file:
            file.write(out)
            sys.stdout.write('\rcase = %d' %(case + fixed))
        else:
            sys.stdout.write(out)
        sys.stdout.flush()

        case += fixed
        n += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('')