import React from 'react'
import {Outlet} from 'react-router-dom'
import BindLayout from '@/components/layouts/BindLayout'

const AuthLayout = () => {
    return (
        <BindLayout>
            <div className='margin-top'></div>
            <div className='container'>
                <div className='auth__wrapper'>
                    <Outlet />
                </div>
            </div>
        </BindLayout>
    )
}

export default AuthLayout
