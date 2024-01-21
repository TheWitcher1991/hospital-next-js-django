import React from 'react'
import Helmet from 'react-helmet'
import {Link} from 'react-router-dom'
import AuthInput from '@/pages/auth/components/AuthInput'

const Login = () => {
    return (
        <>
            <Helmet>
                <title>Войти - ЕМИАС</title>
            </Helmet>

            <form className='auth__form' action='' method='post'>
                <h1>Авторизация</h1>

                <AuthInput name='email' label='Email' type='text' inputMode='email' />

                <AuthInput name='password' label='Пароль' type='text' />

                <button type='button'>Войти</button>

                <div className='exp__text'>Не аккаунта? <Link to='/signup'>Регистрация</Link></div>

            </form>
        </>
    )
}

export default Login
