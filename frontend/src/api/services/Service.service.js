import axios from 'axios'

class Model {

    constructor(url) {
        this.base = 'http://localhost:8080/api/v1'
        this.url = url
    }

    get api () {
        return axios.create({
            withCredentials: true,
            baseURL: this.base
        })
    }

    all () {
        return this.api.get(this.url).then(r => r.data)
    }

}

export default class Service extends Model {

    constructor() {
        super('/services');
    }

}

let service = Service()

service.all()


