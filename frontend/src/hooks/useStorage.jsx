import React, { useState, useEffect } from 'react'

const getLocalStorage = (key, defaultValue) => {
    const saved = localStorage.getItem(key)
    const initial = !saved || saved === 'undefined' ? null : JSON.parse(saved)
    return initial || defaultValue
}

const useStorage = (key, defaultValue) => {
    const [name, setName] = useState(() => {
        return getLocalStorage(key, defaultValue);
    })

    useEffect(() => {
        (async () => {
            await localStorage.setItem(key, JSON.stringify(name))
        })()
    }, [key, name])

    return [name, setName]
}

export default useStorage