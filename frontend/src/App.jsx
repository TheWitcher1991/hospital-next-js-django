import React, {lazy, Suspense} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import {AuthProvider} from './hooks/useAuth'

const Loader = lazy(() => import('./components/Loader'))

const Login = lazy(() => import('./pages/auth/Login'))
const Signup = lazy(() => import('./pages/auth/Signup'))
const Logout = lazy(() => import('./pages/auth/Logout'))
const AuthLayout = lazy(() => import('./pages/auth/AuthLayout'))

const App = () => {
    let user = localStorage.getItem('user')
    user = JSON.parse(user)
    
    return (
        <AuthProvider userData={user}>
            <main className='wrapper'>
                <Router>
                    <Suspense fallback={<Loader />}>
                        <Routes>
                            <Route path='/' element={<AuthLayout />}>
                                <Route path='login' element={<Login />} />
                                <Route path='signup' element={<Signup />} />
                                <Route path='logout' element={<Logout />} />
                            </Route>
                        </Routes>
                    </Suspense>
                </Router>
            </main>
        </AuthProvider>
    )
}

export default App
