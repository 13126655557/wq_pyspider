#encoding:UTF-8
import argparse
def demo1():
    parser = argparse.ArgumentParser()
    #parser.add_argument("echo")
    # type 设置入参数据类型
    parser.add_argument("echo", help="echo the string you use here",type=int)
    #--verbosity 可选参数  python argparse/argparse_demo.py 2 --verbosity 0
    #parser.add_argument("--verbosity", help="increase output verbosity")
    #-v 可选参数简写 python argparse/argparse_demo.py 2 --v 0
    #choices 设置参数选择区域
    parser.add_argument("-v","--verbosity", help="increase output verbosity",choices=[0,1,2],type=int)

    args = parser.parse_args()
    print '##############'
    print args.echo**2

    if args.verbosity:
        print "verbosity turned on"

def demo2():
    '''
    ➜  wq_pyspider git:(master) ✗ python argparse/argparse_demo.py 2 -v
2^2 == 4
➜  wq_pyspider git:(master) ✗
➜  wq_pyspider git:(master) ✗ python argparse/argparse_demo.py 2 -vv
the square of 2 equals 4
➜  wq_pyspider git:(master) ✗ python argparse/argparse_demo.py 2 -vvv
4
    action="count" 后这个参数可以根据输入的格式返回对应的count值
    :return:
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display the square of a given number")
    parser.add_argument("-v", "--verbosity", action="count",
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print "the square of {} equals {}".format(args.square, answer)
    elif args.verbosity == 1:
        print "{}^2 == {}".format(args.square, answer)
    else:
        print answer



def demo3():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.verbosity >= 2:
        print "Running '{}'".format(__file__)
    if args.verbosity >= 1:
        print "{}^{} ==".format(args.x, args.y),
    print answer


def demo4():
    '''
    -v -q 不可以同时使用
    :return:
    '''
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x ** args.y

    if args.quiet:
        print answer
    elif args.verbose:
        print "{} to the power {} equals {}".format(args.x, args.y, answer)
    else:
        print "{}^{} == {}".format(args.x, args.y, answer)




if __name__ == '__main__':
    demo4()