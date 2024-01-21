import React from 'react'

const AuthInput = ({label, name, ...rest}) => {
    return (
        <div className='auth__label'>
            <label htmlFor={name}>{label}</label>
            <input id={name} name={name} {...rest} />
        </div>
    )
}

export default AuthInput