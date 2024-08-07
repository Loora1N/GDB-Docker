# GDB-Docker

在比赛中遇到C++或其他一些项目类的pwn题时，动态链接库过于繁杂。手动或写脚本使用patchelf在本地建立依赖均较为麻烦，且不能保证与题目所提供的docker内环境完全一致。因而如果能直接使用pwntools和gdb在宿主机调试docker环境中的pwn题将方便很多。

该脚本template旨在简化宿主机调试docker内的pwn题调试流程，提高工作效率。

## Usage

调试效果类似本机调试`gdb.attch()`配合tmux，不过仍需注意一下两点

- 参照模板修改自身dockerfile，需安装gdbserver和socat，利用watchdog.sh监听链接
- 参考remote.py中的断点函数`p()`即可

### Dockerfile修改指北

基本逻辑是在dockerfile中添加watchdog.sh，循环监控docker内的pwn题是否存在运行中的进程，然后使用gdbserver attach到对应进程上，参考代码如下：

```dockerfile
RUN echo '#!/bin/bash\n\
while true; do\n\
    sleep 1\n\
    PID=$(pidof /app/URLQueryParser)\n\
    if [ -n "$PID" ]; then\n\
        gdbserver :1234 --attach $PID\n\
    fi\n\
done' > /app/watchdog.sh && \
chmod +x /app/watchdog.sh
```
> 这里的/app/URLQueryParser便是pwn题目的路径

剩余部分便是更改对应题目的start.sh，以确保watchdog.sh随docker同步启动，最后开放端口1234，以便于本地gdb链接

至于remote.py中的断点函数，更改对应的题目路径即可，gdb中需要的命令在gdb_source中定制更改

## 展示

效果图如下：

![调试效果图](/img/exp.png)

