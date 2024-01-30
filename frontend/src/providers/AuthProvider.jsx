import React from 'react'
// import {jwtDecode} from 'jwt-decode'
// import {redirect} from 'react-router-dom'
import PropTypes from 'prop-types'
import {csrf, api} from '@/api/http/axios'

export const AuthContext = React.createContext({})

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
        [user, isAuthenticated])

    return (
        <AuthContext.Provider value={context}>
            {children}
        </AuthContext.Provider>
    )
}

AuthProvider.propTypes = {
    children: PropTypes.any
}
