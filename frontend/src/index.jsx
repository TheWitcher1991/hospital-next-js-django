import React from 'react'
import ReactDOM from 'react-dom/client'
import {AuthProvider} from '@/providers/AuthProvider'
import * as serviceWorker from '@/serviceWorker'
import App from '@/App'

ReactDOM.createRoot(document.getElementById('root')).render(
    <AuthProvider>
        <App/>
    </AuthProvider>
)

serviceWorker.register()
