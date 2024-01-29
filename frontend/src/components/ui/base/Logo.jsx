import React from 'react'
import {Link} from 'react-router-dom'

const Logo = () => {
    return (
        <Link to='/' className='global__logo'>
            <i className='mdi mdi-pill'></i>
            <span>ЕМИАС</span>
        </Link>
    )
}

export default Logo
