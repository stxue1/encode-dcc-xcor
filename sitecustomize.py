import multiprocessing
import os, sys

def parse_cmdline():
    env_ncpu = None
    cmdline_ncpu = None

    env_opt = os.environ.get('PYTHONCPUCOUNT', None)
    if env_opt:
        try:
            ncpu = int(env_opt)
        except ValueError:
            print("WARNING: invalid PYTHONCPUCOUNT value:", env_opt)
        else:
            env_ncpu = ncpu
    # I don't think the below is supported in python2?
    # if 'cpu_count' in sys._xoptions:
    #     xopt = sys._xoptions['cpu_count']
    #     try:
    #         ncpu = int(xopt)
    #     except ValueError:
    #         print("WARNING: invalid PYTHONCPUCOUNT value:", xopt)
    #     else:
    #         cmdline_ncpu = ncpu

    ncpu = env_ncpu
    if cmdline_ncpu:
        ncpu = cmdline_ncpu
    if ncpu:
        # Override os.cpu_count()
        def cpu_count():
            return ncpu
        # cpu_count.__doc__ = os.cpu_count.__doc__
        os.cpu_count = cpu_count
        multiprocessing.cpu_count = cpu_count

parse_cmdline()

