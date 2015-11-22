import sys
import ConfigParser
import os.path


def decide(penalty):
    if not os.path.isfile('MC_decision.ini'):
        temp = open('MC_decision.ini', 'w+')
        temp.write('[main]\nno = 0\n')
        temp.close()
    fp = open('MC_decision.ini', 'r+')
    cfg = ConfigParser.ConfigParser()
    cfg.read('MC_decision.ini')
    no = cfg.getint('main', 'no')
    penalty = str(penalty).replace('-', '')
    if no == 0:
        cfg.set('main', 'no', 1)
        cfg.write(fp)
        return 3
    elif no == 1:
        cfg.set('main', penalty, '%dhere' % 3)
        cfg.set('main', 'no', 2)
        cfg.write(fp)
        return 3
    else:
        temp = fp.read().replace('here', penalty)
        fp.seek(0)
        fp.truncate()
        fp.write(temp)
        fp.seek(0)
        cfg.read('MC_decision.ini')
        try:
            results_per_penalty = cfg.get('main', penalty)
            if len(results_per_penalty) == 2:
                return_list = [3, 2, 0, 1]
                return_list.remove(int(results_per_penalty[0]))
                cfg.set('main', penalty, '%s%dhere' % (results_per_penalty, return_list[0]))
                cfg.write(fp)
                fp.close()
                return return_list[0]
            elif len(results_per_penalty) == 4:
                rpp = [results_per_penalty[0:2], results_per_penalty[2:4]]
                return_list = [3, 2, 0, 1]
                return_list.remove(int(rpp[0][0]))
                return_list.remove(int(rpp[1][0]))
                cfg.set('main', penalty, '%s%dhere' % (results_per_penalty, return_list[0]))
                cfg.write(fp)
                return return_list[0]
            elif len(results_per_penalty) == 6:
                rpp = [results_per_penalty[0:2], results_per_penalty[2:4], results_per_penalty[4:6]]
                return_list = [3, 2, 0, 1]
                return_list.remove(int(rpp[0][0]))
                return_list.remove(int(rpp[1][0]))
                return_list.remove(int(rpp[2][0]))
                cfg.set('main', penalty, '%s%dhere' % (results_per_penalty, return_list[0]))
                cfg.write(fp)
                return return_list[0]
            elif len(results_per_penalty) == 8:
                rpp = [results_per_penalty[i:i+2] for i in range(0, len(results_per_penalty), 2)]
                returned_penalties = [rpp[0][1], rpp[1][1], rpp[2][1], rpp[3][1]]
                index_max = returned_penalties.index(max(returned_penalties))
                return rpp[index_max][0]
        except ConfigParser.NoOptionError:
            cfg.set('main', penalty, '%dhere' % 3)
            cfg.write(fp)
            return 3

print decide(9)

# uncoment this if you want to run in MATLAB with MC_decision.m script.
"""if __name__ == '__main__':
    x = int(sys.argv[1])
    sys.stdout.write(str(decide(x)))
    """
