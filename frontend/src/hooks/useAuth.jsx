import React from 'react'
// import {jwtDecode} from 'jwt-decode'
// import {redirect} from 'react-router-dom'
import PropTypes from 'prop-types'
import {csrf, api} from '@/api/http/axios'

const AuthContext = React.createContext({})

export const AuthProvider = ({children}) => {
    // let [authToken, setAuthToken] = useState(() => localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null)
    // let [user, setUser] = useState(() => localStorage.getItem('token') ? jwtDecode(localStorage.getItem('token')) : null)
    const [isAuthenticated, setAuthenticated] = React.useState(false)
    const [user, setUser] = React.useState({
        csrf: '',
        data: {}
    })

    const authenticate = () => {
        api.get('/authenticate/')
            .then(async ({data}) => {
                if (data.isAuthenticated) {
                    setUser({...user})
                    setAuthenticated(true)
                } else {
                    setUser({...user, csrf: await csrf()})
                    setAuthenticated(false)
                }
            })
            .catch(err => console.log(err))
    }

    const login = (email, password) => {
        api.post('/login/', {email, password})
            .then(async ({data}) => {
                setUser({...data})
                setAuthenticated(true)
            })
            .catch(err => console.log(err))
    }

    const logout = () => {
        api.post('/logout/')
            .then(async () => {
                setUser({data: {}, csrf: await csrf()})
                setAuthenticated(false)
            })
            .catch(err => console.log(err))
    }

    React.useEffect(() => {
        authenticate()
    }, [authenticate])

    let context = React.useMemo(
        () => ({
            user,
            isAuthenticated,
            authenticate,
            login,
            logout
        }),
        [user, isAuthenticated, authenticate])

    return (
        <AuthContext.Provider value={context}>
            {children}
        </AuthContext.Provider>
    )
}

AuthProvider.propTypes = {
    children: PropTypes.any
}

export const useAuth = () => React.useContext(AuthContext)


/*let csrf = async () => {
        let response = await axios.get('http://localhost:8080/api/csrf/')
        return response.headers['X-CSRFToken']
    }

    let login = async (email, password, type) => {
        let response = await api.post('/login', { email, password, type})

        let data = response.data.head

        if (data) {
            localStorage.setItem('token', JSON.stringify(data))
            setAuthToken(data)
            setUser(data)
            setLoading(true)
            redirect('/')
        }
    }

    let logout = async () => {
        let response = await api.post('/logout')
        localStorage.removeItem('token')
        setAuthToken(null)
        setUser(null)
        redirect('/login')
    }

    let updateToken = async () => {
        let response = await axios.post('http://localhost:8080/api/token/refresh/', {
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrf()
            },
            refresh: authToken.refresh
        })
        let data = response.data
        if (response.status === 200) {
            setAuthToken(data)
            setUser(data.access)
            localStorage.setItem('token', JSON.stringify(data))
        } else logout()
        if (loading) setLoading(false)
    }

    useEffect(() => {
        if (loading) updateToken()
        const REFRESH_INTERVAL = 1000 * 60 * 4
        let interval = setInterval(() => {
            if (authToken) updateToken()
        }, REFRESH_INTERVAL)
        return () => clearInterval(interval)


    }, [user, loading]) */
