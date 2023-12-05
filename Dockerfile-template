# Dockerfile for GDB-Docker
# Description: 这个模板只是为了展示功能，实际使用时需注意下面几个sh的部分
# Author: Loora1N
FROM ubuntu:20.04

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y g++ make netcat-openbsd
RUN apt-get install -y socat
RUN apt install -y gdbserver
WORKDIR /app

COPY src/ /app/src/
COPY include/ /app/include/

RUN g++ -fstack-protector-all -pie -fPIE -z relro -z now -z noexecstack -fpermissive -Wno-register -Iinclude -o URLQueryParser src/main.cpp

RUN echo '#!/bin/bash\n\
while true; do\n\
    sleep 1\n\
    PID=$(pidof /app/URLQueryParser)\n\
    if [ -n "$PID" ]; then\n\
        gdbserver :1234 --attach $PID\n\
    fi\n\
done' > /app/watchdog.sh && \
chmod +x /app/watchdog.sh

RUN echo '#!/bin/bash\n\
while true; do\n\
  socat TCP-LISTEN:4000,reuseaddr,fork EXEC:"/app/URLQueryParser",stderr\n\
done\n' > /app/entrypoint.sh && \
chmod +x /app/entrypoint.sh

RUN echo '#!/bin/bash\n\
/app/watchdog.sh &\n\
/app/entrypoint.sh' > /app/start.sh && \
chmod +x /app/start.sh

EXPOSE 4000
EXPOSE 1234

CMD ["/app/start.sh"]
