import React from 'react'

const useInterval = (callback, delay) => {
    const savedCallback = React.useRef()
    
    React.useEffect(() => {
        savedCallback.current = callback
    }, [callback])
    
    React.useEffect(() => {
        const tick = () => savedCallback.current && savedCallback.current()
        
        if (delay !== null && delay > 0) {
            let id = setInterval(tick, delay)
            return () => clearInterval(id)
        } else {
            tick()
        }
    }, [delay])
}

export default useInterval