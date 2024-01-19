import React, {lazy, Suspense, Fragment} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import Loader from './components/Loader'
import ProtectedRoute from './ProtectedRoute'
import AllowRoute from './AllowRoute'

const MainLayout = lazy(() => import('./layouts/MainLayout'))
const AuthLayout = lazy(() => import('./layouts/AuthLayout'))

const Login = lazy(() => import('./pages/auth/Login'))
const Signup = lazy(() => import('./pages/auth/Signup'))
const Logout = lazy(() => import('./pages/auth/Logout'))


const App = () => {
    return (
        <Router>
            <Suspense fallback={<Loader />}>
                <Fragment>
                    <Routes>
                        <Route path='/' element={
                            <AllowRoute>
                                <AuthLayout />
                            </AllowRoute>
                        }>
                            <Route path='login' element={<Login />} />
                            <Route path='signup' element={<Signup />} />
                            <Route path='logout' element={<Logout />} />
                        </Route>

                        <Route path='/' element={
                            <ProtectedRoute>
                                <MainLayout />
                            </ProtectedRoute>
                        }>
                            <Route index />
                        </Route>
                    </Routes>
                </Fragment>
            </Suspense>
        </Router>
    )
}

export default App
