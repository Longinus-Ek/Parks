import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
import 'datatables.net-bs5';
import 'datatables.net-bs5/css/dataTables.bootstrap5.css';
import 'jquery';

createApp(App).use(store).use(router).mount('#app')
