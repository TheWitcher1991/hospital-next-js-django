import React from 'react'
import Logo from '@/components/ui/base/Logo'
import HeaderMenu from './HeaderMenu'
import HeaderButton from './HeaderButton'

const Header = () => {
    return (
        <header id='header'>
            <div className='container'>
                <nav>
                    <Logo />
                    <div className='header__nav-menu'>
                        <HeaderMenu />
                        <HeaderButton />
                    </div>
                </nav>
            </div>
        </header>
    )
}

export default Header
