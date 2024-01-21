import React from 'react'

const useDebounce = (callback, timeout = 200, deps = []) => {
    const data = React.useRef({firstTime: true})

    React.useEffect(() => {
        const {firstTime, clearFunc} = data.current
        
        const handler = setTimeout(() => {
            if (clearFunc && typeof clearFunc === 'function') {
                clearFunc()
            }
            data.current.clearFunc = callback()
        })
        
        return () => clearTimeout(handler)
    }, [timeout, ...deps])
}

export default useDebounce