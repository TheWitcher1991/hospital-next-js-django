import React from 'react'
import NotFound from '@/components/NotFound'
import {useAuth} from '@/hooks/useAuth'

const EmployeeRoute = ({children}) => {
    const {isAuthenticated, user} = useAuth()

    return isAuthenticated && user.data.type === 'С' ? children  : <NotFound />
}

export default EmployeeRoute