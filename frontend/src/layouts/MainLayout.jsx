import React from 'react'
import {Outlet} from 'react-router-dom'
import BindLayout from './BindLayout'

const MainLayout = () => {
    return (
        <BindLayout>
            <Outlet />
        </BindLayout>
    )
}

export default MainLayout