import { makeRequest } from '../../../assets/utils.js'

export const polls = {
    state: {
        pollsVoted: [

        ],
        pollsCreated: [

        ],
    },
    mutations: {
        setPollsCreated(state, value) {
            state.pollsCreated = value;
        },
        setPollsVoted(state, value) {
            state.pollsVoted = value;
        },
        addCreatedPoll(state, value) {
            state.pollsCreated.push(value)
        },
        addVotedPoll(state, value) {
            state.pollsVoted.push(value)
        }
    },
    actions: {
        loadPollData(store) {
            makeRequest('GET', store.rootState.baseUrl + 'api/user/polls/')
                .then(res => { 

                });

            //store.commit('setPollsCreated', JSON.parse(document.getElementById('polls_created').textContent));
            //store.commit('setPollsVoted', JSON.parse(document.getElementById('polls_voted').textContent));
        },
    },
    getters: {
        getPollsCreated(state) {
            return state.pollsCreated;
        },
        getPollsVoted(state) {
            return state.pollsVoted;
        },
    },
};