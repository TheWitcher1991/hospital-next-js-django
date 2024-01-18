import React from 'react'
import {redirect} from 'react-router-dom'

const Logout = () => {
    return (
        <> {redirect('/login')} </>
    )
}

export default Logout