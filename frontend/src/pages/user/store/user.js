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
    },
    actions: {
        setUsername(value) {
            this.commit('setUsername', value);
        },
        setEmail(value) {
            this.commit('setEmail', value);
        },
        setFirstName(value) {
            this.commit('setFirstName', value);
        },
        setLastName(value) {
            this.commit('setLastName', value);
        },
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