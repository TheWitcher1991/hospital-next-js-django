import React from 'react'
import Header from '../ui/heading/Header'
import Footer from '../ui/heading/Footer'

const BindLayout = ({children}) => {
    return (
        <>
            <Header />
            <div className='context'>
                {children}
            </div>
            <Footer />
        </>
    )
}

export default BindLayout
