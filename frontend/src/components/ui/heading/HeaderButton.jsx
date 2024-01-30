import React from 'react'
import {Link} from 'react-router-dom'
import useAuth from '@/hooks/useAuth'

const HeaderButton = () => {
    const {isAuthenticated} = useAuth()

    return (
        <div>
            {!isAuthenticated && (
                <div className='auth__button'>
                    <Link className='bth__active' to='/login'><i className='mdi mdi-login'></i> Авторизация</Link>
                </div>
            )}

            {isAuthenticated && (
                <div className='auth__button'>
                    <Link to='/profile'><i className='mdi mdi-account'></i> Профиль</Link>
                </div>
            )}
        </div>
    )
}

export default HeaderButton
