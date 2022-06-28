def son_func():
    print('cool_func(): Super Cool!')

print(__name__)
if __name__ == '__main__':
    print('Call it locally')
    son_func()