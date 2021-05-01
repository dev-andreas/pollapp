import { makeRequest } from "../../../assets/utils.js";
import { DateTime } from "luxon";

export const user = {
    state: {
        user: {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            date_joined: '',
            profile_pic: '',
        },
        profile_pic_blob: null,
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
        },
        setProfilePic(state, value) {
            state.profile_pic_blob = value;
        },
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
            console.log(store.state.profile_pic_blob);
            if (store.state.profile_pic_blob !== null) {
                data.append("profile_pic", store.state.profile_pic_blob);
            }
            return makeRequest('POST', data, store.getters.getBaseUrl + 'api/user/')
            .finally(() => {
                store.state.profile_pic_blob = null;
            });
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
            return DateTime.fromISO(state.user.date_joined).toLocaleString(DateTime.DATETIME_FULL);
        },
        getFirstName(state) {
            return state.user.first_name;
        },
        getLastName(state) {
            return state.user.last_name;
        },
        getProfilePic(state) {
            return state.user.profile_pic;
        }
    },
};