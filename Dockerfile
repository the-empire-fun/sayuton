FROM ubuntu:16.04

ENV PYTHON_VERSION 3.7.0

ENV HOME /root
ENV ANYENV_HOME $HOME/.anyenv
ENV ANYENV_ENV  $ANYENV_HOME/envs

RUN apt-get update -q -y
RUN apt-get -y install curl git jq nkf make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev libncursesw5-dev xz-utils software-properties-common zip

RUN git clone https://github.com/riywo/anyenv $ANYENV_HOME
ENV PATH $ANYENV_HOME/bin:$PATH
RUN mkdir $ANYENV_ENV

RUN anyenv install pyenv
ENV PATH $ANYENV_ENV/pyenv/bin:$ANYENV_ENV/pyenv/shims:$PATH
ENV PYENV_ROOT $ANYENV_ENV/pyenv

RUN pyenv install $PYTHON_VERSION; pyenv global $PYTHON_VERSION; pyenv rehash

RUN pip install Django

RUN apt-get -y install vim
RUN rm -rf /var/lib/apt/lists/*

COPY tools/run.sh /usr/local/bin/

#COPY /usr/bin/docker /usr/local/bin/
