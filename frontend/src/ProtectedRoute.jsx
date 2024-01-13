import React from 'react'
import {Route, redirect} from 'react-router-dom'

import {useAuth} from './hooks/useAuth'

const ProtectedRoute = ({chidlren, ...rest}) => {
    const { user } = useAuth()
    
    return (
        <>
            {(!user || !user.token || user.token === '') ? redirect('/login') : (
                <Route {...rest}>{chidlren}</Route>
            )}
        </>
       
    )
}

export default ProtectedRoute