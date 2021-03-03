def foo(a):
    assert a==2, Exception("不等于 2")
    print("ok", a)

if __name__ == '__main__':
    foo(1)