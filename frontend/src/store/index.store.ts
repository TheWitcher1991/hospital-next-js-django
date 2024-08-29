import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import { RootReducer } from '@/store/index.reducers'
import { AppMiddlewares } from '@/store/index.middlewares'

export const makeStore = () => {
	return configureStore({
		reducer: RootReducer,
		devTools: process.env.NODE_ENV !== 'production',
		middleware: (getDefaultMiddleware) =>
			getDefaultMiddleware().concat(AppMiddlewares),
	})
}

export const store = makeStore()

setupListeners(store.dispatch)

export type AppStore = ReturnType<typeof makeStore>
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = AppStore['dispatch']
