import { createRouter, createWebHistory } from 'vue-router'
import InstitutionForm from '../components/InstitutionForm.vue'
import UploadCSV from '../views/UploadCSV.vue'
import Dashboard from '../views/Dashboard.vue'
import DashboardList from '../views/DashboardList.vue'
import InstitutionList from '../components/InstitutionList.vue'

const routes = [
  { path: '/', component: InstitutionForm },
  { path: '/upload', component: UploadCSV },
  { path: '/dashboard', component: DashboardList },
  { path: '/dashboard/:id', component: Dashboard },
  { path: '/institutions', component: InstitutionList }
]



export default createRouter({
  history: createWebHistory(),
  routes
})

