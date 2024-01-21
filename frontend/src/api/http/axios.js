import axios from 'axios'

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.withCredentials = true
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// https://djangodoc.ru/3.2/ref/csrf/
const csrf = async () => {
    let {headers} = await axios.get('http://localhost:8080/api/v1/csrf/')
    return headers.get('X-CSRFToken')
}

const api = axios.create({
    baseURL: 'http://localhost:8080/api/v1',
    headers: {
        'Content-Type':'application/json',
        'X-CSRFToken': csrf()
    }
})

export {api, csrf}
