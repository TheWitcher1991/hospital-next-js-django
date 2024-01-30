import React from 'react'
import {AuthContext} from '@/providers/AuthProvider'

const useAuth = () => React.useContext(AuthContext)

export default useAuth

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
