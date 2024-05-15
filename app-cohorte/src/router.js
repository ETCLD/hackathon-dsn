import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import i18n from './i18n'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/:lang',
      component: {
        render: h => h('router-view')
      },
      children: [
        {
          path: '',
          name: 'home',
          component: HomePage
        },
      ]
    }
  ]
})

router.beforeEach((to, from, next) => {
  const lang = to.params.lang;
  if (!['en', 'fr'].includes(lang)) {
    if (to.path.startsWith('/iae')){
      return next({ name: 'iae', params: { lang: 'fr' }, query: to.query});
    }
    else {
      return next('fr/');
    }
  }

  if (i18n.locale !== lang) {
    i18n.locale = lang;
  }

  return next();
});

export default router;