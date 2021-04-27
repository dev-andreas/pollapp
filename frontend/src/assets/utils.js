import axios from "axios"
import { ref } from "vue"

export function makeRequest(method, data, url) {
    return axios({
        method: method,
        url: url,
        headers: {
            'X-CSRFToken': 'csrftoken'
        },
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken'
    });
};

export function useFetching(path) {
    const notFound = ref(false);
    const fetching = ref(true);

    const fetchData = () => {
        notFound.value = false;
        fetching.value = true;

        return makeRequest("GET", "", path)
            .catch((err) => {
                notFound.value = true;
            })
            .finally(() => {
                fetching.value = false;
            });
    };

    return {
        notFound,
        fetching,
        fetchData,
    };
}

export function useSubmit(path) {
    const response = ref('');
    const error = ref('');
    const loading = ref(false);

    const submit = (data) => {
        loading.value = true;
        response.value = '';
        error.value = '';
        return makeRequest("POST", data, path)
            .then(res => {
                response.value = res;
            })
            .catch(err => {
                error.value = err;
            })
            .finally(() => {
                loading.value = false;
            });
    };
    return {
        response,
        error,
        loading,
        submit,
    };
}