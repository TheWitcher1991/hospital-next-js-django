import React from 'react'
import Helmet from 'react-helmet'
import {Link, redirect} from 'react-router-dom'
import AuthInput from '@/pages/auth/components/AuthInput'
import {useAuth} from '@/hooks/useAuth'

const Login = () => {
    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const {login} = useAuth()

    const handleLogin = e => {
        e.preventDefault()

        login(email, password)
        redirect('/')
    }

    return (
        <>
            <Helmet>
                <title>Войти - ЕМИАС</title>
            </Helmet>

            <form className='auth__form' action='' method='post'>
                <h1>Авторизация</h1>

                <AuthInput name='email' label='Email' type='text' inputMode='email'
                    onChange={e => setEmail(e.target.value)}
                    value={email}
                />

                <AuthInput name='password' label='Пароль' type='text'
                    onChange={e => setPassword(e.target.value)}
                    value={password}
                />

                <button type='button' onClick={handleLogin}>Войти</button>

                <div className='exp__text'>Не аккаунта? <Link to='/signup'>Регистрация</Link></div>

            </form>
        </>
    )
}

export default Login
