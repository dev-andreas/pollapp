import { createStore } from 'vuex'
import { user } from './user'
import { polls } from './polls'

export default createStore({
    state: {
        currentPage: 0,
        baseUrl: 'http://127.0.0.1:8000/',
    },
    mutations: {
        setCurrentPage(state, value) {
            state.currentPage = value;
        },
    },
    actions: {
    },
    getters: {
        getCurrentPage(state) {
            return state.currentPage;
        },

        getBaseUrl(state) {
            return state.baseUrl;
        },

        // Navbar
        getNavLinks() {
            return [
                { name: 'Home', link: 'Home' },
                { name: 'Settings', link: 'UserSettings' },
                { name: 'New Poll', link: '' },
            ];
        },
    },
    modules: {
        user,
        polls,
    }
})
