import React, {lazy} from 'react'

import ProtectedRoute from '@/routes/ProtectedRoute'
import AllowRoute from '@/routes/AllowRoute'

const MainLayout = lazy(() => import('@/components/layouts/MainLayout'))
const AuthLayout = lazy(() => import('@/components/layouts/AuthLayout'))

const Login = lazy(() => import('@/components/screens/auth/Login'))
const Signup = lazy(() => import('@/components/screens/auth/Signup'))
const Logout = lazy(() => import('@/components/screens/auth/Logout'))

const Service = lazy(() => import('@/components/screens/patient/Service'))

const NotFound = lazy(() => import('@/components/screens/NotFound'))

const routes = [
    {
        path: '/',
        protect: (
            <AllowRoute>
                <AuthLayout />
            </AllowRoute>
        ),
        key: Date.now(),
        nodes: [
            { path: 'login', element: <Login />, protect: false, key: Date.now(), },
            { path: 'signup', element: <Signup />, protect: false, key: Date.now(), },
            { path: 'logout', element: <Logout />, protect: false, key: Date.now(), }
        ]
    }
]

export default routes
