import React from 'react'
import Header from '@/components/ui/heading/Header'
import Footer from '@/components/ui/heading/Footer'

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
