import React from 'react'
import Logo from '@/components/ui/base/Logo'

const Footer = () => {
    return (
        <footer id='footer'>
            <div className='container'>
                <div className='footer__container'>
                    <div className='footer__img'>
                        <Logo />
                        <div className='footer__img-slot'>
                            <img src='https://www.minobrnauki.gov.ru/local/templates/minobr/images/dest/logo-mobile.svg' alt='' />
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    )
}

export default Footer
