import React from 'react'
import Header from '../components/Header/Header'
import Footer from '../components/Footer/Footer'

const BindLayout = ({children}) => {
    return (
        <main className='wrapper'>
            <Header />
            {children}
            <Footer />
        </main>
    )
}

export default BindLayout