export const user = {
    state: {
        username: 'admin',
        firstName: 'Andreas',
        lastName: 'Gerasimow',
        email: 'andreas.gerasimow12@gmail.com',
        joined: '2021/4/3'
    },
    mutations: {
        setUsername(state, value) {
            state.username = value;
        },
        setEmail(state, value) {
            state.email = value;
        },
        setFirstName(state, value) {
            state.firstName = value;
        },
        setLastName(state, value) {
            state.lastName = value;
        },
        setDateJoined(state, value) {
            state.joined = value;
        }
    },
    actions: {
        loadUserData(store) {
            const user = JSON.parse(document.getElementById('user').textContent);
            store.commit('setUsername', user.username);
            store.commit('setEmail', user.email);
            store.commit('setFirstName', user.first_name);
            store.commit('setLastName', user.last_name);
            store.commit('setDateJoined', user.date_joined)
        },
        saveUserData() {

        }
    },
    getters: {
        getUsername(state) {
            return state.username;
        },
        getEmail(state) {
            return state.email;
        },
        getDateJoined(state) {
            return state.joined;
        },
        getFirstName(state) {
            return state.firstName;
        },
        getLastName(state) {
            return state.lastName;
        }
    },
};