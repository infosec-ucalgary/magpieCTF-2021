FROM nsjailcontainer

ARG USERNAME=magpie
RUN useradd -m $USERNAME
RUN chmod a-w /home/$USERNAME

COPY textadventure /home/magpie/textadventure
COPY terminal-login /home/magpie/terminal-login
RUN chmod o+x /home/magpie/textadventure

EXPOSE 1976

CMD ["/bin/nsjail",                     \
        "-Ml",                          \
        "--hostname", "host",           \
        "--port", "1976",               \
        "--user", "1001",               \
        "--group", "1001",              \
        "--chroot", "/",                \
        "-E", "TERM=xterm",             \
        "--cwd", "/home/magpie",        \
        "--",                           \
        "/home/magpie/textadventure"            \
    ]

