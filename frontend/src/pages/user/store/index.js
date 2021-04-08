import { createStore } from 'vuex'
import { user } from './user'
import { polls } from './polls'

export default createStore({
    state: {
        currentPage: 0,
    },
    mutations: {
        setCurrentPage(state, value) {
            state.currentPage = value;
        }
    },
    actions: {
        setCurrentPage(value) {
            this.commit('setCurrentPage', value);
        }
    },
    getters: {
        getCurrentPage(state) {
            return state.currentPage;
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
