import yappiyappi.start(builtins=True)class A:    def bar(self):        passdef foo():    import time    time.sleep(2.0)    for i in range(20000000):        pass    a = A()    a.bar()    foo()#yappi.write_callgrind_stats()yappi.print_func_stats(sort_type=yappi.SORTTYPE_TAVG)yappi.print_thread_stats()#import cProfile#cProfile.run('foo()', 'fooprof')#import pstats#p = pstats.Stats('fooprof')#p.strip_dirs().sort_stats(-1).print_stats()