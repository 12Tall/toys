import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import 'vue-awesome/icons';

// tslint:disable-next-line
import Icon from 'vue-awesome/components/Icon.vue';
Vue.component('v-icon', Icon);

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
