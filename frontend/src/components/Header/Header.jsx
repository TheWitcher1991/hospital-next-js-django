import React from 'react'
import Logo from '../Logo'
import HeaderMenu from './HeaderMenu'
import HeaderButton from './HeaderButton'

const Header = () => {
    return (
        <header id='header'>
            <div className='container'>
                <nav>
                    <Logo />
                    <div>
                        <HeaderMenu />
                        <HeaderButton />
                    </div>
                </nav>
            </div>
        </header>
    )
}

export default Header