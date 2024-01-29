import React, {lazy, Suspense} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import '@/styles/index.sass'

import Loader from '@/components/ui/base/Loader'
import PatientRoute from '@/routes/PatientRoute'
import EmployeeRoute from '@/routes/EmployeeRoute'
import ProtectedRoute from '@/routes/ProtectedRoute'
import AllowRoute from '@/routes/AllowRoute'

const MainLayout = lazy(() => import('@/components/layouts/MainLayout'))
const AuthLayout = lazy(() => import('@/components/layouts/AuthLayout'))

const Login = lazy(() => import('@/components/screens/auth/Login'))
const Signup = lazy(() => import('@/components/screens/auth/Signup'))
const Logout = lazy(() => import('@/components/screens/auth/Logout'))

const Service = lazy(() => import('@/components/screens/patient/Service'))

const NotFound = lazy(() => import('@/components/screens/NotFound'))

import routes from './routes'

const App = () => {

    return (
        <Router>
            <Suspense fallback={<Loader />}>
                <Routes>

                    {/*routes.map(({path, protect, key, nodes}) => {
                        return (
                            <Route path={path} element={protect} key={key}>
                                {nodes.map(({path, element, key, protect}) => {
                                    if (!protect) {
                                        return <Route path={path} element={element} key={key}></Route>
                                    }

                                    return <Route path={path} element={protect} key={key}></Route>
                                })}
                            </Route>
                        )
                    })*/}


                    <Route path='/' element={
                        <AllowRoute>
                            <AuthLayout />
                        </AllowRoute>
                    }>
                        <Route path='login' element={<Login />} />
                        <Route path='signup' element={<Signup />} />
                        <Route path='logout' element={<Logout />} />
                    </Route>

                    <Route path='/' element={<MainLayout />}>
                        <Route path='service' element={<Service />} />
                    </Route>

                    {/*<Route path='/' element={
                        <ProtectedRoute>
                            <MainLayout />
                        </ProtectedRoute>
                    }>
                        <Route index />
                    </Route>*/}

                    <Route path='*' element={<NotFound />} />
                </Routes>
            </Suspense>
        </Router>
    )
}

export default App
