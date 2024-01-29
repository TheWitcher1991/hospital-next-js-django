import React from 'react'

const BigInput = ({label, name, styleLabel={}, ...rest}) => {
    return (
        <div style={styleLabel} className='auth__label'>
            <label htmlFor={name}>{label}</label>
            <input id={name} name={name} {...rest} />
        </div>
    )
}

export default BigInput