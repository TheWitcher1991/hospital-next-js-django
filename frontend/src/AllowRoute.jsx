import React from 'react'
import {Navigate} from 'react-router-dom'

import {useAuth} from './hooks/useAuth'

const AllowRoute = ({children}) => {
    const { user } = useAuth()

    return !user ? children  : <Navigate to='/' />
}

export default AllowRoute
