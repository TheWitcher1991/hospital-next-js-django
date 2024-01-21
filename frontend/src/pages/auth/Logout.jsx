import React from 'react'
import {Navigate} from 'react-router-dom'
import Helmet from 'react-helmet'
import {useAuth} from '@/hooks/useAuth'

const Logout = () => {
    const {logout} = useAuth()

    logout()

    return (
        <>
            <Helmet>
                <title>Выход - ЕМИАС</title>
            </Helmet>
            <Navigate to='/login' />
        </>
    )
}

export default Logout
