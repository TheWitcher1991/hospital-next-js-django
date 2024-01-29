import React from 'react'
import Helmet from 'react-helmet'
import {Link} from 'react-router-dom'
import ButtonFull from '@/components/ui/buttons/ButtonFull'
import BigInput from '@/components/ui/fields/BigInput'

const Signup = () => {
    return (
        <>
            <Helmet>
                <title>Регистрация - ЕМИАС</title>
            </Helmet>

            <form className='auth__form' action='' method='post'>
                <h1>Регистрация</h1>
                <div className='auth__choice'>
                    <div className='active'>
                        <i className='mdi mdi-emoticon-sick'></i>
                        Я пациент
                    </div>
                    <div>
                        <i className='mdi mdi-doctor'></i>
                        Я сотрудник
                    </div>
                </div>

                <BigInput name='oms' label='Номер ОМС' type='text' inputMode='numeric' maxLength='16'
                />

                <div className='auth__label'>
                    <label htmlFor='surname'>Фамилия</label>
                    <input id='surname' type='text' />
                </div>

                <div className='auth__label'>
                    <label htmlFor='name'>Имя</label>
                    <input id='name' type='text' />
                </div>

                <div className='auth__label'>
                    <label htmlFor=''>Email</label>
                    <input id='email' type='email' inputMode='email' />
                </div>

                <div className='auth__label'>
                    <label htmlFor='password'>Пароль</label>
                    <input id='password' type='password' minLength='8' />
                </div>

                <div className='exp__text' style={{textAlign: 'left'}}>
                    Нажимая “Продолжить”, вы соглашаетесь
                    с  <Link to='/'>Условиями использования</Link> и <Link to='/'>Политикой конфиденциальности</Link>
                </div>

                <ButtonFull name='Продолжить' />

                <div className='exp__text'>Уже зарегистрировались? <Link to='/login'>Войти</Link></div>
            </form>
        </>
    )
}

export default Signup
