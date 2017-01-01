# coding:utf-8
import sys
import traceback


def create_file():
    sys.stdout = open("tmp.txt", "w", encoding='utf-8')


def shake():
    print("シェイクしたよ！")


class EvalProblem(object):
    def __init__(self, id, src, database):
        self.id = id
        self.src = src
        self.db = database
        self.dbc = self.db.cursor()

    def eval(self):
        try:
            create_file()
            exec(self.src) # TODO セキュリティに考慮する
            sys.stdout.close()
            sys.stdout = sys.__stdout__
        except SyntaxError:
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            # TODO SyntaxErrorであると返すようにしたい
            return False, None
        except TypeError:
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            # TODO TypeErrorであると返すようにしたい
            return False, None
        except:
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            return False, None
        else:
            print(shake())
            tmp = self.dbc.execute("select quiz_ans from quiz where quiz_id=?", (self.id,))
            ans = ''.join(tmp.fetchone())
            with open("tmp.txt", "r", encoding='utf-8') as read_file:
                if read_file.read().strip() == ans:
                    return True, ans
            return False, None
