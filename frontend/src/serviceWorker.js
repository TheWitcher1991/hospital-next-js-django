export const register = config => {
    if ('serviceWorker' in navigator) {
        try {
            window.addEventListener('load', async () => {
                navigator.serviceWorker.register('./src/sw.js')
                    .then(() => navigator.serviceWorker.ready.then(worker => {
                        worker.sync.register('sync')
                        console.log('This web app is being served cache-first by a services worker')
                    }))
                    .catch((err) => console.log(err))
            })
        } catch (e) {
            console.log('serviceWorker not working')
        }

    }
}

export const unregister = () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.ready.then(async registration => await registration.unregister())
    }
}
