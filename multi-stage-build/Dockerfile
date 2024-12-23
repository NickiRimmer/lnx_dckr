FROM node:latest AS builder
RUN apt update \
    && apt upgrade
WORKDIR /home
RUN apt install git \
	&& git clone https://github.com/NickiRimmer/MShell.git \
	&& gcc -static -o mshell /home/MShell/v3.c

FROM scratch
COPY --FROM=builder 
