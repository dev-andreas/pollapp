import axios from "axios"

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