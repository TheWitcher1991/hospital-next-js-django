import React, {useMemo} from 'react'
import PropTypes from 'prop-types'

const AuthContext = React.createContext(null)

export const AuthProvider = ({userData, children}) => {
    let [user, setUser] = React.useState(userData)
    user = typeof user === 'string' ? JSON.parse(user) : user
    
    const values = useMemo(
        () => ({
            user,
            setUser
        }),
        [user]
    )
    
    return (
        <AuthContext.Provider value={values}>
             {children}
        </AuthContext.Provider>
    )
}

AuthProvider.propTypes = {
    children: PropTypes.any
}

export const useAuth = () => React.useContext(AuthContext)