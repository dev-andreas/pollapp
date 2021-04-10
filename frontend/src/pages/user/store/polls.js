export const polls = {
    state: {
        pollsVoted: [
            { hash: '12345678', name: 'Testing Poll' },
            { hash: '98374320', name: 'Testing Poll1' },
            { hash: '98841046', name: 'Testing Poll2' },
            { hash: '82791348', name: 'Testing Poll3' },
            { hash: '83713400', name: 'Testing Poll4' },
            { hash: '09861904', name: 'Testing Poll5' },
            { hash: '90019901', name: 'Testing Poll6' },
            { hash: '81443879', name: 'Testing Poll7' },
        ],
        pollsCreated: [
            { hash: '12345678', name: 'Testing Poll' },
            { hash: '98374320', name: 'Testing Poll1' },
            { hash: '98841046', name: 'Testing Poll2' },
            { hash: '82791348', name: 'Testing Poll3' },
            { hash: '83713400', name: 'Testing Poll4' },
            { hash: '09861904', name: 'Testing Poll5' },
            { hash: '90019901', name: 'Testing Poll6' },
            { hash: '81443879', name: 'Testing Poll7' },
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