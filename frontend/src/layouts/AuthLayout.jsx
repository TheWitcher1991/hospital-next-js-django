import React from 'react'
import {Outlet} from 'react-router-dom'
import BindLayout from './BindLayout'

const AuthLayout = () => {
    return (
        <BindLayout>
            <Outlet />
        </BindLayout>
    )
}

export default AuthLayout