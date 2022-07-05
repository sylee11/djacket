import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/Product.vue'
import CategoryView from '../views/Category.vue'
import SearchView from '../views/Search.vue'
import CartView from '../views/CartView.vue'
import SignUpView from '../views/SignUp.vue'
import LogInView from '../views/LoginView.vue'
import MyAccountView from '../views/MyAccount.vue'
import CheckoutProcessView from '../views/CheckoutProcess.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/products/:category_slug/:product_slug',
    name: 'product',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: ProductView
  },
  {
    path: '/categories/:category_slug',
    name: 'category',
    component: CategoryView
  },
  {
    path: '/products/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/sign-up',
    name: 'signUp',
    component: SignUpView
  },
  {
    path: '/log-in',
    name: 'logIn',
    component: LogInView
  },
  {
    path: '/my-account',
    name: 'myAccount',
    component: MyAccountView
  },
  {
    path: '/cart/checkout',
    name: 'checkoutProcess',
    component: CheckoutProcessView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
