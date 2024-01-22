import React from 'react'
    
const ButtonFull = ({name, ...rest}) => {
    return <button className='button__full' type='button' {...rest}>{name}</button>
}

export default ButtonFull