# Web Chat App

* Backend -> Django
* Frontend -> VueJS
* Database -> Postgres
* Admin db -> pgadmin 4

## Backend

### Starting a new project

```
  docker-compose run backend django-admin.py startproject project .

  sudo chown -R $USER .

  npm install -g @vue/cli

  vue create frontend

  docker-compose run frontend npm install
```

### Just Run

```
  sudo chown -R $USER .
  
  docker-compose up
```

## Frontend

## Database

## Documentation

  swagger - https://marcgibbons.com/django-rest-swagger/

## Tasks

### Frontend and Backend
- [ ] List Users of chat room
- [ ] Authentication (regular x/social)
- [ x ] Create a room for chat
- [ ] Participate of room
- [ ] Send messages
- [ ] Private chat
- [ ] Showing messages of a chat
- restrict messages to only users that participate from a room
- get messages only related from a room uri
- delete a chat room
- share a chat room
- List users of room
- Upload image of a room

- [ x ] Add name of 'room'

### Frontend
- [x] Header/Routing
- View of a room

### Backend
- [ x ] Create app for Users
- [ x ] urls for Chats

### Explaning

Criar uma sala
* Quando um usuário cria uma sala, ele automaticamente deve ser adicionado como membro

Abrir um chat com outro usuário
* Ao abrir uma conversa com outro usuário, ambos devem ser adicionados como membros