import os

def basic_test():
    dir = 'myDir'
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        print(dir + '已建立')
        os.rmdir(dir)

    file = 'test.txt'
    if os.path.exists(file):
        os.remove()
    else:
        os.mkdir(file)
        print(file + '剛已建立')

def path_test():
    cur_path = os.path.dirname(__file__)
    print(cur_path)

    file_path = os.path.abspath('basic_test.py')
    if os.path.exists(file_path):
        print('file path', file_path)
        print('file size', os.path.getsize)

        base_name = os.path.basename(file_path)
        print('最後檔案名稱', base_name)

        dir_name = os.path.dirname(file_path)
        print('目錄路徑', dir_name)
        print('是否為目錄', os.path.isdir(base_name))

        fullpath, fname = os.path.split(file_path)
        print('目錄路徑', fullpath)
        print('檔案名稱', fname)

def file_process_test():
    file_name = 'test.txt'
#     content = '''Lambda函式，也就是匿名函式，不需要定義名稱，只有一行運算式，語法非常簡潔，功能強大，所以現代程式語言如Java、C#及Python等都支援Lambda函式，
# 適用於小型的運算，Python的一些內建函式甚至使用它作為參數值的運算。現在就來介紹如何在Python中使用Lambda函式與技巧吧
#     '''
#     f = open(file_name, 'w')
#     f.write(content)

    with open(file_name, 'r') as f:#預設為 r 讀取模式
        print(f)
        for line in f:
            print(line, end='')
    # f.close()
if __name__ == '__main__':
    file_process_test()