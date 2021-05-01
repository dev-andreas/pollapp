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
}

export function useFetching() {
    const notFound = ref(false);
    const fetching = ref(true);

    const fetchData = (path) => {
        notFound.value = false;
        fetching.value = true;

        return new Promise((resolve, reject) => {
            makeRequest("GET", "", path)
                .then((res) => {
                    resolve(res);
                })
                .catch((err) => {
                    notFound.value = true;
                    reject(err);
                })
                .finally(() => {
                    fetching.value = false;
                });
        });
    };

    return {
        notFound,
        fetching,
        fetchData,
    };
}

export function useSubmit() {
    const response = ref('');
    const error = ref('');
    const loading = ref(false);

    const submit = (path, data) => {
        loading.value = true;
        response.value = '';
        error.value = '';

        return new Promise((resolve, reject) => {
            makeRequest("POST", data, path)
                .then(res => {
                    response.value = res;
                    resolve(res);
                })
                .catch(err => {
                    error.value = err;
                    reject(err);
                })
                .finally(() => {
                    loading.value = false;
                });
        });
    };
    return {
        response,
        error,
        loading,
        submit,
    };
}