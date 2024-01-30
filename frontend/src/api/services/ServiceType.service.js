import {api} from '@/api/http/axios'
import axios from "axios";

class ServiceType {
    static all () {
        let  { data } = api.get('/service-type/')
        return data
    }

    static get (pk) {
        let { data } = api.get(`/service-type/${pk}`)
        return data
    }

    static create (data) {
        return api.post('/service-type/', data)
    }

    static update (data) {
        return axios.put(`/service-type/${data.pk}`, data)
    }

    static delete (pk) {
        return axios.delete(`/service-type/${pk}`)
    }
}

export default ServiceType
