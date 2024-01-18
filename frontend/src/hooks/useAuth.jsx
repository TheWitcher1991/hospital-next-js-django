import React, {useEffect, useState, useMemo} from 'react'
import {jwtDecode} from 'jwt-decode'
import {useNavigate} from 'react-router-dom'
import PropTypes from 'prop-types'
import {api} '../utils/axios'

const AuthContext = React.createContext(null)

export const AuthProvider = ({userData, children}) => {
    let [authToken, setAuthToken] = useState(() => localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('token') ? jwtDecode(localStorage.getItem('token')) : null)
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()

    let csrf = async () => {
        let response = await axios.get('http://localhost:8080/api/csrf/')
        return response.headers['X-CSRFToken']
    }

    let login = async (email, password, type) => {
        e.preventDefault()

        let response = await api.post('/login', { email, password, type})

        let data = response.data.head

        if (data) {
            localStorage.setItem('token', JSON.stringify(data))
            setAuthToken(data)
            setUser(data)
            setLoading(true)
            navigate('/')
        }
    }

    let logout = () => {
        localStorage.removeItem('token')
        setAuthToken(null)
        setUser(null)
        navigate('/login')
    }

    /* let updateToken = async () => {
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
    } */

    useEffect(() => {
        /*if (loading) updateToken()
        const REFRESH_INTERVAL = 1000 * 60 * 4
        let interval = setInterval(() => {
            if (authToken) updateToken()
        }, REFRESH_INTERVAL)
        return () => clearInterval(interval)*/


    }, [user, loading])

    let context = useMemo(
        () => ({
            user,
            authToken,
            login,
            logout,
            loading,
        }),
        [user, loading])

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
