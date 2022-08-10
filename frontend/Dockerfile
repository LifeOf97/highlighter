FROM node:buster-slim

# used to run the built app
RUN npm install -g http-server

# create system user/group
RUN useradd --create-home --shell /bin/bash --user-group justhighlight
USER justhighlight

RUN mkdir -p /home/justhighlight/frontend

WORKDIR /home/justhighlight/frontend

COPY --chown=justhighlight:justhighlight package.json .
COPY --chown=justhighlight:justhighlight package-lock.json .

# install dependencies
RUN npm install

# copy project over
COPY --chown=justhighlight:justhighlight . .

# build app
RUN npm run build

# run server
# CMD [ "http-server", "/home/justhighlight/frontend/dist" ]