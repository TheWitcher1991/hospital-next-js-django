import React, {lazy, Suspense} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import Loader from './components/Loader'
import ProtectedRoute from './ProtectedRoute'

const MainLayout = lazy(() => import('./layouts/MainLayout'))
const AuthLayout = lazy(() => import('./layouts/AuthLayout'))

const Login = lazy(() => import('./pages/auth/Login'))
const Signup = lazy(() => import('./pages/auth/Signup'))
const Logout = lazy(() => import('./pages/auth/Logout'))


const App = () => {
    return (
        <main className='wrapper'>
            <Router>
                <Suspense fallback={<Loader />}>
                    <Routes>
                        <ProtectedRoute path='/' element={<MainLayout />}>

                        </ProtectedRoute>

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
