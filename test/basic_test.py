def str_test():
    print('hi', ' ZZ', ' ~~\n', sep=':)', end='##') #defualt end is \n
    name, job, height = 'ZZ', 'data analyst', 158
    print('%s is %s; height:%-5d' % (name, job, height))
    print('{} is {}; height:{}'.format(name, job, height))
    print(type(height))
    print('{0:d}-{0:x}-{0:o}-{0:b}'.format(21)) #decimal - hexidecimal - octal - binary
    print('{0:0<5d} - {0:010,} - {0:^10}'.format(123))
    print('{0:.2f} - {0:10f} - {0:010.3f} - {0:0<10f}'.format(2.12345))
    print('height: ' + str(height)) #str() / int() / float()
    print('{:<6d}'.format(123))

# ordinal mutable
def list_test():
    # list1 = list()
    # list1 = []
    # list1 = list([1, 2, 3, 4, 5])
    list1 = [1, 1, 6, 3, 2]
    list2 = [4, 5]
    list3 = list1 + list2

    sorted_list1 = sorted(list1, reverse=True)
    list1.sort(reverse=True) #True will sort the list descending. Default is reverse=False
    print(sorted_list1)
    # list1.reverse()
    # list1.remove(2)
    # list1.insert(1, 2) #[1, 2, 1, 2, 3]
    # print(list1.pop(2))
    # print(list3.index(2))
    # print(len(list1))
    # print(max(list1))
    # print(min(list1))
    # print(sum(list1))
    # list1.append([100, 200]) #整個list塞進去
    # print(list1)
    # list1.extend([100, 200]) #拆解裡面元素
    # print(list1)
    # print(list1.count(1)) #元素出現次數

    # print(list3) # [1, 2, 3, 4, 5]
    # print(list3[1:3]) # [2, 3] exclude last element
    #
    # list2[0] = 100 # change an element
    # print(list2)
    #
    # list4 = list2 * 2
    # print(list4) # [100, 5, 100, 5] duplicate list element
    #
    # list5 = [100, 5, 100, 5]
    # print(list4 == list5) #True
    # print(100 in list5) #True
    # print(list5[1:]) #[100, 5]
    #
    # list6 = [i for i in range(8)]
    # print(list6)
    #
    # del list6[0]
    # print(list6)

# ordinal immutable
def tuple_test():
    # tuple1 = tuple()
    # tuple1 = ()
    # tuple1 = ((1, 2, 3))
    tuple1 = (1, 2, 3)
    num1, num2, num3 = tuple1 #unpack
    num4, *num5 = tuple1
    print(num4, ' ', num5) #1   [2, 3]

    tuple1 = tuple1 * 2
    print(tuple1)

    # 不可變型態 元素相同為同樣物件
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    print(tuple1 is tuple2)
    print(id(tuple1))
    print(id(tuple2))

# 沒順序 不重複
def set_test():
    set1 = set()
    set1.add('Alex')
    set1.add(123)

    set2 = {321, 'kevin'}
    set3 = set2
    # print(set1 + set2) error

    print(set3 is set2)
    print(id(set2))
    print(id(set3))

# 沒順序 不重複 key須為immutable資料型態like: number string
def dict_test():
    # dict1 =dict({'name': 'kv', 'age': 26})
    # dict1 =dict(name= 'kv', age= 26)
    dict1 = {'name': 'kv', 'age': 26}
    dict2 = {'age': 26, 'name': 'kv'}
    print(dict1 == dict2)

    dict1['new-key'] = 'test'
    del dict1['new-key']

    print(dict1.items()) #dict_items([('name', 'kv'), ('age', 26)])
    print(dict1.keys()) #dict_keys(['name', 'age'])
    print(dict1.values()) #dict_values(['kv', 26])

    for name, age in dict1.items():
        print('{} => {}'.format(name, age))

    dict3 = dict([('name', 'Zz'), ('age', 24)])
    dict4 = dict.fromkeys(['name', 'age'], 'default')
    print(dict4.get('name', 'Jack'))
    print(dict4.get('city', 'taipei'))
    print(dict4.setdefault('gender', 'N')) #dict4的內容會改變，如第一參數的key不存在則會add到dict4，第二個參數沒設預設為None
    print(dict4)

def range_test():
    for i in range(0, 10, 2):
        print(i, end=',')
    for i in range(2):
        if(i == 3):
            break
        print('i=', i)
    else: #沒進到break才會跑到else
        print('else')

def fun_test(width, height = 10):
    print(height)
    return width * height

def many_params_test(*args):
    print(args)

def add_two(x):
    x += 2
    return x

if __name__ == '__main__':
    print(divmod(10, 3)) #商 餘
    print(ord('A'))
    print(chr(65))
    list1 = [1, 2, 3, 4, 5]
    print(list(map(add_two, list1)))
    print(list(map(lambda x: x + 2, list1)))
    print(list1)
