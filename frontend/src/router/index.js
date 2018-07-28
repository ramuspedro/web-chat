import Home from '@/components/Home';
import Contacts from '@/components/Contacts';
import Chats from '@/components/chat/Chats';
import Room from '@/components/chat/Room';
import Rooms from '@/components/Rooms';
import Auth from '@/components/Auth';

export const routes = [{
  path: '/',
  component: Home,
  children: [],
}, {
  path: '/contacts',
  component: Contacts,
  children: [],
}, {
  path: '/chats',
  component: Chats,
  children: [],
  }, {
    path: '/chats/:chat_id',
    component: Room,
    children: [],
  }, {
  path: '/rooms',
  component: Rooms,
  children: [],
}, {
  path: '/auth',
  component: Auth,
  children: [],
}, ];