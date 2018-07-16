import Home from '@/components/Home';
import Contacts from '@/components/Contacts';
import Chats from '@/components/Chats';
import Rooms from '@/components/Rooms';

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
  path: '/rooms',
  component: Rooms,
  children: [],
}, ];