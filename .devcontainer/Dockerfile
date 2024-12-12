FROM ubuntu:latest

# ARG HOST_USER

# USER root

# RUN usermod -l $HOST_USER ubuntu \
#     && usermod -d /home/$HOST_USER -m $HOST_USER

# RUN echo $HOST_USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$HOST_USER \
#     && chmod 0440 /etc/sudoers.d/$HOST_USER

# USER $HOST_USER

# RUN echo "alias ll='ls -l'" >> ~/.bashrc && \
#     echo "alias g='git'" >> ~/.bashrc && \
#     echo ". /usr/share/bash-completion/completions/git" >> ~/.bashrc && \
#     echo "___git_complete g __git_main" >> ~/.bashrc && \
#     echo "complete -F  _fzf_path_completion nano" >> ~/.bashrc && \
#     echo "alias c='clj -M'" >> ~/.bashrc

# ENV LANG=en_US.UTF-8
# ENV LANGUAGE=en_US.UTF-8
# ENV LC_ALL=en_US.UTF-8
# ENV SHELL /bin/bash

# suppress help message about sudo
# RUN touch ~/.sudo_as_admin_successful
# USER root
# RUN cd /tmp && \
#     curl -L -O https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh && \
#     chmod +x linux-install.sh && \
#     ./linux-install.sh
# RUN sudo apt-get update && sudo apt-get install rlwrap

# USER $HOST_USER
