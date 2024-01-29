import React from 'react'
import {Navigate} from 'react-router-dom'
import useAuth from '@/hooks/useAuth'

const AllowRoute = ({children}) => {
    const {isAuthenticated} = useAuth()

    return !isAuthenticated ? children  : <Navigate to='/' />
}

export default AllowRoute
