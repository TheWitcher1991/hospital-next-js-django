import React from 'react'
import Header from '../components/Header/Header'
import Footer from '../components/Footer/Footer'

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