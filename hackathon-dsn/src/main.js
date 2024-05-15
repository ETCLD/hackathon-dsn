import './assets/main.css'

import { createApp } from 'vue'

import "primevue/resources/themes/aura-light-blue/theme.css";

import PrimeVue from 'primevue/config';
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Menubar from 'primevue/menubar';
import Badge from 'primevue/badge';
import Avatar from 'primevue/avatar';
import Toolbar from 'primevue/toolbar';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import TabMenu from 'primevue/tabmenu';
import Card from 'primevue/card';
import Divider from 'primevue/divider';
import Dropdown from 'primevue/dropdown';
import AutoComplete from 'primevue/autocomplete';

// import './style.css'
import App from './App.vue'

const app = createApp(App)
app.use(PrimeVue);
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Menubar', Menubar)
app.component('Badge', Badge)
app.component('Avatar', Avatar)
app.component('Toolbar', Toolbar)
app.component('IconField', IconField)
app.component('InputIcon', InputIcon)
app.component('TabMenu', TabMenu)
app.component('Card', Card)
app.component('Divider', Divider)
app.component('Dropdown', Dropdown)
app.component('AutoComplete', AutoComplete)

app.mount('#app')
