import React, {lazy, Suspense} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import Loader from './components/Loader'
import ProtectedRoute from './ProtectedRoute'

const Login = lazy(() => import('./pages/auth/Login'))
const Signup = lazy(() => import('./pages/auth/Signup'))
const Logout = lazy(() => import('./pages/auth/Logout'))
const AuthLayout = lazy(() => import('./pages/auth/AuthLayout'))

const App = () => {
    return (
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
    )
}

export default App
