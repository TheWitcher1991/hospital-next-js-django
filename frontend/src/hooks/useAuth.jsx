import React, {useEffect, useState} from 'react'
import {jwtDecode} from 'jwt-decode'
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import PropTypes from 'prop-types'

const AuthContext = React.createContext(null)

export const AuthProvider = ({userData, children}) => {
    let [authToken, setAuthToken] = useState(() => localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('token') ? jwtDecode(localStorage.getItem('token')) : null)
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()

    let login = async e => {
        e.preventDefault()

        let response = await axios.post('http://localhost:8080/api/login/', {
            headers: {
                'Content-Type':'application/json'
            },
            username: e.target.username.value,
            password: e.target.password.value,
            type: 0
        })

        let data = response.data

        if (data) {
            localStorage.setItem('token', JSON.stringify(data))
            setAuthToken(data)
            setUser(data.access)
            navigate('/')
        }
    }

    let logout = () => {
        localStorage.removeItem('token')
        setAuthToken(null)
        setUser(null)
        navigate('/login')
    }

    let updateToken = async () => {
        let response = await axios.post('http://localhost:8080/api/token/refresh/', {
            headers: {
                'Content-Type':'application/json'
            },
            refresh: authToken.refresh
        })

        let data = response.data

        if (response.status === 200) {
            setAuthToken(data)
            setUser(data.access)
            localStorage.setItem('token', JSON.stringify(data))
        } else {
            logout()
        }

        if (loading) setLoading(false)

    }

    let context = {
        user,
        authToken,
        login,
        logout
    }

    useEffect(() => {
        if (loading) updateToken()

        const REFRESH_INTERVAL = 1000 * 60 * 4

        let interval = setInterval(() => {
            if (authToken) updateToken()
        }, REFRESH_INTERVAL)

        return () => clearInterval(interval)
    }, [authToken, loading]);

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
