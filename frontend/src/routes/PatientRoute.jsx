import React from 'react'
import NotFound from '@/components/NotFound'
import {useAuth} from '@/hooks/useAuth'

const PatientRoute = ({children}) => {
    const {isAuthenticated, user} = useAuth()

    return isAuthenticated && user.data.type === 'П' ? children  : <NotFound />
}

export default PatientRoute
