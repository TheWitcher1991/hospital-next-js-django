import React from 'react'
import {Outlet} from 'react-router-dom'

const AuthLayout = () => {
    return (
        <section>
            <Outlet />
        </section>
    )
}

export default AuthLayout