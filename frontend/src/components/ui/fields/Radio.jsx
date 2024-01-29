import React from 'react'

const Radio = ({label, name, ...rest}) => {
    return (
        <div className='white__radio'>
            <input type='checkbox' className='white-radio' name={name} id={name} {...rest} />
            <label htmlFor={name}><span>{label}</span></label>
        </div>
        )
}

export default Radio