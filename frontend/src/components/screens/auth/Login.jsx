import React, {useState} from 'react'
import Helmet from 'react-helmet'
import {Link, redirect} from 'react-router-dom'
import CheckBox from '@/components/ui/fields/CheckBox'
import ButtonFull from '@/components/ui/buttons/ButtonFull'
import BigInput from '@/components/ui/fields/BigInput'
import useAuth from '@/hooks/useAuth'

const Login = () => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [remember, setRemember] = useState(false)
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

                <BigInput name='email' label='Email' type='text' inputMode='email'
                    onChange={e => setEmail(e.target.value)}
                    value={email}
                />

                <BigInput name='password' label='Пароль' type='text'
                    onChange={e => setPassword(e.target.value)}
                    value={password}
                    styleLabel={{marginBottom: 6}}
                />

                <CheckBox label='Запомнить меня' name='remember' value='1'
                    checked={remember} onChange={() => setRemember(!remember)}
                />

                <ButtonFull name='Войти' onClick={handleLogin} />

                <div className='exp__text'>Не аккаунта? <Link to='/signup'>Регистрация</Link></div>

            </form>
        </>
    )
}

export default Login
