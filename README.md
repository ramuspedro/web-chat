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
- [ ] List Users
- [ ] Authentication (regular/social)
- [ ] Create a room for chat
- [ ] Participate of room
- [ ] Send messages
- [ ] Private chat

- [ ] Add name of 'room'

### Frontend
- [ x ] Header/Routing

### Backend
- [ ] Create app for Users
- [ ] urls for Chats

### Explaning

Criar uma sala
* Quando um usuário cria uma sala, ele automaticamente deve ser adicionado como membro

Abrir um chat com outro usuário
* Ao abrir uma conversa com outro usuário, ambos devem ser adicionados como membros