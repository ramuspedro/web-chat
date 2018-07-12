
FROM node:9

LABEL authors="Pedro Ramos"

# Create a directory where our app will be placed
RUN mkdir -p /home/app

COPY . /home/app

# Change directory so that our commands run inside this new directory
WORKDIR /home/app

RUN npm install -g @vue/cli