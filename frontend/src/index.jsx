import React from 'react'
import ReactDOM from 'react-dom/client'
import reportWebVitals from './webvitals/reportWebVitals'
import App from './App'

import {AuthProvider} from './hooks/useAuth'

let user = localStorage.getItem('token')
user = JSON.parse(user)

ReactDOM.createRoot(document.getElementById('root')).render(
    <AuthProvider userData={user}>
        <App/>
    </AuthProvider>
)

reportWebVitals()
