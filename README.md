# GDB-Docker

在比赛中遇到C++或其他一些项目类的pwn题时，动态链接库过于繁杂。手动或写脚本使用patchelf均较为麻烦，且一定能保证与docker内环境完全一致。因而如果能直接使用pwntools和gdb在宿主机调试docker环境中的pwn题将方便很多。

该脚本template旨在简化宿主机调试docker内的pwn题调试流程，提高工作效率。

## Usage

调试效果类似本机调试`gdb.attch()`配合tmux，不过仍需注意一下两点

- 参照模板修改自身dockerfile，需安装gdbserver和socat，利用watchdog.sh监听链接
- 参考remote.py中的断点函数`p()`即可
