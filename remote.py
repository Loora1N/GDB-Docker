"""
File: remote.py
Author: Loora1N
Email: loorain917@gmail.com
Time: 2023-12-05
"""
from pwn import *
import subprocess

context.binary = './URLQueryParser'
context.log_level = 'debug'
context.arch = 'amd64'
context.os = 'linux'


io = remote('127.0.0.1', 4000)

# gdb参数，远程调试堆时需要设置glibc版本
gdb_source ='''
target remote 127.0.0.1:1234
set resolve-heap-via-heuristic on
set glibc 2.31
'''

def convert_to_gdb_script(gdb_source):
    gdb_script = ' '.join([f"-ex '{line.strip()}'" for line in gdb_source.split('\n') if line.strip()])
    return gdb_script


def p():
    sleep(1)
    cmd = 'tmux split-window -h "gdb ./URLQueryParser '+convert_to_gdb_script(gdb_source) + '"'
    subprocess.Popen(cmd, shell=True)

# io交互代码部分

io.interactive()
