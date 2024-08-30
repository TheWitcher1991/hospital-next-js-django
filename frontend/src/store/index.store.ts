import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import {
	AppMiddlewares,
	RTKQueryErrorLoggerMiddleware,
} from '@/store/index.middlewares'
import { persistedReducer } from '@/store/index.storage'
import {
	FLUSH,
	REHYDRATE,
	PAUSE,
	PERSIST,
	PURGE,
	REGISTER,
	persistStore,
} from 'redux-persist'

export const makeStore = () => {
	return configureStore({
		reducer: persistedReducer,
		devTools: process.env.NODE_ENV !== 'production',
		middleware: getDefaultMiddleware =>
			getDefaultMiddleware({
				serializableCheck: {
					ignoreActions: [
						FLUSH,
						REHYDRATE,
						PAUSE,
						PERSIST,
						PURGE,
						REGISTER,
					],
				},
			})
				.concat(RTKQueryErrorLoggerMiddleware)
				.concat(AppMiddlewares),
	})
}

export const store = makeStore()

export const persistor = persistStore(store)

setupListeners(store.dispatch)

export type AppStore = ReturnType<typeof makeStore>
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = AppStore['dispatch']
