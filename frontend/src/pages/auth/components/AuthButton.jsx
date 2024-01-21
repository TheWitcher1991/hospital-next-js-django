import React from 'react'

const AuthButton = ({children, ...rest}) => {
    return (
        <button className='auth__button-component' type='button' {...rest}>children</button>
    )
}

export default AuthButton;