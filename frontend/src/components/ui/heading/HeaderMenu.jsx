import React from 'react'
import {Link} from 'react-router-dom'
import useAuth from '@/hooks/useAuth'
import {patientRoutes, employeeRoutes} from '@/routes/routes'

const HeaderMenu = () => {
    return (
        <div className='header-menu'>
            {patientRoutes.map(({id, path, name}) => {
                return <Link to={path} tabIndex={id} key={Date.now()}>{name}</Link>
            })}
        </div>
    )

    /* const {isAuthenticated, user} = useAuth()

    if (isAuthenticated) {
        const {type} = user.data

        return (
            <div className='header-menu'>
                {type === 'П' && patientRoutes.map(({id, path, name}) => {
                    return <Link to={path} tabIndex={id} key={Date.now()}>{name}</Link>
                })}

                {type === 'С' && employeeRoutes.map(({id, path, name}) => {
                    return <Link to={path} tabIndex={id} key={Date.now()}>{name}</Link>
                })}
            </div>
        )
    }

    return <React.Fragment></React.Fragment> */
}

export default HeaderMenu
