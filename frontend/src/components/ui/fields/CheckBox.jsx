import React from 'react'

const CheckBox = ({label, name, ...rest}) => {
    return (
        <div className='white__checkbox'>
            <input type='checkbox' className='white-checkbox' name={name} id={name} {...rest} />
            <label htmlFor={name}><span>{label}</span></label>
        </div>
    )
}

export default CheckBox