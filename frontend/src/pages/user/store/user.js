import { makeRequest } from "../../../assets/utils.js"

export const user = {
    state: {
        user: {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            date_joined: ''
        },
    },
    mutations: {
        setUser(state, value) {
            state.user = value;
        },
        setUsername(state, value) {
            state.user.username = value;
        },
        setFirstName(state, value) {
            state.user.first_name = value;
        },
        setLastName(state, value) {
            state.user.last_name = value;
        },
        setEmail(state, value) {
            state.user.email = value;
        }
    },
    actions: {
        loadUserData(store) {
            const user = JSON.parse(document.getElementById('user').textContent);
            store.commit('setUser', user);
        },
        saveUserData(store) {
            let data = new FormData();
            data.append('username', store.getters.getUsername);
            data.append("first_name", store.getters.getFirstName);
            data.append("last_name", store.getters.getLastName);
            data.append("email", store.getters.getEmail);
            return makeRequest('POST', data, store.getters.getBaseUrl + 'api/user/');
        }
    },
    getters: {
        getUser(state) {
            return state.user;
        },
        getUsername(state) {
            return state.user.username;
        },
        getEmail(state) {
            return state.user.email;
        },
        getDateJoined(state) {
            return state.user.date_joined;
        },
        getFirstName(state) {
            return state.user.first_name;
        },
        getLastName(state) {
            return state.user.last_name;
        }
    },
};