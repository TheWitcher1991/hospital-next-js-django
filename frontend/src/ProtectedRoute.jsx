import React from 'react'
import {Route, redirect} from 'react-router-dom'

import {useAuth} from './hooks/useAuth'

const ProtectedRoute = ({children, ...rest}) => {
    const { user } = useAuth()

    return (
        <>
            {(!user || !user.token || user.token === '') ? redirect('/login') : (
                <Route {...rest}>{children}</Route>
            )}
        </>

    )
}

export default ProtectedRoute
