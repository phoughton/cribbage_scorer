FROM gitpod/workspace-full:latest

USER gitpod

RUN echo "alias ll='ls -lrta'" >> ~/.bashrc
RUN echo "export PIP_USER=false" >> ~/.bashrc
