def f(*args, **kwargs):
    print(args)
    print(*kwargs)

f(100, 50, 25, 0)
f(galleons=100, sickles=50, knuts=25)
