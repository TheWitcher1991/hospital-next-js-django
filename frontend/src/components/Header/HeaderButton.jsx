import React from 'react'
import {Link} from 'react-router-dom'
import {useAuth} from '@/hooks/useAuth'

const HeaderButton = () => {
    const {isAuthenticated} = useAuth()

    return (
        <div>
            {!isAuthenticated && (
                <div className='auth__button'>
                    <Link to='/login'><i className='mdi mdi-login'></i> Войти</Link>
                    <Link className='bth__active' to='/signup'><i className='mdi mdi-account-plus-outline'></i> Регистрация</Link>
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
