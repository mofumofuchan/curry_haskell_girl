# coding:utf-8
import sys
import traceback


class EvalProblem(object):
    def __init__(self, data):
        self.data = data

    def eval(self):
        try:
            exec(self.data)
        except SyntaxError:
            # print('--------------------------------------------')
            # print(traceback.format_exc(sys.exc_info()[2]))
            # print('--------------------------------------------')
            return False
        except TypeError:
            # print('--------------------------------------------')
            # print(traceback.format_exc(sys.exc_info()[2]))
            # print('--------------------------------------------')
            return False
        else:
            return True
