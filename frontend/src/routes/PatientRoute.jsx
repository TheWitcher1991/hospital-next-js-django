import React from 'react'
import {Outlet} from 'react-router-dom'
import NotFound from '@/components/screens/NotFound'
import useAuth from '@/hooks/useAuth'

const PatientRoute = ({children}) => {
    const {isAuthenticated, user} = useAuth()

    return isAuthenticated && user.data.type === 'П' ? <Outlet /> : <NotFound />
}

export default PatientRoute
