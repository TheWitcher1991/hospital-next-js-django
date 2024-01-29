import React from 'react'
import {Outlet} from 'react-router-dom'
import NotFound from '@/components/screens/NotFound'
import useAuth from '@/hooks/useAuth'

const EmployeeRoute = ({children}) => {
    const {isAuthenticated, user} = useAuth()

    return isAuthenticated && user.data.type === 'С' ? <Outlet /> : <NotFound />
}

export default EmployeeRoute
